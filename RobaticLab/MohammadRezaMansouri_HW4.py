import cv2 as cv
from queue import Queue
from threading import Thread
import numpy as np


class FileVideoStream:
    def __init__(self, path, queue_size=128):
        self.stream = cv.VideoCapture(path)
        self.stopped = False
        # initialize the queue used to store frames read from
        # the video file
        self.Q = Queue(maxsize=queue_size)

    def start(self):
        # start a thread to read frames from the file video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            if not self.Q.full():
                # read the next frame from the file
                grabbed, fr = self.stream.read()
                self.Q.put(fr)

    def read(self):
        return self.Q.get()

    def stop(self):
        self.stopped = True
        self.stream.release()


video = FileVideoStream(0).start()

lower = np.array([255, 255, 255])
upper = np.array([0, 0, 0])

is_down = False
is_clicked = False

dots = []


def mouse_function(event, x, y, flags, params):
    global hsv, is_clicked
    if event == cv.EVENT_LBUTTONDOWN:
        print(upper)
        print(lower)
        is_clicked = True
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


def draw_dot_thread():
    while True:
        draw_dot()


def draw_dot():
    for i in range(len(dots)):
        if i > 0:
            cv.line(frame, dots[i - 1], dots[i], (255, 0, 0), thickness=5)


# draw_thread = Thread(target=self.update, args=())
# cap = cv.VideoCapture(0)
cv.namedWindow('video')
cv.namedWindow('color')
cv.setMouseCallback('video', mouse_function)

# _thread.start_new_thread(draw_dot_thread, ())

while True:
    frame = video.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    result = cv.inRange(hsv, lower, upper)
    color = cv.bitwise_and(frame, frame, mask=result)

    contours, _h = cv.findContours(result, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv.contourArea(contour)
        if 1000 < area < 100000:
            x, y, w, h = cv.boundingRect(contour)
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
            center = (x + w // 2, y + h // 2)
            dots.append(center)
            draw_dot()

    cv.imshow('video', frame)
    cv.imshow('color', color)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

    k = cv.waitKey(1)
    if k == ord('q'):  # press q for quite
        break

video.stop()
cv.destroyAllWindows()
