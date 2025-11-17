import cv2
import numpy as np
import os

def rotation(image, rotation_angle):
    img = cv2.imread(image)

    if (rotation_angle == 90):
        rotation_code = cv2.ROTATE_90_CLOCKWISE
    elif (rotation_angle == 180):
        rotation_code = cv2.ROTATE_180
    else:
        return 0
    
    rotated_img = cv2.rotate(img, rotation_code)
    
    cv2.imshow("Lena rotated", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_rotated_90.png"
    cv2.imwrite(image_output_path, rotated_img)

    print("Saved image")
    return 0 


def main():
    image_path = "assignment_2\lena-2.png"

    rotation(image_path, 90)
    return 0

main()