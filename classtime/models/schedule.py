
import hashlib

from classtime.core import db

SCHEDULE_HASH_LENGTH = 30
def calculate_schedule_hash(section_ids, institution, term):
    md5 = hashlib.md5()
    for section_id in section_ids:
        md5.update(section_id)
    md5.update(institution)
    md5.update(term)
    return md5.hexdigest()[:SCHEDULE_HASH_LENGTH]

# Coordinates many-to-many relationship between schedules and sections
sections = db.Table('sections',
    db.Column('institution', db.Text),
    db.Column('term', db.Text),
    db.Column('course', db.Text),
    db.Column('section_id', db.Text),
    db.Column('schedule_id', db.String(SCHEDULE_HASH_LENGTH)),
    db.ForeignKeyConstraint(['institution', 'term', 'course', 'section_id'],
        ['section.institution', 'section.term', 'section.course', 'section.class_']),
    db.ForeignKeyConstraint(['institution', 'term', 'schedule_id'],
        ['schedule.institution', 'schedule.term', 'schedule.hash_id'])
)

class Schedule(db.Model):
    institution = db.Column(db.Text, primary_key=True)
    term = db.Column(db.Text, primary_key=True)
    sections = db.relationship('Section', secondary=sections)
    hash_id = db.Column(db.String(SCHEDULE_HASH_LENGTH), primary_key=True, unique=True)
    asString = db.Column(db.Text)
    __table_args__ = (db.ForeignKeyConstraint(['institution', 'term'],
                                           ['term.institution', 'term.term']),
                      {})

    def __init__(self, jsonobj):
        for key, value in jsonobj.items():
            setattr(self, key, value)
        self.asString = '<{}..> in <term={}> at <{}>'.format(
            self.hash_id[:6], self.term, self.institution)

    def __repr__(self):
        return '<Schedule: ({asString}) @ {institution}>'.format(
                asString=self.asString,
                institution=self.institution)
