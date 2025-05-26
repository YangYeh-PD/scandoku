class Sudoku {
   public:
    Sudoku();
    Sudoku(const int init_map[]);
    void setMap(const int set_map[]);
    void setElement(int index, int value);
    int getFirstZeroIndex();
    int getElement(int index);
    bool isLegal(int index);
    bool isCorrect();

    static const int Sudokusize = 81;

   private:
    bool checkUnity(int arr[]);
    int map[Sudokusize];
};
