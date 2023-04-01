from mtcnn import MTCNN
import cv2

# initialize the MTCNN detector
detector = MTCNN()

# load the input image and convert it to grayscale
image = cv2.imread('/home/jawabreh/Desktop/mtcnn/test.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect the face using MTCNN
faces = detector.detect_faces(image)

# draw a bounding box around the face
for face in faces:
    x, y, w, h = face['box']
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# save the image with the bounding box to the output directory
cv2.imwrite('/home/jawabreh/Desktop/mtcnn/bounding_box.jpg', image)
