# Face Detection and Recognition System

This project implements a real-time face detection and recognition system using `MTCNN` for face detection and `face_recognition` library for face recognition. The system captures video from the webcam, detects faces, and recognizes known faces by comparing them with a set of pre-stored face images.

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [Future Improvements](#future-improvements)

## Installation

### Prerequisites

Make sure you have Python 3.x installed. You will also need the following libraries:

1. `opencv-python`
2. `mtcnn`
3. `face_recognition`
4. `numpy`

Install the required libraries using the following commands:

```bash
pip install opencv-python mtcnn face_recognition numpy
```

### Additional Requirements

- **Known Faces Directory**: You need a directory structure that contains subdirectories of known people, where each subdirectory is the name of the person, and inside each subdirectory are images of that person.

For example:

```
|-- known_faces
    |-- person1
        |-- image1.jpg
        |-- image2.jpg
    |-- person2
        |-- image1.jpg
        |-- image2.jpg
```

## How it Works

### Loading Known Faces
The `load_known_faces` function reads face images from the `known_faces` directory, encodes them using `face_recognition`, and stores their encodings along with the names of the persons.

### Face Detection
MTCNN is used to detect faces from the webcam feed. It outputs bounding boxes for faces.

### Face Recognition
After detecting faces, the system extracts the face region, encodes it, and compares the encoding with the pre-loaded known face encodings to determine if the face matches any known person.

### Drawing on the Frame
For each detected face, a bounding box is drawn, and the name of the recognized person is displayed above the box. If the person is unknown, it will display "Unknown".

## Usage

1. Place images of known individuals in the `known_faces` directory as described in the [dataset section](#dataset).
2. Run the following command to start the face recognition system:

```bash
python face_recognition_system.py
```

The webcam feed will open, and the system will start detecting and recognizing faces in real-time. Press `q` to quit the program.

### Example of the system in action:

- If the face of a known person (e.g., "John") is detected, the system will display a green rectangle around the face with the label "John".
- For unknown faces, it will display "Unknown".

## Future Improvements

- **Performance Optimization**: Improve frame processing speed to handle more faces in real-time with less latency.
- **Multiple Recognitions**: Add support for recognizing multiple faces at the same time more accurately.
- **Face Database Management**: Create a user-friendly interface to add new known faces and manage the face dataset.
- **Face Embedding Storage**: Store face embeddings in a database to avoid re-encoding faces every time the system starts.
- **Face Mask Detection**: Integrate mask detection during recognition to improve accuracy in pandemic settings.
  
