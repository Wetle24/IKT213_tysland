import face_recognition
import cv2
img = cv2.imread("assignment_5/known_people/John_Cena.jpg")
rgb = img[:, :, ::-1]
locations = face_recognition.face_locations(rgb)
encodings = face_recognition.face_encodings(rgb, locations)
print(encodings)