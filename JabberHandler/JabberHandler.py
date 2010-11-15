#! /usr/bin/env python

import logging
import xmpp
import JabberErrors

'''Class to authenticate the user with Facebook'''

class JabberHandler:

	jId				= None
	jClient			= None
	jCon			= None
	jJabberErrors	= None
	jUser			= None
	jPass			= None
	jData			= None

	def __init__(self, jUser, jPass, jDomain, jDebug=True):
		""" Initializes the Jabber Protocol for jUser"""
		
		self.jUser		= jUser
		self.jPass		= jPass
		self.jDomain	= jDomain
		self.jDebug		= jDebug
		self.jId		= xmpp.protocol.JID(jUser)
		self.jClient	= xmpp.Client(jDomain)

	def Connect(self):
		""" Initialzes to Jabber connection"""

		self.jJabberErrors	= JabberErrors.JabberErrors()
		self.jCon		= self.jClient.connect()

		if not self.jCon:
			if self.jDebug is True:
				print 'Connect Error: Code', self.jJabberErrors.getConnectionError()
			return self.jJabberErrors.getConnectionError()

		self.jAuth	= self.jClient.auth(self.jId.getNode(), self.jPass, resource=self.jId.getResource(), sasl=0)

		if not self.jAuth:
			if self.jDebug is True:
				print 'Auth Error: Code', self.jJabberErrors.getAuthError()
			return self.jJabberErrors.getAuthError()

		return self.jJabberErrors.getSuccessCode()

	def Present(self):
		self.jClient.sendInitPresence(requestRoster=0)

	def FetchData(self, dataType):
		roster		= self.jClient.getRoster()
		rosterItems	= roster.getItems()

		return rosterItems


	def DisConnect(self):
		""" Disconnect from Jabber connection"""

		self.jClient.disconnect()
		self.jClient	= None
