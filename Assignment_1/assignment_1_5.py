import cv2
import os

cam = cv2.VideoCapture(0)

fps = int(cam.get(cv2.CAP_PROP_FPS))
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

#got some errors with the path, so I had to do this instead of just writing in the path in the "open"
output_path = os.path.join("solutions", "camera_outputs.txt")

with open(output_path, "w") as output_file:
    output_file.write(f"A: fps: {fps}\n")
    output_file.write(f"B: height: {frame_height}\n")
    output_file.write(f"C: width: {frame_width}\n")

while True:
    ret, frame = cam.read()

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()