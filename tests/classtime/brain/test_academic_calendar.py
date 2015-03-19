
from __future__ import absolute_import

import unittest

from classtime.core import db
from classtime.models import Course
from classtime.brain import AcademicCalendar

class TestAcademicCalendar(unittest.TestCase): # pylint: disable=R0904
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

def test_courses_unique_across_terms():
	cal = AcademicCalendar('ualberta')
	db.drop_all()
	db.create_all()

	terms = cal._fetch(datatype='terms')
	cal._save(terms, datatype='terms')

	courses = cal._fetch(datatype='courses', term='1510')
	cal._save(courses, datatype='courses')
	courses_overlapping = cal._fetch(datatype='courses', term='1520')
	cal._save(courses_overlapping, datatype='courses')

	assert len(Course.query.all()) == len(courses) + len(courses_overlapping)
