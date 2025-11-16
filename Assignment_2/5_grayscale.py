import cv2
import numpy as np
import os

def grayscale(image):
    img = cv2.imread(image)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Lena cropped", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_grayscale.png"
    cv2.imwrite(image_output_path, gray_img)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"
    grayscale(image_path)
    return 0

main()