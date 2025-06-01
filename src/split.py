import cv2 as cv

img = cv.imread("../bin/sudoku_warpped.jpg")

cell_size = 252 // 9
for i in range(9):  # row
    for j in range(9):  # column
        x = j * cell_size
        y = i * cell_size
        cell = img[y + 2:y + cell_size - 2, x + 2:x + cell_size - 2]
        filename = f"../digits/cell_{i}_{j}.jpg"
        cv.imwrite(filename, cell)
