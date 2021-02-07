import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
load_dotenv()


def init_db():
    app_credentials = credentials.Certificate(os.getenv("ACCOUNT"))
    firebase_admin.initialize_app(app_credentials)
    db = firestore.client()
    return db
