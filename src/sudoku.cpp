#include "sudoku.h"

Sudoku::Sudoku() {
    for (int i = 0; i < Sudokusize; i++) map[i] = 0;
}
Sudoku::Sudoku(const int init_map[]) {
    for (int i = 0; i < Sudokusize; i++) map[i] = init_map[i];
}
void Sudoku::setMap(const int set_map[]) {
    for (int i = 0; i < Sudokusize; i++) map[i] = set_map[i];
}
void Sudoku::setElement(int index, int value) { map[index] = value; }
int Sudoku::getFirstZeroIndex() {
    for (int i = 0; i < Sudokusize; i++) {
        if (map[i] == 0) return i;
    }
    return -1;
}
int Sudoku::getElement(int index) { return map[index]; }
bool Sudoku::checkUnity(int arr[]) {
    int arr_unity[9];  // counters

    for (int i = 0; i < 9; i++) arr_unity[i] = 0;         // initialize
    for (int i = 0; i < 9; i++) ++arr_unity[arr[i] - 1];  // count
    for (int i = 0; i < 9; i++) {
        if (arr_unity[i] != 1)  // all element
            return false;       // must be 1
    }
    return true;
}
// Check if the elements before index are all unique
bool Sudoku::isLegal(int index) {
    // check the row
    for (int column = (index / 9) * 9; column < ((index / 9) + 1) * 9;
         column++) {
        if (column != index && map[column] == map[index]) return false;
    }
    // check the column
    for (int row = (index % 9); row < (index % 9) + Sudokusize; row += 9) {
        if (row != index && map[row] == map[index]) {
            return false;
        }
    }
    // check the cells
    int row = index / 9;
    int column = index % 9;
    int start_loc = (row / 3) * 27 + (column / 3) * 3;
    int counts = -1;
    for (int i = start_loc; i <= start_loc + 20;
         i += 1 + ((counts % 3) / 2) * 6) {
        if (i != index && map[i] == map[index]) {
            return false;
        }
        counts++;
    }
    return true;
}
// Check if the elements on entire Sudoku are unique
bool Sudoku::isCorrect() {
    bool check_result;
    int check_arr[9];
    int location;
    // check rows
    for (int i = 0; i < Sudokusize; i += 9) {
        for (int j = 0; j < 9; j++) {
            check_arr[j] = map[i + j];
        }
        check_result = checkUnity(check_arr);
        if (!check_result) {
            return false;
        }
    }
    // check columns
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j += 1) {
            check_arr[j] = map[i + j * 9];
        }
        check_result = checkUnity(check_arr);
        if (!check_result) {
            return false;
        }
    }
    // check cells
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            location = 27 * (i / 3) + 3 * (i % 3) + 9 * (j / 3) + (j % 3);
            check_arr[j] = map[location];
        }
        check_result = checkUnity(check_arr);
        if (!check_result) {
            return false;
        }
    }
    return true;
}
