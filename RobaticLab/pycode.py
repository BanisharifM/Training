import cv2 as cv
import numpy as np
import threading
import statistics

lower = np.array([250,250,250])
upper = np.array([0,0,0])
points = []


def mouse_function(event, x, y, flags,param):
    global hsv, lower, upper
    if event == cv.EVENT_LBUTTONDOWN:
        if hsv[y][x][0] < lower[0]:
            lower[0] = hsv[y][x][0]
        elif hsv[y][x][0] > upper[0]:
            upper[0] = hsv[y][x][0]

        if hsv[y][x][1] < lower[1]:
            lower[1] = hsv[y][x][1]
        elif hsv[y][x][1] > upper[1]:
            upper[1] = hsv[y][x][1]

        if hsv[y][x][2] < lower[2]:
            lower[2] = hsv[y][x][2]
        elif hsv[y][x][2] > upper[2]:
            upper[2] = hsv[y][x][2]


cap = cv.VideoCapture(1)

cv.namedWindow('Video')
cv.namedWindow('Result')
cv.namedWindow('Contours', cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('Video', mouse_function)

if cap.isOpened():

    while True:
        _, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        result = cv.inRange(hsv, lower, upper)
        cv.imshow('Video', frame)
        final = cv.bitwise_and(frame, frame, mask=result)
        cv.imshow('Result', final)

        img = final
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        _, tresh = cv.threshold(gray, 30, 255, cv.THRESH_BINARY_INV)
        contours, hierarchy = cv.findContours(tresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for idx, cnt in enumerate(contours):
            if idx != 0:
                x, y, w, h = cv.boundingRect(cnt)
                center = (x + w // 2, y + h // 2)
                print('Area:{} Center: ({}, {})'.format(cv.contourArea(cnt), center[0], center[1]))
                cv.circle(img, center, 5, (255, 0, 0), -1)
                img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                points.append(center)
                for idx, cnt in enumerate(points):
                    if idx != len(points) - 1:
                        img = cv.line(img, points[idx], points[idx + 1], (0, 0, 255), 1)
                cv.imshow('Contours', img)

        k = cv.waitKey(1)
        if k == ord('q'):
            break

cap.release()