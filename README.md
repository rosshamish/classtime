![](http://i.imgur.com/YS6rK5F.png) classtime
=========
[![Documentation Status](https://readthedocs.org/projects/classtime/badge/?version=latest)](https://readthedocs.org/projects/classtime/?badge=latest)
[![Build Status](https://travis-ci.org/rosshamish/classtime.svg)](https://travis-ci.org/rosshamish/classtime)

##### An API for UAlberta course data and schedule generation

<hr />

> **Deprecation Notice**: classtime is deprecated as of April 11, 2017. It is no longer actively maintained, and the public API will no longer be available.

Classtime is an HTTP API for course data and schedule generation. It supports the [University of Alberta](https://ualberta.ca). The documentation is available online at http://classtime.rtfd.org.

It can be used to:

* browse terms
* browse courses
* get details on any course
* generate schedules, with support for core courses, electives, and preferences

It was developed in parallel with [winston](https://github.com/ahoskins/winston), http://heywinston.com, the official frontend. 

It is [well documented](#docs), [well tested](#tests), and there's half a plugin system written - if you're interested in porting it to your school, get in touch.

> Authors: [Ross Anderson](https://github.com/rosshamish), [Andrew Hoskins](https://github.com/ahoskins)

Examples
--------

GET /api/v1/terms
```javascript
{
  "objects": [
    {
      "endDate": "2007-12-05",
      "startDate": "2007-09-05",
      "term": "1210",
      "termTitle": "Fall Term 2007"
    },
    { <term object 2> },
    ...
    { <term object N> }
  ],
  ...
}
```

GET /api/v1/courses-min
```javascript
{
  objects = [
    {
      "faculty": "Faculty of Business",
      "subjects": [
        {
          "subject": "ACCTG",
          "subjectTitle": "Accounting",
          "courses": [
             {
                "course": "000001",
                "asString": "ACCTG 300",
                "courseTitle": "Intermediate Accounting"
             },
             { <course object> }
             ...
           ]
         },
         { <subject object> }
         ...
      ]
    },
    { <faculty object> }
    ...
  ]
}
```

GET /api/v1/courses/000001
```javascript
{
  "asString": "ACCTG 300",
  "career": "UGRD",
  "catalog": 300,
  "course": "000001",
  "courseDescription": "Provides a basic understanding of accounting: how accounting numbers are generated, the meaning of accounting reports, and how to use accounting reports to make decisions. Note: Not open to students registered in the Faculty of Business. Not for credit in the Bachelor of Commerce Program.",
  "courseTitle": "Introduction to Accounting",
  "department": "Department of Accounting, Operations and Information Systems",
  "departmentCode": "AOIS",
  "faculty": "Faculty of Business",
  "facultyCode": "BC",
  "subject": "ACCTG",
  "subjectTitle": "Accounting",
  "term": "1490",
  "units": 3
}
```

Generate schedules
GET /api/v1/generate-schedules?q={"institution":"ualberta","courses":["001343","004093"],"term":"1490"}
```javascript
{
  "objects": [
    {
      "sections": [
        {
          ...
          <course attributes>
          ...
          "class_": "62293",
          "component": "LEC",
          "day": "MWF",
          "startTime": "10:00 AM",
          "endTime": "10:50 AM",
          ...
          "section": "A02",
          "campus": "MAIN",
          "capacity": 0,
          "instructorUid": "jdavis",
          "location": "CCIS L2 190"
        },
        { <section object 2> },
        ...
        { <section object N> }
      ],
      "more_like_this": [<schedule-identifier>, <schedule-identifier>, ..]
    },
    { <schedule object 2> },
    ...
    { <schedule object M> }
  ],
  ...
}
```

Docs
----

Documentation is hosted at [classtime.readthedocs.org](http://classtime.readthedocs.org). The docs can also be [built locally](#building-the-docs).

#### Build docs locally

Documentation follows [reStructuredText] syntax, looks great when built with [sphinx], and is best viewed in a browser like [firefox] or [chrome].

Build with [sphinx]
> $ cd docs  
> $ make html  

View with [firefox], [chrome], or any other browser
> $ firefox _build/html/index.html &

[git]: http://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[python]: https://www.python.org/downloads/
[pip]: http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x
[firefox]: https://www.mozilla.org/en-US/firefox/new/
[chrome]: http://www.google.com/chrome/
[reStructuredText]: http://docutils.sourceforge.net/docs/user/rst/quickref.html
[sphinx]: http://sphinx-doc.org/
[issue-new]: https://github.com/rosshamish/classtime/issues/new
[issue-list]: https://github.com/rosshamish/classtime/issues
[issue-activity]: https://github.com/rosshamish/classtime/issues?q=is%3Aissue+sort%3Aupdated-desc
[milestones]: https://github.com/rosshamish/classtime/milestones

Tests
-----

[Nose][nose] is used for testing.

[Travis-ci][travis-ci] is set up to test the master branch, as well as all pull requests.

#### Run tests locally

> $ cd tests  
> $ nosetests

Testing is discussed in more detail in the [docs](#docs).

[nose]: https://nose.readthedocs.org/en/latest/
[travis-ci]: https://travis-ci.org/rosshamish/classtime

Contributing
------------

The project is no longer actively maintained. If you'd like to contribute, get in touch first.

Commit messages loosely follow the [Angular.js commit message style guide][commit-style-guide].  The purpose is to sprinkle about 10 characters of background information into the front of each commit message.

[commit-style-guide]: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit?pli=1

#### Getting started

Get the code with [git]
> $ git clone https://github.com/rosshamish/classtime  
> $ cd classtime

Install dependencies with [pip]
> $ pip install -r requirements.txt

Run the server with [python 2][python] (not 3)
> $ python runserver.py  
> Server running on http://localhost:5000 ...

Get terms in [chrome] or [firefox]
> GET http://localhost:5000/api/v1/terms

Get courses
> GET http://localhost:5000/api/v1/courses

Get schedules
> GET http://localhost:5000/api/v1/generate-schedules?q={"institution":"ualberta","courses":["001343","004093"],"term":"1490"}

Thanks
------

[Mason Strong](https://github.com/codingHappiness) ([contact](mailto:mstrong@ualberta.ca)) and [Peter Crinklaw](http://blackacrebrewing.com/hey.swf) for ideas, advice, and for sharing the code from their Cmput 275 schedule-builder project as a point of reference.

[Ryan Shea](http://ryaneshea.com) for his [angular-flask app boilerplate](https://github.com/rxl/angular-flask)

With inspiration from
---------------------
- [morinted, t0xicCode, and DanielMurdoch's 'schedule-generator' for the University of Ottawa](https://github.com/morinted/schedule-generator)
- [cosbynator's 'course qualifier' for the University of Waterloo](https://github.com/cosbynator/Course-Qualifier), demo: http://www.coursequalifier.com/
- [Uberi's 'COURSERATOR3000' for the University of Waterloo](https://github.com/Uberi/COURSERATOR3000)
- [scott113341's 'SCUclasses' for Santa Clara University](https://github.com/scott113341/SCUclasses), demo: http://scuclasses.com
- [adicu's 'Courses' for Columbia University](https://github.com/adi-archive/Schedule-Builder), demo: http://courses.adicu.com
- [adiciu's course data API for Columbia University](https://github.com/adicu/data.adicu.com)
- [arxanas's 'schedumich' for the University of Michigan](https://github.com/arxanas/schedumich)
- [and others](https://github.com/search?o=desc&q=university+scheduling&ref=searchresults&s=stars&type=Repositories&utf8=%E2%9C%93)
