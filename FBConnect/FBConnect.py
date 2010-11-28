import FBUser
import FBDBConnect

access_token    = '154808361231346|2.rtqNG_HiVeYiFOjUbpfR7w__.3600.1290906000-508175635|tRcJucvzAfnKJjNLC510I2kUv44'
db_filename     = 'C:/Stuffs/My Documents/My Dropbox/Workspace/pyDCHub/db/db.sqlite'

user    = FBUser.FBUser(access_token)
print user.fetchFriends()
print user.fetchEMail()

db_conn = FBDBConnect.FBDBConnect(db_filename)
db_conn.FBDBQuery(str(user.fetchUid()))
db_conn.FBDBClose()