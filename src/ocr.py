# OpenCV module for image processing
# Tesseract OCR for printed digits recognization
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

import os
import numpy as np
import cv2 as cv
import pytesseract

def is_blank(img, ratio = 0.9250):
    if np.sum(img) > 28 * 28 * 255 * ratio:
        return True
    else:
        return False

with open("./test/problem", "w") as file:  # clear the problem.txt
    pass
file = open("./test/problem", "a")

for i in range(9):  # row
    for j in range(9):  # column
        img = cv.imread(f"./digits/cell_{i}_{j}.jpg")
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if is_blank(img):
            file.write('0')
            file.write(' ')
        else:
            file.write(str(int(pytesseract.image_to_string(img, config="--psm 10 digits"))))
            file.write(' ')
    file.write('\n')

file.close()
