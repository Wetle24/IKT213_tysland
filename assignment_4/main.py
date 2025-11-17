import cv2
import numpy as np

def harris_corner_detection(reference_image):
    gray_image = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    gray_image = np.float32(gray_image)

    dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)

    dst = cv2.dilate(dst, None)

    reference_image[dst > 0.01 * dst.max()] = [0, 0, 255]

    return reference_image


def sift_feature_matching(reference_image,image_to_align, max_features, good_match_percent):
    gray_image1 = cv2.cvtColor(image_to_align, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create(max_features)
    keypoints1, descriptors1 = sift.detectAndCompute(gray_image1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray_image2, None)

    FLANN_INDEX_KDTREE = 1
    indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    searchParams = dict(checks=50)

    flann = cv2.FlannBasedMatcher(indexParams, searchParams)

    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good = []
    for m, n in matches:
        if m.distance < good_match_percent * n.distance:
            good.append(m)

    sorted_good = sorted(good, key=lambda x: x.distance)[:max_features]
    draw_parameters = dict(matchColor=(0, 255, 0), singlePointColor=None, flags=2, matchesThickness=10)
    matched_image = cv2.drawMatches(image_to_align, keypoints1, reference_image, keypoints2, sorted_good, None,
                                    **draw_parameters)
    
    matched_keypoints1 = [keypoints1[m.queryIdx] for m in sorted_good]
    reference_match = cv2.drawKeypoints(reference_image, matched_keypoints1, None, color=(0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    matched_keypoints2 = [keypoints2[m.trainIdx] for m in sorted_good]
    image_to_align_matches = cv2.drawKeypoints(image_to_align, matched_keypoints2, None, color=(0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite('assignment_4/solutions/reference_SIFT.png', reference_match)
    cv2.imwrite('assignment_4/solutions/align_SIFT.png', image_to_align_matches)
    cv2.imwrite('assignment_4/solutions/matched_SIFT.png', matched_image)
    return matched_image

def main():

    image_output_path = "assignment_4/solutions"

    reference_path = "assignment_4/reference_img.png"
    reference_image = cv2.imread(reference_path)

    harris_corners = harris_corner_detection(reference_image)
    cv2.imshow("Harris Corner Detection", harris_corners)
    cv2.imwrite(f'{image_output_path}/harris.png', harris_corners)
    cv2.waitKey(0)


    align_path = "assignment_4/align_this.jpg"
    image_to_align = cv2.imread(align_path)

    aligned_image = sift_feature_matching(image_to_align, harris_corners, 10, 0.7)
    cv2.imshow("Aligned Image", aligned_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()




if __name__ == "__main__":
    default_path = 'assignment_2/images'
    main()