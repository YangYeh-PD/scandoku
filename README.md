# Scandoku
**Scandoku** aims to simplify the Sudoku-solving experience by letting users take a photo of any puzzle and get the solution instantly with no 
manual input required. It also serves as a demonstration of combining computer vision, machine learning, and algorithmic problem-solving into a 
practical application.

## Features
- Solve 9×9 Sudoku puzzles using naive backtracking.
- Using [OpenCV](https://github.com/opencv/opencv) to find Sudoku problem contour and split into 81 cells.
- Integrated with [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for image-based printed digits recognition.

## Installation
Since the project is built based on OpenCV and Tesseract, we have to download these Python modules.
### Linux (Ubuntu)
```bash
sudo apt update
sudo apt install python3-opencv
sudo apt install tesseract-ocr
pip install pytesseract
```
### macOS
```bash
pip3 install opencv-python
brew install tesseract
pip3 install pytesseract
```
### Check the installation
Execute the following commands,
```bash
python3 -c "import cv2; print(cv2.__version__)"
tesseract --version
```
you should get the result
```bash
4.11.0
tesseract 5.5.1
```

## Future Works
- Solving performance improvement. (MRV Method)

## Contributing
Thanks for contributing the project. Please adhere to the following instructions.

1. Fork the Project
2. Create your Feature Branch
```bash
git checkout -b AmazingFeature
```
3. Commit your Changes
4. Push to the Branch
```
git push origin AmazingFeature
```
5. Open a Pull Request

## License
This project is open-source and available under the MIT License. See `LICENSE` for more information.

## Reference
- [Sudoku Wikipedia](https://en.wikipedia.org/wiki/Sudoku)
- [How to write a Git commit message](https://cbea.ms/git-commit/)
