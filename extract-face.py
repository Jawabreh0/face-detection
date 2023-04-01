from mtcnn import MTCNN
import cv2

# initialize the MTCNN detector
detector = MTCNN()

# load the input image and convert it to grayscale
image = cv2.imread('/home/jawabreh/Desktop/mtcnn/test.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect the face using MTCNN
faces = detector.detect_faces(image)

# extract the face from the image
for face in faces:
    x, y, w, h = face['box']
    extracted_face = image[y:y+h, x:x+w]

# save the extracted face to the output directory
cv2.imwrite('/home/jawabreh/Desktop/mtcnn/extracted_face.jpg', extracted_face)
