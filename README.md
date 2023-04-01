# face-detection
This GitHub repository contains an implementation of a face detection algorithm using MTCNN (Multi-Task Cascaded Convolutional Networks). MTCNN is a state-of-the-art deep learning-based face detection algorithm that is able to accurately detect faces even in challenging environments, such as low light, occlusions, and various angles.

## Content 
* extract-face.py 
This file contains the implementation of face extraction from an image using MTCNN. It takes an input image, detects faces using MTCNN, and saves each detected face as a separate image file, this can be used to extract to train an AI model.

* draw-box.py 
This file contains the implementation of drawing a bounding box around a detected face using MTCNN. It takes an input image, detects faces using MTCNN, and draws a bounding box around each detected face. It then saves the result as a new image file.

* real-time.py
This file contains the implementation of real-time face detection using MTCNN. It captures video from the webcam and detects faces in the frames using the MTCNN algorithm. It then draws a bounding box around the detected face and displays the result on the screen.

## Requirements 
* Python 3.6 or later
* MTCNN
* OpenCV
* NumPy

## Usage
To use the face detection algorithm, you can download the repository and run any of the three Python files. For real-time face detection, run real-time.py. For face extraction, run extract-face.py. For drawing bounding boxes, run draw-box.py.

You can modify the parameters in each file to customize the face detection algorithm, such as the confidence threshold and the minimum face size. Additionally, you can use these files as a starting point to integrate face detection into other computer vision applications.

Contributors are welcome to contribute to the repository by improving the code or adding new features.
