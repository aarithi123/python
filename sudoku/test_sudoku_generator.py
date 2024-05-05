import sudoku_generator


def main():
    grid = sudoku_generator.generate_sudoku(9,30)
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
