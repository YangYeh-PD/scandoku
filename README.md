# 📘 Scandoku
**Scandoku** aims to simplify the Sudoku-solving experience by letting users take a photo of any puzzle and get the solution instantly—no manual 
input required. It also serves as a demonstration of combining computer vision, machine learning, and algorithmic problem-solving into a practical 
application.

## 📌 Features
- Solve 9×9 Sudoku puzzles using backtracking.
- Using [OpenCV](https://github.com/opencv/opencv) to find Sudoku problem contour and split into 81 cells for recognition.
- Integrated with [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for image-based printed digits recognition.

## 🚫 Limitations
- It currently cannot judge whether the problem has only one solution or many solutions.
- Some digit recognitions might be wrong.

## 🔭 Future Work
- Automatic Control.
- Build GUI for result. (SDL3)
- Performance improvement. (MRV Method)

## 📝 Reference
- [Sudoku Wikipedia](https://en.wikipedia.org/wiki/Sudoku).
