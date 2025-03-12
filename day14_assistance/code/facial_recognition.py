import cv2
import face_recognition as fr

PATH = "/home/jorgerxbio/Repositories/programming/python-courses/python-total-programador-avanzado-en-16-dias/day14_assistance/data/"

# load images
control_photo = fr.load_image_file(PATH + "FotoA.jpg")
test_photo = fr.load_image_file(PATH + "FotoB.jpg")

# Prepare photos to RGB
control_photo = cv2.cvtColor(control_photo, cv2.COLOR_BGR2RGB)
test_photo = cv2.cvtColor(test_photo, cv2.COLOR_BGR2RGB)

# localize control face
place_face_A = fr.face_locations(control_photo)[0]
coded_face_A = fr.face_encodings(control_photo)[0]

# localize control face
place_face_B = fr.face_locations(test_photo)[0]
coded_face_B = fr.face_encodings(test_photo)[0]

# display rectangle
cv2.rectangle(
    control_photo,
    (place_face_A[3], place_face_A[0]),
    (place_face_A[1], place_face_A[2]),
    (0, 255, 0),
    2,
)

cv2.rectangle(
    test_photo,
    (place_face_B[3], place_face_B[0]),
    (place_face_B[1], place_face_B[2]),
    (0, 255, 0),
    2,
)

# make comparison
result = fr.compare_faces([coded_face_A], coded_face_B)

# measurement of distance
distance = fr.face_distance([coded_face_A], coded_face_B)

# display result
cv2.putText(
    test_photo,
    f"{result} {distance.round(2)}",
    (50, 50),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0, 255, 0),
    2,
)

# display images
cv2.imshow("Control Photo", control_photo)
cv2.imshow("Test Photo", test_photo)

# keep the program open
cv2.waitKey(0)
