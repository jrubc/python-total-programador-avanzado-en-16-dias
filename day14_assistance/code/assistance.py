import os
from datetime import datetime

import cv2
import face_recognition as fr
import numpy

DATA_PATH = "/home/jorgerxbio/Repositories/programming/python-courses/python-total-programador-avanzado-en-16-dias/day14_assistance/data/"

# create data base
path = "Empleados"
my_images = []
employee_names = []
employee_list = os.listdir(path)

for name in employee_list:
    currently_image = cv2.imread(f"{path}/{name}")
    my_images.append(currently_image)
    employee_names.append(os.path.splitext(name)[0])

print(employee_names)


def encode(images):
    # create a new list
    coded_list = []

    # pass each image
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # encode
        coded = fr.face_encodings(image)[0]

        # add to list
        coded_list.append(coded)

    # return coded list
    return coded_list


def admitted_register(person):
    f = open(DATA_PATH + "registro.csv", "r+")
    data_list = f.readlines()
    register_names = []
    for line in data_list:
        admitted = line.split(",")
        register_names.append(admitted[0])

    if person not in register_names:
        now = datetime.now()
        now_string = now.strftime("%H:%M:%S")
        f.writelines(f"\n{person}, {now_string}")


coded_employee_list = encode(my_images)

# take a photo using a web cam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# read image of the cam
success, image = capture.read()
if not success:
    print("It was not possible to take a capture")
else:
    # recognize face in capture
    capture_face = fr.face_locations(image)

    # encode captured face
    encoded_capture_face = fr.face_encodings(image, capture_face)

    # search for matches
    for codif_face, local_cara in zip(encoded_capture_face, capture_face):
        match = fr.compare_faces(coded_employee_list, codif_face)
        distances = fr.face_distance(coded_employee_list, codif_face)

        print(distances)
        match_index = numpy.argmin(distances)

        # display matches (if there are)
        if distances[match_index] > 0.6:
            print("it doesn't match")
        else:
            print("You're welcome :)")
            # search employee name
            name = employee_names[match_index]

            y1, x2, y2, x1 = local_cara
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                image,
                name,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                2,
            )

            admitted_register(name)

            # display image
            cv2.imshow("Web image", image)

            # keep window open
            cv2.waitKey(0)
