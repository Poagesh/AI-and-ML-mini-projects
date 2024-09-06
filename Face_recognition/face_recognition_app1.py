import os
import cv2
from mtcnn.mtcnn import MTCNN
import face_recognition
import numpy as np

def load_known_faces(known_faces_dir):
    known_face_encodings = []
    known_face_names = []

    for person_name in os.listdir(known_faces_dir):
        person_dir = os.path.join(known_faces_dir, person_name)
        
        if not os.path.isdir(person_dir):
            continue

        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                face_encoding = face_encodings[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(person_name)

    return known_face_encodings, known_face_names

def detect_and_recognize_faces(frame, detector, known_face_encodings, known_face_names):
    rgb_frame = frame[:, :, ::-1]
    
    faces = detector.detect_faces(rgb_frame)

    face_locations = []
    for face in faces:
        x, y, width, height = face['box']
        face_locations.append((y, x + width, y + height, x))

    face_encodings = []
    for (y, x1, y1, x0) in face_locations:
        face_image = rgb_frame[y:y1, x0:x1]
        face_encoding = face_recognition.face_encodings(face_image)

        if face_encoding:
            face_encodings.append(face_encoding[0])
        else:
            face_encodings.append(None)

    face_names = []
    for face_encoding in face_encodings:
        if face_encoding is None:
            face_names.append("Unknown")
            continue

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    return face_locations, face_names

def main():
    detector = MTCNN()

    known_faces_dir = 'known_faces'
    known_face_encodings, known_face_names = load_known_faces(known_faces_dir)

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        face_locations, face_names = detect_and_recognize_faces(frame, detector, known_face_encodings, known_face_names)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
