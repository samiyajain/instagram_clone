import firebase_admin
from firebase_admin import credentials, firestore

#initiakize firebase 
cred = credentials.Certificate("firebase_key.json")

if not firebase_admin_apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()