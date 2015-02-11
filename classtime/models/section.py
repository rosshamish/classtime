
from classtime.core import db

class Section(db.Model):
    institution = db.Column(db.Text)
    term = db.Column(db.Text)
    course = db.Column(db.Text, db.ForeignKey('course.course'))
    class_ = db.Column(db.Text, primary_key=True, unique=True)
    section = db.Column(db.Text)
    component = db.Column(db.Text)
    classType = db.Column(db.Text)
    classStatus = db.Column(db.Text)
    enrollStatus = db.Column(db.Text)
    capacity = db.Column(db.Integer)

    session = db.Column(db.Text)
    campus = db.Column(db.Text)
    autoEnroll = db.Column(db.Text)
    # ("frequently null") classTopic = ...
    classNotes = db.Column(db.Text)
    # consent
    # gradingBasis
    # instructionMode
    # classUrl
    instructorUid = db.Column(db.Text)
    # examStatus
    # examDate
    # examStartTime
    # examEndTime
    # examLocation
    asString = db.Column(db.Text)

    day = db.Column(db.Text)
    startTime = db.Column(db.Text)
    endTime = db.Column(db.Text)
    location = db.Column(db.Text)

    schedule = db.Column(db.Text, db.ForeignKey('schedule.hash_id'))

    def __init__(self, jsonobj):
        for key, value in jsonobj.items():
            if key == 'class':
                key = 'class_'
            self.__setattr__(key, value)

    def __repr__(self):
        return '<Section: #{num} ({name}) @ {institution}>'.format(
                num=self.class_,
                name=self.asString,
                institution=self.institution)

    def to_dict(self):
        d = dict((col, getattr(self, col)) for col in self.__table__.columns.keys())
        d['class'] = d.get('class_')
        return d
