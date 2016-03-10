import collections
import pycosat
import itertools

from classtime.logging import logging
logging = logging.getLogger(__name__) # pylint: disable=C0103

import classtime

from classtime.brain.scheduling.schedule import Schedule


def find_schedules(schedule_params, num_requested):
    """
    :param dict schedule_params: parameters to build the schedule with.
        Check :ref:`api/generate-schedules <api-generate-schedules>`
        for available parameters.
    """
    logging.info('Received schedule request')

    if 'term' not in schedule_params:
        logging.error("Schedule generation call did not specify <term>")
    term = schedule_params.get('term', '')
    institution = schedule_params.get('institution', 'ualberta')
    cal = classtime.brain.get_calendar(institution)

    if 'courses' not in schedule_params:
        logging.error("Schedule generation call did not specify <courses>")
    course_ids = schedule_params.get('courses', list())
    busy_times = schedule_params.get('busy-times', list())
    preferences = schedule_params.get('preferences', dict())
    electives_groups = schedule_params.get('electives', list())
    for electives_group in electives_groups:
        if 'courses' not in electives_group:
            logging.warning('"courses" not found for electives. q={}'.format(
                schedule_params))

    schedules = _generate_schedules_sat(cal, term, course_ids, busy_times, electives_groups, preferences)
    schedules = _condense_schedules(cal, schedules)
    schedules = sorted(schedules,
                       reverse=True,
                       key=lambda s: s.overall_score())
    if not schedules:
        logging.error('No schedules found for q={}'.format(
            schedule_params))
    else:
        logging.info('Returning {}/{} schedules from request q={}'.format(
            min(num_requested, len(schedules)),
            len(schedules),
            schedule_params))
        debug_msg = 'Request q={q}\n' + \
                    'Response: Returning {ret} schedules\n' + \
                    '          including {ret_like} more like them\n' + \
                    '          out of {tot} total generated\n' + \
                    'Returning:\n{ret_schedules}'
        logging.debug(debug_msg.format(
            q=schedule_params,
            ret=min(num_requested,
                len(schedules)),
            ret_like=sum([len(s.more_like_this)
                          for s in schedules[:num_requested]]),
            tot=len(schedules) + sum([len(s.more_like_this)
                                     for s in schedules]),
            ret_schedules=schedules[:num_requested]))
    return schedules[:num_requested]


def _generate_schedules_sat(cal, term, course_ids, busy_times, electives_groups, preferences):
    schedules = []
    core_sections = [section
                     for course in cal.course_components(term, course_ids)
                     for component in course
                     for section in component]
    elective_group_course_ids = [eg.get('courses') for eg in electives_groups]
    for elective_course_ids in itertools.product(*elective_group_course_ids):
        sections = core_sections + [
            section
            for course in cal.course_components(term, elective_course_ids)
            for component in course
            for section in component
        ]
        schedules += _generate_schedules_sat_from_sections(sections, busy_times, preferences)
    return schedules


def _generate_schedules_sat_from_sections(sections, busy_times, preferences):
    clauses = []

    # Map from input domain to SAT domain
    # - input domain: course sections
    # - SAT domain: integers
    from_index, from_string, to_index = _build_section_index(sections)

    # Constraint: Must schedule one section for each core component
    core_clauses = collections.defaultdict(list)
    for core_section in sections:
        index = to_index[core_section.get('asString')]
        core_clauses[core_section.get('course') + core_section.get('component')].append(index)
    clauses += [v for k, v in core_clauses.iteritems()]

    # Constraint: Must not schedule conflicting sections together
    # Note: sections in the same component conflict
    # Note: recall (A' + B') == (AB)'
    conflict_clauses = []
    for a, b in _get_conflicts(sections, busy_times):
        if a.get('asString') != b.get('asString'):
            conflict_clauses.append([-1 * to_index[a.get('asString')],
                                     -1 * to_index[b.get('asString')]])
        else:
            conflict_clauses.append([-1 * to_index[a.get('asString')]])
    clauses += conflict_clauses

    # Solve the SAT problem and map back to input domain from SAT domain
    schedules = []
    for solution in pycosat.itersolve(clauses):
        sections = [from_index[i] for i in solution
                    if i > 0]
        schedules.append(Schedule(sections=sections,
                                  preferences=preferences))
        if len(schedules) > 100:
            break
    return schedules


def _build_section_index(components):
    from_index = {}
    from_string = {}
    to_index = {}
    for index, section in enumerate(components, 1):
        from_index[index] = section
        from_string[section.get('asString')] = section
        to_index[section.get('asString')] = index
        index += 1
    return from_index, from_string, to_index


def _get_conflicts(components, busy_times):
    conflicts = []
    for i, a in enumerate(components, 1):
        for j, b in enumerate(components, 1):
            if j <= i:
                continue
            if _conflicts(a, b, busy_times):
                conflicts.append([a,b])
    return conflicts


def _conflicts(section_a, section_b, busy_times):
    if section_a.get('course') == section_b.get('course') and \
       section_a.get('component') == section_b.get('component'):
        return True
    schedule = Schedule(busy_times=busy_times)
    if schedule.conflicts(section_a):
        return True
    schedule.add_section(section_a)
    if schedule.conflicts(section_b):
        return True
    return False


def _condense_schedules(cal, schedules):
    schedules = sorted(schedules,
                       key=lambda s: (s.overall_score(), s.timetable_bitmap))
    lag, lead = 0, 1
    condensed_indices = list()
    while lead < len(schedules):
        schedule, lead_schedule = schedules[lag], schedules[lead]
        if schedule.is_similar(lead_schedule):
            more_like_this_id = cal.get_schedule_identifier(lead_schedule)
            schedule.more_like_this.append(more_like_this_id)
            condensed_indices.append(lead)
        else:
            lag = lead
        lead += 1
    return [s for i, s in enumerate(schedules)
            if i not in condensed_indices]
