
from classtime.core import db

class Term(db.Model):
    institution = db.Column(db.Text)
    term = db.Column(db.Text, primary_key=True, unique=True)
    termTitle = db.Column(db.Text)
    startDate = db.Column(db.Text)
    endDate = db.Column(db.Text)

    courses = db.relationship('Course')

    def __init__(self, jsonobj):
        for key, value in jsonobj.items():
            self.__setattr__(key, value)

    def __repr__(self):
        return '<Term #{num} ({name}) @ {institution}>'.format(
                num=self.term,
                name=self.termTitle,
                institution=self.institution)
