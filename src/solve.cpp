#include <cstdlib>
#include <fstream>
#include <iostream>

#include "sudoku.h"
using namespace std;

bool solve(Sudoku, Sudoku &);

int main(int argc, char *argv[]) {
    int num;
    Sudoku ques, ans;
    ifstream inFile("./test/problem", ios::in);
    if (!inFile) {
        cout << "Failed to open problem file" << endl;
        exit(1);
    }
    ofstream outFile("./test/solution", ios::out);
    if (!outFile) {
        cout << "Failed to open solution file" << endl;
        exit(1);
    }

    for (int i = 0; i < Sudoku::Sudokusize; i++) {
        inFile >> num;
        ques.map[i] = num;
    }

    // Tell you whether a Sudoku question has a solution
    // If yes, it will print it out
    if (solve(ques, ans)) {
        cout << "Solvable!\n";
        for (int i = 0; i < Sudoku::Sudokusize; i++) {
            cout << ans.map[i] << " ";
            outFile << ans.map[i] << " ";
            if (i % 9 == 8) {
                cout << endl;
                outFile << endl;
            }
        }
    } else {
        cout << "Unsolvable!!\n";
        cout << endl;
    }
    return 0;
}

// Solve Sudoku with naive BackTracking
bool solve(Sudoku question, Sudoku &answer) {
    int firstZero;
    firstZero = question.getFirstZeroIndex();
    if (firstZero == -1) {  // Ending Condition
        if (question.isCorrect()) {
            answer = question;
            return true;
        } else {
            return false;
        }
    } else {  // Recursive Relation
        for (int num = 1; num <= 9; num++) {
            question.map[firstZero] = num;
            if (!question.isLegal(firstZero)) {
                continue;
            } else if (solve(question, answer)) {
                return true;
            }
        }
    }
    return false;
}
