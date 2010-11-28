#! /usr/bin/env python

""" This class defines common errors for JabberHandler"""
class JabberErrors:
	
	sucError	= 100
	conError	= sucError+1
	authError	= conError+1

	def getConnectionError(self):
		return self.conError

	def getAuthError(self):
		return self.authError

	def getSuccessCode(self):
		return self.sucError

