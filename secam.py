# Mac: import cv2 for camera and pygame for alert sound
# Windows: import cv2 for camera and winsound for alert sound

import cv2
import pygame

# set alert sound effect for the secam

pygame.init()
pygame.mixer.init()
beep_sound = pygame.mixer.Sound("mixkit-industry-alarm-tone-2979.wav")

# code for the secam using open cv

camera = cv2.VideoCapture(0)
img = 0

while camera.isOpened():
    return_val, frame1 = camera.read()
    return_val, frame2 = camera.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(threshold, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:

        # start alert sound when contourArea is larger than 8500
        if cv2.contourArea(c) < 8500:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        beep_sound.play()

        # capture images of the thief
        return_val, image = camera.read()
        cv2.imwrite('catch' + str(img + 1) + '.png', image)
        img += 1
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('My Secam', frame1)