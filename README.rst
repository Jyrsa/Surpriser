You can clone the git repository by issuing command::

    git clone git://github.com/Jyrsa/Surpriser.git

In a Unix such as kosh.aalto.fi or kekkonen or any of the Niksula machines.

For a not-too-long and not-too-in-depth introduction to git see
http://www.vogella.de/articles/Git/article.html

Introduction
============

This repository contains an example demonstrated during my guest lecture at
the course T-106.1215 Basics of Programming part II at Aalto University.

It demonstrates technologies used in software development with python and is
intended to be used with python 2.7.



Setting up Virtualenv
=====================

To set up virtualenv to try this stuff, run::

    #set up a virtualenv called spanishenv
    virtualenv spanishenv
    #activate the newly created virtualenv
    source spanishenv/bin/activate.csh
    # there are several scripts, activate or activate.fish may be what you
    # want
    
    # install the required packages, listed in requirements.pip
    pip install -r requirements.pip

When you get tired of virtualenv, you can get rid of it with a simple command::
    
    deactivate

If you get tired of spanishenv, you can just rm -rf spanishenv. But do be
careful with rm -rf!

Quality Assurance
=================

To do quality assurance try::

    nosetests

Nose will collect classes and files that look like tests (based on their
name) and run them and report it's findings. 

You can find the tests written under spain/tests.py. They are incomplete as
special cases involving the file system haven't been tested for. What kinds of
things can happen in a file system? How could you test for them? Hint: think
about the special files in Unix systems.

Also, the command line parser is totally untested. How could you test command
line parsing? Hint: when testing stdout, sys.stdout was masked in the unit
test. Command line parameters are in the list sys.argv.

To measyre the readability quality of the source code try::

    pylint surpriser.py 

There are small issues because I was lazy doing this. Can you fix them easily?

You can measure coverage when running unit tests by passing the following
parameter to nosetests::

    nosetests --with-coverage

You can get a code coveragereport by running::

    coverage report

Note particularly that coverage doesn't report the file surprise.py as it
hasn't even been run by any nosetests. You shouldn always suspect if your
high coverage is real.

You can also measure the coverage of arbitary python executions, e.g.::
    
    coverage surprise.py -# 2
    coverage report


The virtualenv scripts seem broken for me in Niksula. If your path isn't set
correctly, you can run coverage, nosetests and pylint from
/path/to/spanishenv/bin directly. 

Extra
=====

For mad street cred make a change to this code and issue a pull-request to try
out git and GitHub. Python is all about collaborative effort. 

