import os
import ConfigParser
from sqlite3 import dbapi2

FIREFOXPATH = os.environ['HOME']+'/.mozilla/firefox'
INIPROFILEPATH = os.path.join(FIREFOXPATH, 'profiles.ini')

print FIREFOXPATH
print INIPROFILEPATH
if not os.path.exists(FIREFOXPATH) or  not os.path.exists(INIPROFILEPATH):
    raise Exception, "Firefox path does not exist"

def getProfiles():
    parser = ConfigParser.ConfigParser()
    parser.read(INIPROFILEPATH)
    index = 0
    profiles = []
   
    try:
        while 1:
            path = parser.get('Profile%d' % index, 'Path')
            name = parser.get('Profile%d' % index, 'Name')
            
            path = os.path.join(FIREFOXPATH, path)
            
            index+=1
            
            profiles.append([path,name])
           
    except ConfigParser.NoSectionError, err:
        print err
    
    finally:
        return profiles

        
class Profile:
    def __init__(self, path, name):
        self.path = path
        self.name = name
       
        self.refresh()

    def _Extract(self, container, instance, filename, sql_query):
       
        path = os.path.join(self.path, filename)
        print path
       
        conn = dbapi2.connect(path)
        cur = conn.cursor()
        cur.execute(sql_query)

        for row in cur.fetchall():
            container.append(instance(row))
           
        conn.close()

    def _ExtractCookies(self):
        self._cookies = []

        self._Extract(self._cookies, Cookie, 'cookies.sqlite', "SELECT host, name, value From moz_cookies")

    def refresh(self):
        self._ExtractCookies()

    def getCookieByHostName(self, name):
        cookies = []
        for cookie in self._cookies:
            if name in cookie.host:
                cookies.append(cookie)
        return cookies

    def getCookieLength(self):
        return self._cookies.__len__()

    def getCookieObject(self, index):
        return self._cookies[index]

    def getDownloadObject(self, index):
        return self._downloads[index]

    def getDownloadHistoryLength(self):
        return self._downloads.__len__()

    def getFormHistoryObject(self, index):
        return self._formhistory[index]

    def getFormHistoryLength(self):
        return self._formhistory.__len__()
       

class Cookie:
   
    def __init__(self, tup):
        self.host, self.name, self.value = tup
