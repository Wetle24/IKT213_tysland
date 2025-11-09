import numpy as np
import cv2
import os

def print_image_information(image):
    img = cv2.imread(image)

    height, width, channel = img.shape
    size = img.size
    data_type = img.dtype
    print('A: height ', height)
    print('B: width ', width)
    print('C: channel ', channel)
    print('D. size ', size)
    print('E. data type ', data_type)
    return

def main():
    print_image_information("assignment_1\lena-1.png")
    return 0

main()