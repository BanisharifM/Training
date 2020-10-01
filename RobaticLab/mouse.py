import cv2 as cv
import numpy as np


def mouse_function(event, x, y, flag, param):
    global x1, x2, y1, y2
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
    elif event == cv.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        color_ranging()


def color_ranging():
    global x1, x2, y1, y2
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    if x1 == x2 and y1 == y2:
        set_rang(x1, y1)
    else:
        for x in range(x1, x2, 2):
            for y in range(y1, y2, 2):
                set_rang(x, y)


def set_rang(x, y):
    set_upper(x, y)
    set_lower(x, y)


def set_upper(x, y):
    global hsv, upper
    if hsv[y][x][0] > upper[0]:
        upper[0] = hsv[y][x][0]

    if hsv[y][x][1] > upper[1]:
        upper[1] = hsv[y][x][1]

    if hsv[y][x][2] > upper[2]:
        upper[2] = hsv[y][x][2]


def set_lower(x, y):
    global hsv, lower
    if hsv[y][x][0] < lower[0]:
        lower[0] = hsv[y][x][0]

    if hsv[y][x][1] < lower[1]:
        lower[1] = hsv[y][x][1]

    if hsv[y][x][2] < lower[2]:
        lower[2] = hsv[y][x][2]


x1 = 0
y1 = 0
x2 = 0
y2 = 0

lower = np.array([255, 255, 255])
upper = np.array([0, 0, 0])

lower1 = np.array([0, 13, 107])
upper1 = np.array([47, 92, 206])

cap = cv.VideoCapture(0)

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
