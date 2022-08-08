from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
from firebase_admin import db
from firebase_admin import storage as admin_storage

# Initialize
cred = credentials.Certificate("privateAccountKey.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'triperadvise.appspot.com'})

# Iterate through all users. This will still retrieve users in batches,
# buffering no more than 1000 users in memory at a time.
a = []
for user in auth.list_users().iterate_all():
    a.append(user.email)






