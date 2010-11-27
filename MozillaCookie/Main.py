'''
Created on Nov 24, 2010

@author: Naresh
'''

import MozillaCookie

print 'Hi'

for profile in MozillaCookie.getProfiles():
    userProfile = MozillaCookie.Profile(profile[0], profile[1])
    print "Reading information from %s Profile" % userProfile.name
    for cookieIndex in xrange(userProfile.getCookieLength()):
        cookie = userProfile.getCookieObject(cookieIndex)
        print "Host: %s\nName: %s\nValue: %s\n\n" % (cookie.host, cookie.name, cookie.value)
