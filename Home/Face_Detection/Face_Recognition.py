import face_recognition
import os
import sys
sys.path.append('D:\Programing By Monu Kumar\Django Projects\FaceAttendence\Home\Face_Detection')
import cv2
import numpy as np
from Home.models import EmployeeDetails

class Face_Recog():
    extra_path='Home/Face_Detection/'

    def load_data(self):
        known_face_encodings = []
        known_face_names = []

        for record in EmployeeDetails.objects.values('Emp_id','Name', 'img'):
            img_path = record['img']
            emp_id = record['Emp_id']
            name = record['Name']
            img = face_recognition.load_image_file(img_path)
            img_encoding = face_recognition.face_encodings(img)
            if img_encoding:
                known_face_encodings.append(img_encoding[0])
                known_face_names.append(str(emp_id)+ '  '+name)    

        if len(known_face_encodings) == len(known_face_names):
            return np.array(known_face_encodings), known_face_names
        else:
            raise ValueError("Mismatch between face encodings and names")

    def Face_Verification(self, frame, known_face_encodings, known_face_names):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
        
        return face_locations, face_names

    def display(self, frame, face_locations, face_names):
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    def Face_detection_with_name(self, frame, known_face_encodings, known_face_names, process_this_frame):
        face_locations, face_names = [], []
        if process_this_frame:
            face_locations, face_names = self.Face_Verification(frame, known_face_encodings, known_face_names)

        process_this_frame = not process_this_frame
        self.display(frame, face_locations, face_names)
        
        if face_names ==[] or face_names == ['Unknown']:
            return face_names
        else:
            return  int((face_names[0])[:2])
    
