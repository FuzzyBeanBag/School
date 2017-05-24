#!/usr/bin/python
#
# NSSB 246 - Python Scripting
# Taylor McGee
# 05-16-2017
#
# WebCheck.py
# ex: ./webCheck.py <hostname> -p 80
# Re-Wrote the script as the book didnt define against errors
# this is more true and looks for port 80 and 443 for service
# and reports back status.

import httplib
import sys
import socket
import argparse
from optparse import OptionParser


usageString = "\n %prog hostname \n %prog -p <port 80 or 443> hostname \n\n Example: %prog www.google.com \n Example: %prog -p 80 www.google.com \n Example: %prog -p 443 www.google.com"
parser = OptionParser(usage=usageString)
parser.add_option("-p", "--port", dest="port", metavar="PORT", default=80, type="int", help="Port to connect to")
(opts,args) = parser.parse_args()

if len(args) < 1:
	parser.error("Hostname is required")


host = args[0]
port = opts.port


try:

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))

except socket.gaierror, e:

  print host + " : Down: %s" % e
  sys.exit(1)

else:

#Check to see if we are going to check port 80 or 443 for host up.
  if (port == 443):
    client = httplib.HTTPSConnection(host,port)
    client.request("GET","/")
    resp = client.getresponse()
    client.close

    if resp.status == 200:
      print host + " : ", port, " OK"
      sys.exit()

  elif (port == 80):
    client = httplib.HTTPConnection(host,port)
    client.request("GET","/")
    resp = client.getresponse()
    client.close()

    if resp.status == 200:
      print host + " : ", port, " OK"
      sys.exit()

  else:
    print "This is a WebCheck script that checks port 80 or port 443,\nAll other ports will not work correctly and may cause Errors."
    sys.exit()



