from mtcnn import MTCNN
import cv2

# initialize the MTCNN detector
detector = MTCNN()

# initialize the video capture object for the default camera
cap = cv2.VideoCapture(0)

while True:
    # read the frame from the camera
    ret, frame = cap.read()

    # detect faces using MTCNN
    faces = detector.detect_faces(frame)

    # draw bounding boxes around the faces
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # show the resulting frame
    cv2.imshow('Real-time Face Detection', frame)

    # press 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
