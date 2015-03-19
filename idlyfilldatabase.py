import os
import sys
from classtime import app

def is_main_process():
    return os.environ.get('WERKZEUG_RUN_MAIN')

def idly_fill():
    from classtime.brain import AcademicCalendar
    for institution in ['ualberta']:
        AcademicCalendar.idly_fill(institution, sleeptime=2, force_refresh=True)

def runserver():
    if is_main_process():
        idly_fill()
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)

if __name__ == '__main__':
    idly_fill()
