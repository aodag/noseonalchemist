noseonalchemist
============================

nose plugin for reporting about commit counts on SQLAlchemy

USAGE
----------------

run nosetests with ``--with-commitreport``::

 $ nosetests --with-commitreport

you can get report of commit counts::

  /path/to/test1.py
  tests.test_it commit 2 times
  tests.test_it2 commit 11 times

  /path/to/test2.py
  tests2.test_it commit 2 times
  tests2.test_it2 commit 11 times

