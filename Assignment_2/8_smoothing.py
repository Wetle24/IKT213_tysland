import cv2
import numpy as np
import os

def smoothing(image):
    img = cv2.imread(image)

    averaging = cv2.blur(img, (15,15))
    gaussian = cv2.GaussianBlur(img, (15, 15), cv2.BORDER_DEFAULT)
    median = cv2.medianBlur(img, 15)
    
    cv2.imshow("Lena blur", averaging)
    cv2.waitKey(0)
    cv2.imshow("Lena gaussian", gaussian)
    cv2.waitKey(0)
    cv2.imshow("Lena median", median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    avg_path = "assignment_2/solutions/assignment_2_lena_blurred.png"
    gaussian_path = "assignment_2/solutions/assignment_2_lena_gaussian.png"
    median_path = "assignment_2/solutions/assignment_2_lena_median.png"
    cv2.imwrite(avg_path, averaging)
    cv2.imwrite(gaussian_path, gaussian)
    cv2.imwrite(median_path, median)

    print("Saved images")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"
    smoothing(image_path)
    return 0

main()