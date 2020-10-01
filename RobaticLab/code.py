import cv2 as cv
import numpy as np
import threading

lower = np.array([250,250,250])
upper = np.array([0,0,0])

def mouse_function(event,x,y,flags,param):
    global hsv, is_clicked, lower, upper
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

cv.namedWindow('select')
cv.namedWindow('Result')
cv.setMouseCallback('select', mouse_function)

while True:
    frame = cv.imread('cnt.jpg')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    result = cv.inRange(hsv, lower, upper)
    cv.imshow('select', frame)
    final = cv.bitwise_and(frame, frame, mask=result)
    cv.imshow('Result', final)
    k = cv.waitKey(1)
    if k == ord('n'):    
        break

cv.namedWindow('Original', cv.WINDOW_AUTOSIZE)
cv.namedWindow('Threshold', cv.WINDOW_AUTOSIZE)
cv.namedWindow('Contours', cv.WINDOW_AUTOSIZE)

img = final
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, tresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY_INV)
contours, hierarchy = cv.findContours(tresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

def thread_1():
    cv.imshow('Original', frame)
    cv.imshow('Threshold', tresh)

def thread_2():
    cv.drawContours(img, contours, -1, (0, 0, 0), thickness=2)
    cv.imshow('Contours', frame)

cv.waitKey(0)

for idx, cnt in enumerate(contours):
    if idx != 0:
        x, y, w, h = cv.boundingRect(cnt)
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = (x + w // 2, y + h // 2)
        print('Area:{} Center: ({}, {})'.format(cv.contourArea(cnt), center[0], center[1]))
        cv.circle(img, center, 5, (255, 0, 0), -1)
        cv.imshow('Contours', img)
        cv.waitKey(0)