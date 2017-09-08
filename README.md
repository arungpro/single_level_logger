# Configure Log Level

## Overview

single_level_logger is a log trace program that can be configured <br />
to display number of above and below lines from the line of match for <br />
the query.

Though the scope of the program remain to the first find of pattern <br />
that we have requested for.

Due to time constraints the program is rolled out on an intend.<br />
There are sample screen shots attached.

## Pre-requisite:

Python 2.7 and above

## How to USE:

In `logger.py` file update the `get` call with search string and number <br />
of line bound, That you are interested.

example: `logger.get('docker-compose', 1, 2)`

![This how it looks](https://github.com/arungpro/single_level_logger/blob/master/log.png)
