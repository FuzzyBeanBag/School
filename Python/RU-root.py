#!/usr/bin/python

import os

myUID = os.getuid()

if myUID == 0:
	print "You Are Root!"
elif myUID < 500:
	print "You are a SYSTEM account."
else:
	print "You're just a regular user."


if os.getenv('user') == "root":
	print "You Are Root!"
elif os.getuid() == 0:
	print "You are SUDO as Root."
elif os.access('/etc/shadow' .os.R_OK):
	print "You are not root, but you can read shadow"
else:
	print "No Soup for you!"

