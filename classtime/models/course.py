
from classtime.core import db

class Course(db.Model):
    institution = db.Column(db.Text, primary_key=True)
    term = db.Column(db.Text, primary_key=True)
    course = db.Column(db.Text, primary_key=True)
    subject = db.Column(db.Text)
    subjectTitle = db.Column(db.Text)
    catalog = db.Column(db.Text)
    courseTitle = db.Column(db.Text)
    courseDescription = db.Column(db.Text)
    facultyCode = db.Column(db.Text)
    faculty = db.Column(db.Text)
    departmentCode = db.Column(db.Text)
    department = db.Column(db.Text)
    career = db.Column(db.Text)
    units = db.Column(db.Float)
    asString = db.Column(db.Text)

    sections = db.relationship('Section')

    __table_args__ = (db.ForeignKeyConstraint(['institution', 'term'],
                                           ['term.institution', 'term.term']),
                      {})

    def __init__(self, jsonobj):
        for key, value in jsonobj.items():
            self.__setattr__(key, value)

    def __repr__(self):
        return '<Course: #{num} ({name}) @ {institution}>'.format(
                num=self.course,
                name=self.asString,
                institution=self.institution)

    def to_dict(self):
        return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())
        