import cv2
import numpy as np

def sobel_edge_detection(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    sobel = cv2.Sobel(blurred, cv2.CV_64F, 1, 1, ksize=1)
    sobel = cv2.convertScaleAbs(sobel)
    return sobel


def canny_edge_detection(image, threshold_1, threshold_2):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    edges = cv2.Canny(blurred, threshold_1, threshold_2)
    return edges

def template_match(image, template):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    width, height = gray_template.shape[::-1]

    result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where (result >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + width, pt[1] + height), (0, 0, 255), 2)
    return image

def resize(image, scale_factor: int, up_or_down: str):
    height, width, channel = image.shape
    if up_or_down == 'up':
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
    elif up_or_down == 'down':
        new_width = int(width / scale_factor)
        new_height = int(height / scale_factor)
    else:
        raise ValueError("not recognized up or down")
    
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_image



def main():

    image_path = "assignment_3\lambo.png"
    image_output_path = "assignment_3/solutions"

    img = cv2.imread(image_path)

    sobel = sobel_edge_detection(img)

    cv2.imshow("Sobel Edge Detection", sobel)
    cv2.waitKey(0)
    cv2.imwrite(f'{image_output_path}/sobel.png', sobel)

    canny = canny_edge_detection(img, 50, 50)
    cv2.imshow("Canny Edge Detection", canny)
    cv2.imwrite(f'{image_output_path}/canny.png', canny)

    cv2.waitKey(0)

    shape = cv2.imread("assignment_3\shapes.png")
    template = cv2.imread("assignment_3\shapes_template.jpg")

    matched = template_match(shape, template)
    cv2.imshow("Template Matching", matched)
    cv2.imwrite(f'{image_output_path}/matched.png', matched)


    cv2.waitKey(0)

    resized_up = resize(img, 2, 'up')
    cv2.imshow("Resized Up", resized_up)
    cv2.imwrite(f'{image_output_path}/resized_up.png', resized_up)

    cv2.waitKey(0)

    resized_down = resize(img, 2, 'down')
    cv2.imshow("Resized Down", resized_down)
    cv2.imwrite(f'{image_output_path}/resized_down.png', resized_down)

    cv2.waitKey(0)


    cv2.destroyAllWindows()








if __name__ == "__main__":
    default_path = 'assignment_2/images'
    main()