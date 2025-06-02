# OpenCV for image processing
#
# Copyright 2025 Leo Yeh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2 as cv

img = cv.imread("./bin/sudoku_warpped.jpg")

cell_size = 324 // 9
for i in range(9):  # row
    for j in range(9):  # column
        x = j * cell_size
        y = i * cell_size
        cell = img[y + 4:y + cell_size - 4, x + 4:x + cell_size - 4]
        filename = f"./digits/cell_{i}_{j}.jpg"
        cv.imwrite(filename, cell)
