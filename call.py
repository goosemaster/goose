import os
import sys
from subprocess import call


CMD = sys.argv[1]

#call(["ls", "-l"])

if len(sys.argv) < 2:
    sys.exit('Usage: call.py system command' % sys.argv[0])



output = call([CMD])
response = str(output)
test = type(response)
