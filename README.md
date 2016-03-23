![](http://i.imgur.com/YS6rK5F.png) classtime
=========
[![Documentation Status](https://readthedocs.org/projects/classtime/badge/?version=latest)](https://readthedocs.org/projects/classtime/?badge=latest)

Classtime is an HTTP API for course data and schedule generation at UAlberta. This repo contains the documentation, which is available online at http://classtime.rtfd.org.

Purpose: “Build a university schedule that fits your life in less than five minutes”

It can be used for the following:

* browse terms
* browse courses
* get details on any course
* generate schedules, with support for core courses, electives, and preferences

Classtime currently only supports the University of Alberta.

> Maintainers: [Ross Anderson](https://github.com/rosshamish), [Andrew Hoskins](https://github.com/ahoskins)

Demo
----

Get terms: https://classtime.herokuapp.com/api/v1/terms
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

Get courses: https://classtime.herokuapp.com/api/v1/courses-min
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

Get detailed information about a particular course: https://classtime.herokuapp.com/api/v1/courses/000001
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

Generate schedules: https://classtime.herokuapp.com/api/v1/generate-schedules?q={"institution":"ualberta","courses":["001343","004093"],"term":"1490"}
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

Filter data requests by any field, e.g. https://classtime.herokuapp.com/api/v1/courses-min?q={"filters":[{"name":"institution","op":"equals","val":"ualberta"},{"name":"term","op":"equals","val":"1570"}]}

Building the documentation
----

Documentation follows [reStructuredText] syntax, looks great when built with [sphinx], and is best viewed in a browser like [firefox] or [chrome].

Build with [sphinx]
```bash
$ pip install -U Sphinx
$ cd docs
$ make html
```  

View with [firefox], [chrome], or any other browser
```bash
$ firefox _build/html/index.html &
```

[firefox]: https://www.mozilla.org/en-US/firefox/new/
[chrome]: http://www.google.com/chrome/
[reStructuredText]: http://docutils.sourceforge.net/docs/user/rst/quickref.html
[sphinx]: http://sphinx-doc.org/

Thanks
------

[Mason Strong](https://github.com/codingHappiness) ([contact](mailto:mstrong@ualberta.ca)) and [Peter Crinklaw](http://blackacrebrewing.com/hey.swf) for ideas, advice, and for sharing the code from their Cmput 275 schedule-builder project as a point of reference.

[Ryan Shea](http://ryaneshea.com) for his [angular-flask app boilerplate](https://github.com/rxl/angular-flask)

Prior art / see also
--------------------
- [morinted, t0xicCode, and DanielMurdoch's 'schedule-generator' for the University of Ottawa](https://github.com/morinted/schedule-generator)
- [cosbynator's 'course qualifier' for the University of Waterloo](https://github.com/cosbynator/Course-Qualifier), demo: http://www.coursequalifier.com/
- [Uberi's 'COURSERATOR3000' for the University of Waterloo](https://github.com/Uberi/COURSERATOR3000)
- [scott113341's 'SCUclasses' for Santa Clara University](https://github.com/scott113341/SCUclasses), demo: http://scuclasses.com
- [adicu's 'Courses' for Columbia University](https://github.com/adi-archive/Schedule-Builder), demo: http://courses.adicu.com
- [adiciu's course data API for Columbia University](https://github.com/adicu/data.adicu.com)
- [arxanas's 'schedumich' for the University of Michigan](https://github.com/arxanas/schedumich)
- [and others](https://github.com/search?o=desc&q=university+scheduling&ref=searchresults&s=stars&type=Repositories&utf8=%E2%9C%93)
