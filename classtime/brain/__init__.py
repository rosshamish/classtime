
import os
import json

from classtime.logging import logging
logging = logging.getLogger(__name__) # pylint: disable=C0103

from classtime.core import db
from classtime.models import Institution

from .academic_calendar import AcademicCalendar

def get_calendar(institution):
    return AcademicCalendar(institution)
