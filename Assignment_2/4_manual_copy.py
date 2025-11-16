import cv2
import numpy as np
import os

def copy(image, emptyPictureArray):
    img = cv2.imread(image)
    
    height, width, channels = img.shape

    for y in range(height):
        for x in range(width):
            emptyPictureArray[y, x] = img[y, x]

    cv2.imshow("Copied Picture", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_copied.png"
    cv2.imwrite(image_output_path, emptyPictureArray)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"

    temp = cv2.imread(image_path)
    height, width, channels = temp.shape
    emptyPictureArray = np.zeros((height, width, channels), dtype=np.uint8)

    copy(image_path, emptyPictureArray)
    return 0

main()