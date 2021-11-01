import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'projectId': "mukhamapp",
})

db = firestore.client()


def schoolWise(school='SCOPE'):
    docs = db.collection("Users").where('school', '==', school).stream()
    for doc in docs:
        print(doc.id)
# schoolWise('SCOPE')


def individualView():
    docs = db.collection("Users").stream()
    for doc in docs:
        userId = doc.id


individualView()
