> Find a university schedule that fits your life in less than 5 minutes

classtime offers university course catalog access **and** schedule generation capabilities through a convenient REST API. It is well documented, well tested, and actively maintained.

It enables frontends which improve the course registration experience of post-secondary students.

It currently supports the [University of Alberta](http://ualberta.ca), and is intended to pair nicely with [BearTracks](https://beartracks.ualberta.ca).

The official frontend is maintained by [Andrew Hoskins](https://github.com/ahoskins) at [ahoskins/winston](https://github.com/ahoskins/winston). 

Maintainer: [Ross Anderson](https://github.com/rosshamish)

API Examples
------------

Once this repo is open-sourced, API examples will be hosted on readthedocs. Until then, build the docs locally to view API examples (instructions below).

Contributing
------------

Commit messages loosely follow the [Angular.js commit message style guide][commit-style-guide].  The purpose is to sprinkle about 10 characters of background information into the front of each commit message.

For the most part, commit messages are written in the present tense - the message tells others what the commit will **do** if they merge it into their branch.

Template

	type(context): change X to Y from Z

Good

	a4kd93 feat(schedule-generation): add electives support to the API  
	bd8663 docs(api): document new electives support  
	9d9f77 tests(schedule-generation): add tests to verify sane scheduling of electives

Not good

	a4kd93 api has electives now  
	bd8663 documented electives feature  
	9d9f77 hopefully electives work, tests are in now

Github issues are used for discussion, questions, and task tracking. Don't worry about assigning labels.

[commit-style-guide]: https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit?pli=1

Building the docs
-----------------

Documentation follows [reStructuredText] syntax, looks great when built with [sphinx], and is best viewed in a browser like [firefox] or [chrome].

Clone the project with [git]
> $ git clone https://github.com/rosshamish/classtime  
> $ cd classtime  

Install requirements with [pip]
> $ pip install -r requirements.txt  

Build with [sphinx]
> $ cd docs  
> $ make html  

View with [firefox], [chrome], or any other browser
> $ firefox _build/html/index.html &

When documentation is unclear, missing, or incorrect, [add an issue][issue-new] to the [docs work queue][milestones].

[git]: http://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[pip]: http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x
[firefox]: https://www.mozilla.org/en-US/firefox/new/
[chrome]: http://www.google.com/chrome/
[reStructuredText]: http://docutils.sourceforge.net/docs/user/rst/quickref.html
[sphinx]: http://sphinx-doc.org/
[issue-new]: https://github.com/RossHamish/classtime/issues/new
[milestones]: https://github.com/RossHamish/classtime/milestones

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
