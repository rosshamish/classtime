===========
Get started
===========

Purpose
~~~~~~~

This is a REST API which enables rich web applications based on University of Alberta course data.

The goal is to give students at the University of Alberta more flexibility, more options, and more freedom in choosing their timetable each semester.

This API enables the following functionality.

- Students are able to
    * browse available courses from any term
    * find out more about each course
    * block off times in the week for sleeping, for work, for seeing friends, etc
    * pick courses
    * pick electives
    * browse matching timetables

The official frontend lives at `ahoskins/winston <https://github.com/ahoskins/winston>`__.

Get set up
~~~~~~~~~~

Get `pip <https://pip.readthedocs.org/en/latest/>`__, for installing dependencies. On Ubuntu, do ::

 $ sudo apt-get install pip

Clone the source ::

 $ git clone https://github.com/rosshamish/classtime classtime
 $ cd classtime

Install dependencies ::

 $ sudo pip install -r requirements.txt

Check it out
~~~~~~~~~~~~

Run the server ::

 $ python runserver.py

Send a request to the API ::

 GET http://localhost:5000/api/v1/terms

Troubleshooting
~~~~~~~~~~~~~~~

If the install fails, you might also need to `install python-ldap's
dependencies manually <http://stackoverflow.com/questions/4768446/python-cant-install-python-ldap>`__

virtualenv
~~~~~~~~~~

A virtual environment is an isolated build environment best used on a
per-project basis. It is recommended to use one. A good option is
`virtualenv <http://virtualenv.readthedocs.org/en/latest/virtualenv.html>`__.

Usage ::

	$ virtualenv venv # create a virtual environment in the folder 'venv'
	$ . venv/bin/activate  # activate the virtual environment
	(venv)$ pip install -r requirements.txt # install dependencies to the virtual environment