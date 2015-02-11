
from classtime.core import db

class Institution(db.Model):
    institution = db.Column(db.Text, primary_key=True, unique=True)
    name = db.Column(db.Text)

    def __init__(self, jsonobj):
        for key, value in jsonobj.items():
            self.__setattr__(key, value)

    def __repr__(self):
        return '<Institution: {institution} ({name})>'.format(
                institution=self.institution,
                name=self.name)
        