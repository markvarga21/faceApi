import numpy as np
import cv2

def convert_filestorage_to_cv2_image(filestorage):
    file_contents = filestorage.read()
    nparr = np.fromstring(file_contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    return image