import cv2 as cv

img = cv.imread("../bin/sudoku_warpped.jpg")

cell_size = 900 // 9
for i in range(9):  # row
    for j in range(9):  # column
        x = j * cell_size
        y = i * cell_size
        cell = img[y:y+cell_size, x:x+cell_size]
        filename = f"../bin/cell_{i}_{j}.jpg"
        cv.imwrite(filename, cell)
