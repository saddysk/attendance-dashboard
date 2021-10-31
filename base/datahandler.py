
import firebase_admin
# from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'projectId': "mukhamapp",
})

db = firestore.client()


def getUserDetails(userId):
    ref = db.collection("Users").document(userId)

    doc = ref.get()
    if doc.exists:
        data = doc.to_dict()
        userDetails = {
            'email': data['email'],
            'fullName': data['fullName'],
            'school': data['school'],
        }

        return userDetails
    else:
        return None


def getAttendance(userId):
    ref = db.collection("Attendance").document(userId)

    doc = ref.get()
    if doc.exists:
        data = doc.to_dict()
        print(data)
    else:
        return None
