""" WSGI script for loading the lsgauge application into Apache """

import sys

if sys.version_info[0]<3:       # require python3
 raise Exception("Python3 required! Current (wrong) version: '%s'" % sys.version_info)

# This is the path to the application code.
# Add it to the python load path
sys.path.insert(0, '/home/pi/lsgauge/')

# Finally load our app.
from lsgauge import application as application

