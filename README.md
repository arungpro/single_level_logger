single_level_logger
----------------------

single_level_logger is a log trace program that can be configured to display number of above and below lines from the line of match for the query.

Though the scope of the program remain to the first find of pattern that we have requested for.

Due to time constraints the program is rolled out on an intend. There are sample screen shots attached.

Pre-requisite:
----------------
Python 2.7 and above

How to USE:
------------

In `logger.py` file update the `get` call with search string and number of line bound, That you are interested.
example: `logger.get('docker-compose', 1, 2)`

![This how it looks](https://github.com/arungpro/single_level_logger/blob/master/log.png)
