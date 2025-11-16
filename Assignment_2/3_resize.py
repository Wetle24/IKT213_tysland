import cv2
import numpy as np
import os

def resize(image, height, width):
    img = cv2.imread(image)
    
    resized_img = cv2.resize(img, (height, width))

    oheight, owidth, ochannel = img.shape
    nheight, nwidth, nchannel = resized_img.shape

    print(f"Old size: \nHeight: {oheight}, Wdith: {owidth}")
    print(f"New size: \nHeight: {nheight}, Width: {nwidth}")

    cv2.imshow("Lena cropped", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_resized.png"
    cv2.imwrite(image_output_path, resized_img)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"
    resize(image_path, 200, 200)
    return 0

main()