
import unittest

from classtime.brain.scheduling import Schedule

class TestSchedule(unittest.TestCase): #pylint: disable=R0904
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_section_add(self):
        def assert_section_add(section, numblocks_expected):
            """
            Check that adding a given section to a new Schedule
            - fills the expected number of timetable blocks
            """
            schedule = Schedule()
            schedule.add_section(section)
            numblocks = 0
            for day in schedule.timetable:
                for block in day:
                    if block is not Schedule.OPEN:
                        numblocks += 1
            assert numblocks == numblocks_expected

        testcases = [
            {
                'day': 'TR',
                'startTime': '08:00 AM',
                'endTime': '08:50 AM',

                'expected': 4
            },
            {
                'day': 'MTWRF',
                'startTime': '08:00 AM',
                'endTime': '08:50 AM',

                'expected': 10
            },
            {
                'day': 'TR',
                'startTime': '08:00 AM',
                'endTime': '08:50 PM',

                'expected': 52
            },
            {
                'day': 'TR',
                'startTime': '08:00 AM',
                'endTime': '09:20 AM',

                'expected': 6
            },
            {
                'day': 'M',
                'startTime': '06:00 PM',
                'endTime': '08:50 PM',

                'expected': 6
            }
        ]
        for section in testcases:
            assert_section_add(section,
                section.get('expected'))

    def test_busy_time_add(self):
        def assert_busy_time_add(busy_time, numblocks_expected):
            """
            Check that adding a given busy_time to a new Schedule
            - fills the expected number of timetable blocks
            """
            schedule = Schedule()
            schedule.add_busy_time(busy_time)
            numblocks = 0
            for day in schedule.timetable:
                for block in day:
                    if block is not Schedule.OPEN:
                        numblocks += 1
            assert numblocks == numblocks_expected

        testcases = [
            {
                'day': 'TR',
                'startTime': '08:00 AM',
                'endTime': '08:50 AM',

                'expected': 4
            },
            {
                'day': 'MTWRF',
                'startTime': '08:00 AM',
                'endTime': '08:50 AM',

                'expected': 10
            },
            {
                'day': 'TR',
                'startTime': '08:00 AM',
                'endTime': '08:50 PM',

                'expected': 52
            },
            {
                'day': 'TR',
                'startTime': '08:00 AM',
                'endTime': '09:20 AM',

                'expected': 6
            },
            {
                'day': 'M',
                'startTime': '06:00 PM',
                'endTime': '08:50 PM',

                'expected': 6
            }
        ]
        for section in testcases:
            assert_busy_time_add(section,
                section.get('expected'))

    def test_busy_time_overlap(self):
        """
        See github.com/rosshamish/classtime/issues/96
        """
        def assert_busy_time_overlap_doesnt_double(busy_times, numblocks_expected):
            """
            Check that adding the same busy_time more than once to a new Schedule
            is idempotent
            """
            schedule = Schedule()
            bitmaps_set = set()
            for busy_time in busy_times:
                schedule.add_busy_time(busy_time)
                bitmaps_set.add(''.join(bin(day_bitmap) for day_bitmap in schedule.timetable_bitmap))
            assert len(bitmaps_set) == 1

            numblocks = 0
            for day in schedule.timetable:
                for block in day:
                    if block is not Schedule.OPEN:
                        numblocks += 1
            assert numblocks == numblocks_expected
        testcases = [
            {
                'busy_times': [
                    {
                        'day': 'W',
                        'startTime': '08:00 AM',
                        'endTime': '08:20 AM',
                    },
                    {
                        'day': 'W',
                        'startTime': '08:00 AM',
                        'endTime': '08:20 AM',
                    }
                ],
                'expected': 1
            }
        ]
        for testcase in testcases:
            assert_busy_time_overlap_doesnt_double(testcase.get('busy_times'),
                testcase.get('expected'))

    def test_conflict_recognition(self): #pylint: disable=R0201
        def assert_conflict_recognition(sections, has_conflict):
            """
            Assert that a list of sections has either:
            - one or more conflicts, or
            - no conflicts
            """
            schedule = Schedule()
            for section in sections:
                if schedule.conflicts(section):
                    assert has_conflict == True
                    return
                else:
                    schedule.add_section(section)
            assert has_conflict == False

        testcases = [
            {
                'expected': True,
                'sections':
                [
                    {
                        'day': 'TR',
                        'startTime': '08:00 AM',
                        'endTime': '08:50 AM'
                    },
                    {
                        'day': 'MTWRF',
                        'startTime': '08:00 AM',
                        'endTime': '08:50 AM'
                    }
                ]
            },
            {
                'expected': False,
                'sections':
                [
                    {
                        'day': 'TR',
                        'startTime': '08:00 AM',
                        'endTime': '08:50 AM'
                    },
                    {
                        'day': 'TR',
                        'startTime': '09:00 AM',
                        'endTime': '09:50 AM'
                    }
                ]
            },
            {
                'expected': False,
                'sections':
                [
                    {
                        'day': 'TR',
                        'startTime': '07:00 PM',
                        'endTime': '07:50 PM'
                    },
                    {
                        'day': 'TR',
                        'startTime': '08:00 PM',
                        'endTime': '09:00 PM'
                    }
                ]
            },
            {
                'expected': True,
                'sections':
                [
                    {
                        'day': 'TR',
                        'startTime': '07:00 PM',
                        'endTime': '07:50 PM'
                    },
                    {
                        'day': 'TR',
                        'startTime': '08:00 PM',
                        'endTime': '09:00 PM'
                    },
                    {
                        'day': 'TR',
                        'startTime': '08:30 PM',
                        'endTime': '08:50 PM'
                    }
                ]
            }
        ]
        for scenario in testcases:
            assert_conflict_recognition(scenario.get('sections'),
                scenario.get('expected'))

    def test_comparison_called_but_no_courses(self):
        sched = Schedule(sections=[], preferences={'no-marathons': 1})
        sched.is_similar(Schedule())

def test_preferences_null_values():
    sched = Schedule(preferences={ 'no-marathons': None })
    sched.overall_score() # should not raise an exception
