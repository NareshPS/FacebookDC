from sqlite3 import dbapi2
import sys
import os

class FBDBConnect:
    db_filename     = None
    db_conn         = None
    db_prepStmnt    = 'SELECT * from records where uid=%s'

    
    def __init__(self, filename):
        
        self.db_filename    = filename
        print self.db_filename
        
        if len(self.db_filename) > 0:
            try:        
                self.db_conn    = dbapi2.connect(self.db_filename)
            except:
                print sys.exc_info()
                print 'Exception Occured'
        else:
            print 'Invalid File Name'
        
            
    def FBDBQuery(self, uid):     
        dict    = None
        if self.db_conn is not None:
            try:
                cur     = self.db_conn.cursor()
                query   = (self.db_prepStmnt)%uid
                cur.execute(query)
                for row in cur.fetchall():
                    print row
                
            except:
                print sys.exc_info()
                print 'Exception Occured'
        else:
            print 'Connection not open'
            
    def FBDBClose(self):
        if self.db_conn is not None:
            self.db_conn.close()