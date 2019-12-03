import os

import cv2
import mysql.connector


def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read("trainer/trainer.yml")
classifier_path = "classifier.xml"
faceCascade = cv2.CascadeClassifier(classifier_path)


def get_profile(s_roll):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
        db_cursor = connection.cursor()
        print(str(s_roll))
        db_cursor.execute("SELECT s_name FROM studentdetails WHERE s_roll = " + str(s_roll))
        query_result = db_cursor.fetchone()
        student_profile = None
        for row in query_result:
            student_profile = row
        print(student_profile)
        connection.close()
        return student_profile

    except Exception as e:
        print(e)


video_feed = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
profiles = {}

while True:
    ret, image = video_feed.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_image, 1.2, 5)
    for (x, y, w, h) in faces:
        student_id, confidence = recognizer.predict(gray_image[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(str(student_id))
        profile = get_profile(student_id)
        if profile is not None:
            cv2.putText(image, profile, (x, y + h + 30), font, 1, (0, 0, 255), 3)
            cv2.putText(image, "Accuracy: {0:.2f}%".format(round(100 - confidence, 2)), (x, y + h + 60), font, 1, (0, 0, 255), 3)
    cv2.imshow('Face', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("exit")
        break

video_feed.release()
cv2.destroyAllWindows()