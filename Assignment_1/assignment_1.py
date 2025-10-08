import numpy as np
import cv2

def print_image_information(image):
    #function code here
    img = cv2.imread("lena-1.png",1)

    height, width, channel = img.shape
    print('height ', height)
    print('width ', width)
    print('channel ', channel)
    return

def main():
    #all code here
    print("Hello World")
    print_image_information("lena-1.png")
    return 0

main()