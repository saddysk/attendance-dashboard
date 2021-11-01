import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from datetime import datetime, timedelta


cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'projectId': "mukhamapp",
})

db = firestore.client()


# get personal details
def getUserDetails(userId):
    ref = db.collection("Users").document(userId)

    doc = ref.get()
    if doc.exists:
        data = doc.to_dict()
        userDetails = {
            'empId': data['EmpId'],
            'fullName': data['fullName'],
            'school': data['school'],
        }
        return userDetails
    else:
        return None


# get attendance
def getAttendance(userId, fromDate=datetime.today().replace(day=1), toDate=datetime.today()):
    ref = db.collection("Attendance").document(userId)

    doc = ref.get()
    if doc.exists:
        data = doc.to_dict()
    else:
        return None

    attendance = []
    totalPositiveCount = 0
    totalNegativeCount = 0

    delta = timedelta(days=1)
    while fromDate <= toDate:
        stringDate = fromDate.strftime('%d-%m-%Y')
        tempDict = {
            'date': stringDate,
            'morningStatus': 0,
            'eveningStatus': 0
        }
        fromDate += delta
        try:
            attendanceForEachDay = data[stringDate]
            if attendanceForEachDay[0] is not False:
                tempDict['morningStatus'] = 1
            if attendanceForEachDay[1] is not False:
                tempDict['eveningStatus'] = 1
        except:
            pass

        if tempDict['morningStatus'] == 1 and tempDict['eveningStatus'] == 1:
            totalPositiveCount += 1
        else:
            totalNegativeCount += 1

        attendance.insert(0, tempDict)

    positivePercent = totalPositiveCount / \
        (totalPositiveCount + totalNegativeCount) * 100
    negativePercent = totalNegativeCount / \
        (totalPositiveCount + totalNegativeCount) * 100
    attendanceDetails = {
        'attendance': attendance,
        'positivePercent': float("{:.2f}".format(positivePercent)),
        'negativePercent': float("{:.2f}".format(negativePercent)),
    }
    return attendanceDetails


# get individual attendance
def getIndividualAttendance(fromDate, toDate):
    docs = db.collection("Users").stream()

    individualAttendance = []
    for doc in docs:
        userId = doc.id
        userDetail = getUserDetails(userId)
        userAttendance = getAttendance(userId, fromDate, toDate)

        attendance = {
            'school': userDetail['school'],
            'fullName': userDetail['fullName'],
            'totalPresent': userAttendance['positivePercent'],
            'totalAbsent': userAttendance['negativePercent'],
        }
        individualAttendance.insert(0, attendance)
    return individualAttendance


# get school wise attendance
"""
def getAttendanceSchoolWise(school, fromDate, toDate):
    # get users belong to the given school
    docs = db.collection("Users").where('school', '==', school).stream()

    for doc in docs:
        userId = doc.id

        print('\n\n*************', None, '\n\n*************')
"""
