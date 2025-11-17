import cv2
import numpy as np
import os

def hue_shifted(image, emptyPictureArray, hue):
    img = cv2.imread(image)

    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.imshow("Lena RGB", rgb_image)
    cv2.waitKey(0)

    r, g, b = cv2.split(rgb_image)


    r_shifted = np.clip(r + hue, 0, 255)
    g_shifted = np.clip(g + hue, 0, 255)
    b_shifted = np.clip(b + hue, 0, 255)

    shifted_image = cv2.merge((r_shifted, g_shifted, b_shifted)).astype(np.uint8)

    height, width, channels = img.shape

    for y in range(height):
        for x in range(width):
            emptyPictureArray[y, x] = shifted_image[y, x]
    
    cv2.imshow("Lena HSV", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image_output_path = "assignment_2/solutions/assignment_2_lena_hue_shifted.png"
    cv2.imwrite(image_output_path, shifted_image)

    print("Saved image")
    return 0


def main():
    image_path = "assignment_2\lena-2.png"

    temp = cv2.imread(image_path)
    height, width, channels = temp.shape
    emptyPictureArray = np.zeros((height, width, channels), dtype=np.uint8)

    hue_shifted(image_path, emptyPictureArray, 50)
    return 0

main()