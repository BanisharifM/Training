import cv2 as cv


def mouse_callback(event, x, y, flags, param):
    global x1, x2, y1, y2
    if event == cv.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
    elif event == cv.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        if x1 != x2 and y1 != y2:
            crop_image()


def crop_image():
    global i, x1, x2, y1, y2
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    cropped_img = frame[y1:y2, x1:x2]
    cv.namedWindow('cropped', cv.WINDOW_FULLSCREEN)
    cv.imshow("cropped", cropped_img)  # display croped_image in cropped window
    key = ord('a')
    while key != ord('e'):  # exit from crop window
        key = cv.waitKey(1)
        if key == ord('s'):  # save croped image
            cv.imwrite('croped' + str(i) + '.jpg', cropped_img)
            i += 1
    cv.destroyWindow('cropped')


cap = cv.VideoCapture('video.mp4')
if cap.isOpened():
    print("video is open!!! ")
else:
    exit()

i = 0
cv.namedWindow('video', cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('video', mouse_callback)
x1 = 0
y1 = 0
x2 = 0
y2 = 0

while True:
    ret, frame = cap.read()
    if ret is not True:
        break

    cv.imshow('video', frame)

    key = cv.waitKey(1)
    if key == ord('q'):  # quit
        break
    elif key == ord('p'):  # puse
        while key != ord('c'):  # continue
            key = cv.waitKey(1)

cap.release()
cv.destroyAllWindows()
