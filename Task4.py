import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

img=cv2.imread("Resources/Image1.jpeg")
imgContour=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlurr=cv2.GaussianBlur(img,(5,5),1)
imgCanny=cv2.Canny(imgBlurr,400,400)

contours = getContours(imgCanny)

if contours:
    largest=max(contours,key=cv2.contourArea)

    rect = cv2.minAreaRect(largest)
    box = cv2.boxPoints(rect)
    box = np.int32(box)

    # for cnt in contours:
    cv2.drawContours(imgContour, [box], 0, (0, 0, 255), 2)

    center, (width, height), angle = rect
    print(angle)
    # if angle < -45:
    #     angle += 90

    if -45 <= angle < 45:
        direction = "Right"
    elif 45 <= angle < 135:
        direction = "Upward"
    elif 135 <= angle < 225:
        direction = "Left"
    else:
        direction = "Downward"

    print(f"Direction of the arrow: {direction}")

cv2.imshow('Detected Arrow', imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()
