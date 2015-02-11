==================
The Local Database
==================

The local database is used as a cache for the remote database. Schedule
generation requests will fetch section data from the remote server when
necessary, but terms and courses must be manually seeded.

If one of the following is true, terms and courses will be lazily downloaded
in the background
 - the server is run via python with zero arguments :code:`$ python runserver.py`
 - the server is run via gunicorn and SECRET_KEY is set :code:`$ export SECRET_KEY=something; gunicorn runserver:app -w 3`

By default, a local database is stored as a SQLite database in the filesystem
at /tmp/classtime.db . In production, PostgreSQL is used, so if you are
developing for prod and want to match your environment (because dev/prod parity
is a good thing), do the following:

1. Install PostgreSQL
2. Set DATABASE_URL to your postgre URI

That's it! It should just work.

.. _`seed-db`:

seed\_db
~~~~~~~~

Seed the database with the specified term and all courses in it.

::

 $ python manage.py seed_db [--term TERM]

:TERM: :ref:`4-digit unique term identifier <4-digit-term-identifier>`
       , default='1490' (Fall Term 2014)

.. _`delete-db`:

delete\_db
~~~~~~~~~~

Delete the database completely. This is irreversible.

::

 $ python manage.py delete_db

.. _`refresh-db`:

refresh\_db
~~~~~~~~~~~

Delete and rebuild the database with the specified term and all courses
in it 

::

 $ python manage.py refresh_db [--term TERM]

:TERM: :ref:`4-digit unique term identifier <4-digit-term-identifier>`
       , default='1490' (Fall Term 2014)
