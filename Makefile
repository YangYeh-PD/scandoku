CC = g++
CFLAGS = -c -Wall
SRC_DIR = src
BIN_DIR = bin
DIGITS_DIR = digits

TARGET = $(BIN_DIR)/solve
SRCS = $(wildcard $(SRC_DIR)/*.cpp)
OBJS = $(patsubst $(SRC_DIR)/%.cpp,$(BIN_DIR)/%.o,$(SRCS))

# Compile and Run
all: $(TARGET) run

$(TARGET): $(OBJS)
	@echo "--- Creating executable for solve ---"
	$(CC) $^ -o $@

$(BIN_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) $< -o $@

run:
	@echo "--- Running detect.py ---"
	python3 $(SRC_DIR)/detect.py
	@echo "--- Running split.py ---"
	python3 $(SRC_DIR)/split.py
	@echo "--- Running ocr.py ---"
	python3 $(SRC_DIR)/ocr.py
	@echo "--- Running solve ---"
	$(TARGET)

.PHONY: clean
clean:
	-rm -f $(BIN_DIR)/*.o $(BIN_DIR)/*.jpg $(DIGITS_DIR)/*.jpg $(TARGET)

# Dependency Chain
$(BIN_DIR)/solve.o: $(SRC_DIR)/solve.cpp $(SRC_DIR)/sudoku.h
$(BIN_DIR)/sudoku.o: $(SRC_DIR)/sudoku.cpp $(SRC_DIR)/sudoku.h

