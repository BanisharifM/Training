import cv2 as cv
import numpy as np


def mouse_function(event, x, y, flag, param):
    global frame, lower, upper
    if event == cv.EVENT_LBUTTONDOWN:
        if hsv[y][x][0] < lower[0]:
            lower[0] = hsv[y][x][0]
        if hsv[y][x][0] > upper[0]:
            upper[0] = hsv[y][x][0]

        if hsv[y][x][1] < lower[1]:
            lower[1] = hsv[y][x][1]
        if hsv[y][x][1] > upper[1]:
            upper[1] = hsv[y][x][1]

        if hsv[y][x][2] < lower[2]:
            lower[2] = hsv[y][x][2]
        if hsv[y][x][2] > upper[2]:
            upper[2] = hsv[y][x][2]
        print(lower)


lower = np.array([255, 255, 255])
upper = np.array([0, 0, 0])

lower1 = np.array([0, 13, 107])
upper1 = np.array([47, 92, 206])

cap = cv.VideoCapture('video1.mp4')

cv.namedWindow('Video')
cv.namedWindow('Result')
cv.setMouseCallback('Video', mouse_function)
if cap.isOpened():
    print('camera is opened')
while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    result = cv.inRange(hsv, lower, upper)
    cv.imshow('Video', frame)
    final = cv.bitwise_and(frame, frame, mask=result)
    cv.imshow('Result', final)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
