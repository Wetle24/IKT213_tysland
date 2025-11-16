import cv2
import numpy as np
import os

def hsv(image):
    img = cv2.imread(image)

    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    cv2.imshow("Lena HSV", hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_hsv.png"
    cv2.imwrite(image_output_path, hsv_image)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"
    hsv(image_path)
    return 0

main()