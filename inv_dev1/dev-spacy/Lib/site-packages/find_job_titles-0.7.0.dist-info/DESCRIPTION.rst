===============
find_job_titles
===============

.. image:: https://img.shields.io/pypi/v/find_job_titles.svg
        :target: https://pypi.python.org/pypi/find_job_titles

.. image:: https://img.shields.io/pypi/pyversions/find_job_titles.svg
        :target: https://pypi.python.org/pypi/find_job_titles

.. image:: https://img.shields.io/travis/fluquid/find_job_titles.svg
        :target: https://travis-ci.org/fluquid/find_job_titles

.. image:: https://codecov.io/github/fluquid/find_job_titles/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/fluquid/find_job_titles

Find Job Titles in Strings

* Free software: MIT license
* Python versions: 2.7, 3.4+

Features
--------

* Find any of 77k job titles in a given string
* Text processing is extremely fast using "acora" library
* Dictionary generation takes about 20 seconds upfront

Quickstart
----------

Instantiate "Finder" and start extracting job titles::

    >>> from find_job_titles import Finder
    >>> finder.findall('I am the Senior Vice President')
    [('Senior Vice President', 9),
     ('Vice President', 16),
     ('President', 21)]

All possible, overlapping matches are returned.
Matches contain positional information of where the match was found.

Alternatively use "finditer" for lazy consumption of matches::

    >>> finder.finditer('I am the Senior Vice President')]
    <generator object ...>

Credits
-------

This package was created with Cookiecutter_ and the `fluquid/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fluquid/cookiecutter-pypackage`: https://github.com/fluquid/cookiecutter-pypackage

=======
History
=======


0.7.0 (2017-08-22)
------------------

* fixed tox tests for py27 re: different unicode treatment by acora and pyahocorasick
* only testing default `Finder` using pyahocorasick now.

0.6.0 (2017-08-22)
------------------

* rewrote and fixed longest match code
* added pyahocorasick implementation and made default
* added params to enable/disable longest matches

0.5.0 (2017-08-22)
------------------

0.4.0 (2017-08-21)
------------------

* updated title list with marketing execs
* set non-dev version

0.3.0-dev (2017-08-18)
----------------------

* updated title list (- surnames, - blacklist, + added_roles)

0.2.0-dev (2017-08-18)
----------------------

* proper tracking of code with releases

0.1.0 (unreleased)
------------------

* First release on PyPI.

