import cv2
import numpy as np
import os

def crop(image, x_0, x_1, y_0, y_1):
    img = cv2.imread(image)
    
    height, width, channel = img.shape
    cropped_img = img[y_0:height-y_1, x_0:width-x_1]

    cv2.imshow("Lena cropped", cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_cropped.png"
    cv2.imwrite(image_output_path, cropped_img)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"
    crop(image_path, 80, 130, 80, 130)
    return 0

main()