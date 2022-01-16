import pyrebase


# configuration key
firebaseConfig = {
  'apiKey': "AIzaSyBCs37bq0qIIgyRC77AOBMKlwZdR6eqFNI",
  'authDomain': "triperadvise.firebaseapp.com",
  'projectId': "triperadvise",
  'storageBucket': "triperadvise.appspot.com",
  'messagingSenderId': "415829560302",
  'appId': "1:415829560302:web:27d2770750748f92875cff",
  'measurementId': "G-8SG87YPDT1",
  'databaseURL': "https://triperadvise-default-rtdb.europe-west1.firebasedatabase.app/"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Databases
db = firebase.database()
storage = firebase.storage()

