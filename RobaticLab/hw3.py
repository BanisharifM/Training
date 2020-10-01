import cv2 as cv
import numpy as np
from queue import Queue
from threading import Thread


lo = np.array([255, 255, 255])
up = np.array([0, 0, 0])


def mouse_f(event, x, y, f, g):
    global hsv, lo, up
    if event == cv.EVENT_LBUTTONDOWN:
        print(hsv[y][x])
        for i in range(3):
            lo[i] = min(lo[i], hsv[y][x][i])
            up[i] = max(up[i], hsv[y][x][i])


class FileVideoStream:
    def __init__(self, path, queueSize=128):
        self.stream = cv.VideoCapture(0)
        if self.stream.isOpened():
            print('opened successfully!')
        self.stopped = False
        self.Q = Queue(maxsize=queueSize)

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            if not self.Q.full():
                grabbed, fr = self.stream.read()
                self.Q.put(fr)

    def read(self):
        return self.Q.get()

    def stop(self):
        self.stopped = True
        self.stream.release()


video = FileVideoStream(0).start()
cv.namedWindow('main')
cv.namedWindow('res')
cv.namedWindow('tmp')
cv.setMouseCallback('main', mouse_f)
li = []
while True:
    frame = video.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    res = cv.inRange(hsv, lo, up)
    cv.imshow('main', frame)
    coll = cv.bitwise_and(frame, frame, mask=res)
    cv.imshow('res', coll)
    contours, hierarchy = cv.findContours(res, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        if 1000 < cv.contourArea(cnt) < 100000:
            x, y, w, h = cv.boundingRect(cnt)
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center = (x + w // 2, y + h // 2)
            print('Center:', center[0], center[1])
            li.append(center)
    for c in range(1, len(li)):
        cv.line(frame, li[c-1], li[c], (0, 0, 255), thickness=4)
    cv.imshow('tmp', frame)
    k = cv.waitKey(1)
    if k == ord('q'):  # press q for quit
        break
video.stop()
cv.destroyAllWindows()
