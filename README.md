![](http://i.imgur.com/YS6rK5F.png) classtime
=========
[![Documentation Status](https://readthedocs.org/projects/classtime/badge/?version=latest)](https://readthedocs.org/projects/classtime/?badge=latest)
[![Build Status](https://travis-ci.org/rosshamish/classtime.svg)](https://travis-ci.org/rosshamish/classtime)


##### UAlberta course data and schedule generation as a REST API

<hr />

classtime is a platform-agnostic data source for building rich applications for [University of Alberta](https://ualberta.ca) students.

It was developed in parallel with [winston](https://github.com/ahoskins/winston), the official frontend.

It is [well documented](#docs), [well tested](#tests), and [actively maintained][issue-activity].

There is preliminary support for plugging in other schools, and contributions of that nature are welcome and encouraged. [Open an issue][issue-new] to discuss adding support for your school.

> Maintainers: [Ross Anderson](https://github.com/rosshamish), [Andrew Hoskins](https://github.com/ahoskins)

Get started
-----------

Get the code with [git]
> $ git clone https://github.com/rosshamish/classtime  
> $ cd classtime

Install dependencies with [pip]
> $ pip install -r requirements.txt

Run the server with [python 2][python] (not 3)
> $ python runserver.py  
> Server running on http://localhost:5000 ...

Get terms in [chrome] or [firefox]
> GET http://localhost:5000/api/terms

Get courses
> GET http://localhost:5000/api/courses

Get schedules
> GET http://localhost:5000/api/generate-schedules?q={"institution":"ualberta", "courses":["001343","004093"], "term":"1490"}

Docs
----

Documentation is hosted at [classtime.readthedocs.org](http://classtime.readthedocs.org). The docs can also be [built locally](#building-the-docs).

When documentation is unclear, missing, or incorrect, [add an issue][issue-new] to the [docs work queue][milestones].

### Building the docs

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

> $ cd tests  
> $ nosetests

[Travis-ci][travis-ci] is used to test all pushes to master, as well as all pull requests.

Testing is discussed in more detail in the [docs](#docs).

[nose]: https://nose.readthedocs.org/en/latest/
[travis-ci]: https://travis-ci.org/rosshamish/classtime

Get involved
------------

Use [Github Issues][issue-list] for discussion, questions, and task tracking. Don't worry about assigning labels.

Commit messages loosely follow the [Angular.js commit message style guide][commit-style-guide].  The purpose is to sprinkle about 10 characters of background information into the front of each commit message.

[commit-style-guide]: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit?pli=1

Thanks
------

[Mason Strong](https://github.com/hadacigar) ([contact](mailto:mstrong@ualberta.ca)) and [Peter Crinklaw](http://blackacrebrewing.com/hey.swf) for ideas, advice, and for sharing the code from their Cmput 275 schedule-builder project as a point of reference.

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
