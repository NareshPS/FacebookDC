#! /usr/bin/env python

import JabberHandler
import sys

jHandler	= JabberHandler.JabberHandler(sys.argv[1],sys.argv[2])
print jHandler.Connect()
for user in jHandler.FetchData(1):
	print user
#jHandler.DisConnect()

