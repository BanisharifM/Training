import cv2 as cv
from queue import Queue
from threading import Thread


class FileVideoStream:
    def __init__(self, path, queueSize=128):
        self.stream = cv.VideoCapture(path)
        self.stopped = False
        # initialize the queue used to store frames read from
        # the video file
        self.Q = Queue(maxsize=queueSize)

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


thresh = 1
max_value = 1


def update(x):
    global thresh, max_value
    thresh = cv.getTrackbarPos('Thresh', 'Video')
    max_value = cv.getTrackbarPos('Max', 'Video')
    pass


cv.namedWindow('Video', cv.WINDOW_AUTOSIZE)
# create track bars
cv.createTrackbar('Thresh', 'Video', 1, 255, update)
cv.createTrackbar('Max', 'Video', 1, 255, update)

video = FileVideoStream(1).start()

while True:
    start = cv.getTickCount()
    frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, result = cv.threshold(gray, thresh, max_value, cv.THRESH_BINARY)
    cv.imshow('Video', result)

    k = cv.waitKey(1)
    if k == ord('q'):  # press q for quite
        break

    end = cv.getTickCount()
    time = (end - start) / cv.getTickFrequency()
    print(f'FPS: {1 / time}')

video.stop()
cv.destroyAllWindows()