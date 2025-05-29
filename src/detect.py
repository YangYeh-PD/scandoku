import cv2 as cv
import numpy as np

# Reorder the rectangle points
def reorder_points(pts):
    pts = pts.reshape((4, 2))
    new_pts = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    new_pts[0] = pts[np.argmin(s)]
    new_pts[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    new_pts[1] = pts[np.argmin(diff)]
    new_pts[3] = pts[np.argmax(diff)]

    return new_pts

img = cv.imread("../test/input.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), 0)
canny = cv.Canny(blur, 125, 175)
thresh = cv.adaptiveThreshold(canny, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 5, 2)

blank = np.zeros(img.shape, dtype="uint8")
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found!")
cv.drawContours(blank, contours, -1, (255, 255, 255), 1)

# Find the maximum rectangle
max_area = 0
sudoku_contour = None
for contour in contours:
    area = cv.contourArea(contour)
    if area > 1000: # avoid the noice
        peri = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.05 * peri, True)
        if len(approx) == 4 and area > max_area:
            sudoku_contour = approx
            max_area = area

src_pts = reorder_points(sudoku_contour)
dst_pts = np.array([
    [0, 0],
    [900, 0],
    [900, 900],
    [0, 900]
], dtype="float32")

M = cv.getPerspectiveTransform(src_pts, dst_pts)
warped = cv.warpPerspective(thresh, M, (900, 900))
cv.imwrite("../bin/sudoku_warpped.jpg", warped)
