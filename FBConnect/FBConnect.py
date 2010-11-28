import FBUser
import FBDBConnect

access_token    = '154808361231346|2.KV6Q5xwebmuwmsWZdIC7zw__.3600.1290909600-508175635|zDTFW9uqmB4AlkhXFg-ktFzMpT0'
db_filename     = 'C:/Stuffs/www/db.sqlite'#'C:/Stuffs/My Documents/My Dropbox/Workspace/pyDCHub/db/db.sqlite'

user    = FBUser.FBUser(access_token)
print user.fetchFriends()
print user.fetchEMail()

db_conn = FBDBConnect.FBDBConnect(db_filename)
db_conn.FBDBQuery(str(user.fetchUid()))
db_conn.FBDBClose()