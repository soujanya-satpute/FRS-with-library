import cv2
from simple_facerec import SimpleFacerec
import serial
port = serial.Serial('/dev/cu.usbserial-1420',9600)

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    print(face_locations)
    print(face_names)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        if(face_names[0] == 'soujanya'):
            port.write(str.encode('1'))
            print("sent 1")
        elif(face_names[0] == 'Kaustubh'):
            port.write(str.encode('1'))
            print("sent 1")
        elif(face_names[0] == 'Amrit'):
            port.write(str.encode('1'))
            print("sent 1")
        elif (face_names[0] == 'Unknown'):
            port.write(str.encode('0'))
            print("sent 0")
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)
    


    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()