import os
import sys
from classtime import app

def is_main_process():
    return os.environ.get('WERKZEUG_RUN_MAIN')

def idly_fill():
    from classtime.brain import AcademicCalendar
    for institution in ['ualberta']:
        AcademicCalendar.idly_fill(institution)

def runserver():
    if is_main_process() and len(sys.argv) <= 1:
        idly_fill()
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)

if __name__ == '__main__':
    runserver()
elif os.environ.get('SECRET_KEY'):
    idly_fill()
