import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os
import datetime

# Fetch the service account key JSON file contents
cred = credentials.Certificate(os.getcwd()+'\Bangkit-capfits-firebase-adminsdk-ir8od-6b9ecbadba.json')

# Initialize the app with a service account, granting admin privileges
# https://console.firebase.google.com/project/bangkit-capfits/storage/bangkit-capfits.appspot.com/files
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'bangkit-capfits.appspot.com',
}, name='storage')

bucket = storage.bucket(app=app)
blob = bucket.blob("Allbaseimage/1.jpg")

print(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))