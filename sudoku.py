from itertools import product as cp
import random

def solve(pz):
    for (r, c) in cp(range(0, 9), repeat=2):
        if pz[r][c] == 0:
            for n in range(1, 10):
                ok = True
                for i in range(0, 9):
                    if n in (pz[i][c], pz[r][i]):
                        ok = False
                        break
                for (i, j) in cp(range(0, 3), repeat=2):
                    if pz[r - r % 3 + i][c - c % 3 + j] == n:
                        ok = False
                        break
                if ok:
                    pz[r][c] = n
                    if try_pz := solve(pz):
                        return try_pz
                    pz[r][c] = 0
            return False
    return pz

def display(pz):

    pz = [['*' if n == 0 else n for n in r] for r in pz]
    s = ' ' * 9
    if any('*' in sl for sl in pz):
        s = f"\n{s}UNSOLVED PUZZLE\n"
    else:
        s = f"\n{s}COMPLETED PUZZLE\n"
    for r in range(0, 9):
        if ((r % 3 == 0) and (r != 0)):
            s += f"{'-' * 33}\n"
        for c in range(0, 9):
            if ((c % 3 == 0) and (c != 0)):
                s += ' | '
            s += f' {pz[r][c]} '
        s += '\n'
    s += "\n\n"
    print(s)



def generate_sudoku():
    """
    Generates a Sudoku puzzle with a unique solution.
    """
    one = list(range(1, 10))
    random.shuffle(one)
    grid = [[0 for _ in range(9)] for _ in range(8)]
    grid.insert(0,one)

    # Fill the grid with a solution
    solve(grid)

    # Remove numbers to create the puzzle
    squares = list(range(81))
    random.shuffle(squares)

    # Remove numbers while maintaining a unique solution.
    attempts = 50
    removed_cells = 0

    for _ in range(attempts):
      for i in range(20, 65): # This is how many empty cells can be removed
          if removed_cells >= i:
            break
          cell_index = squares[i]
          row = cell_index // 9
          col = cell_index % 9
          backup = grid[row][col]
          grid[row][col] = 0

          # Check if the puzzle is still solvable with the removed cell.
          grid_copy = [row[:] for row in grid]
          if not solve(grid_copy):
              grid[row][col] = backup
          else:
            removed_cells += 1

    return grid




# commands used in solution video for reference
if __name__ == '__main__':
    tp2 = generate_sudoku()
    display(tp2)
    display(solve(tp2))
