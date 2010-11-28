#! /usr/bin/env python

import JabberHandler
import JabberErrors
import sys

jErrors		= JabberErrors.JabberErrors()
jHandler	= JabberHandler.JabberHandler(sys.argv(1),sys.argv(2),'chat.facebook.com')
jErrorCode	= jHandler.Connect()
if jErrorCode is jErrors.getSuccessCode():
	jHandler.Present()
	for user in jHandler.FetchData(1):
		print user
else:
	print jErrorCode
	print 'Connection Error'

#jHandler.DisConnect()

