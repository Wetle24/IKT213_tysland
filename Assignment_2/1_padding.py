import cv2
import numpy as np
import os

def padding(image, border_width):
    img = cv2.imread(image)
    img_with_border = cv2.copyMakeBorder(img, border_width, border_width, border_width, border_width, cv2.BORDER_REFLECT)
    cv2.imshow("Lena padded", img_with_border)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image_output_path = "assignment_2/solutions/assignment_2_lena_padded.png"
    cv2.imwrite(image_output_path, img_with_border)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"
    padding(image_path, 100)
    return 0

main()