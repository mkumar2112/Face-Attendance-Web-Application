import cv2 as cv
import sys
sys.path.append('D:\Programing By Monu Kumar\Django Projects\FaceAttendence\Home\Face_Detection')
from .Save_Data import Attendence_True
from .Face_Recognition import Face_Recog
import os
import schedule



face_cap = cv.CascadeClassifier('Home\Face_Detection\Data_For_Detection\haarcascade_frontalface_default.xml')
# Save_Info = Save_Person_Info()

# Initialize some variables
process_this_frame = True
Face_Recognition = Face_Recog()


def Attend_True(pid):
    Attendence_True(pid)

def Face_Attend(going_live=False):
    video_capture = cv.VideoCapture(0)
    # video_capture = qqqqqcv.VideoCapture('http://172.16.2.7:4747/video')
    while going_live:
        # schedule.run_pending()
        ret, frame = video_capture.read()
        if ret:
            known_face_encodings, known_face_names = Face_Recognition.load_data()
            Is_person = Face_Recognition.Face_detection_with_name(frame, known_face_encodings, known_face_names, process_this_frame)
            print('------>',Is_person, )
            if Is_person != [] and Is_person != ['Unknown']:
                Attend_True(Is_person)
            # Display the resulting image
            cv.imshow('Video', frame)
            # Hit 'q' on the keyboard to quit!
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Can't receive frame (stream end?). Exiting ...")
            return False

    # Release handle to the webcam
    # video_capture.release()
    cv.destroyAllWindows()

