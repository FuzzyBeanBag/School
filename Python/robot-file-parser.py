#!/usr/bin/python
#
#=====================================================
# NSSB 246 - Python Scripting
# Taylor McGee
# 05-15-2017
# RobotParser.py
#=====================================================

import robotparser

sites = ['www.robotstxt.org']

def getDenies(site):

		paths = []

#Create a new robot parser instance and read the site's robot file.
#
		robot = robotparser.robotfileparser()
		robot.set_url("http://www.robotstxt.org/robots.txt")
		robot.read()
#
# For each entry, look at the rule lines and add the path to paths if disallowed.
#
		for entry in robot.entries:
			for line in entry.rulelines:
				not line.allowance and paths.append(line.path)
				return set(paths)

			for site in sites:
				print "Denies for " + site
				print "\t" + "\n\t".join(getDenies(site))

