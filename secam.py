import cv2

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame1 = camera.read()
    ret, frame2 = camera.read()
    diff = cv2.absdiff(frame1, frame2)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('My Secam', diff)