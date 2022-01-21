import cv2 as cv


def resize_frame(img, scale):
    return cv.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)), interpolation=cv.INTER_AREA)


cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    height, width, channels = img.shape
    sample = img[0: height // 2, 0: width // 2]
    cv.line(sample, (0, 0), (sample.shape[1], sample.shape[0]), (0, 0, 255), 5)
    cv.line(sample, (sample.shape[1], 0), (0, sample.shape[0]), (0, 0, 255), 5)
    img[0: height // 2, 0: width // 2] = sample
    img[0: height // 2, width // 2: width] = sample
    img[height // 2: height, 0: width // 2] = sample
    img[height // 2: height, width // 2: width] = sample
    img = resize_frame(img, 1.5)
    cv.imshow('Capture', img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
