CC = g++
CFLAGS = -c -Wall
SRC_DIR = src
BIN_DIR = bin

TARGET = $(BIN_DIR)/solve

SRCS = $(wildcard $(SRC_DIR)/*.cpp)

OBJS = $(patsubst $(SRC_DIR)/%.cpp,$(BIN_DIR)/%.o,$(SRCS))

all: $(TARGET)

$(TARGET): $(OBJS)
	@echo "-----------------------------"
	@echo "Creating executable for solve"
	@echo "-----------------------------"
	$(CC) $^ -o $@

$(BIN_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	-rm -f $(BIN_DIR)/*.o $(BIN_DIR)/*.jpg $(TARGET)

# Dependency Chain
$(BIN_DIR)/solve.o: $(SRC_DIR)/solve.cpp $(SRC_DIR)/sudoku.h
$(BIN_DIR)/sudoku.o: $(SRC_DIR)/sudoku.cpp $(SRC_DIR)/sudoku.h

