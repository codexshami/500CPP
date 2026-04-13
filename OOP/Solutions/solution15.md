# Solution 15: Tic-Tac-Toe Game

## Approach Explanation
Board class manages 3x3 grid. Check rows, columns, diagonals for wins.

## Step-by-Step Logic
1. Board initializes 3x3 grid.
2. move places symbol, checks win.
3. Check all 8 winning conditions.

## Complexity
- **Time Complexity:** O(1) per move
- **Space Complexity:** O(1)

## Code
```python
class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.current = 'X'
    def move(self, r, c):
        if self.board[r][c] != ' ': return 'Invalid'
        self.board[r][c] = self.current
        if self._check_win(): return f'{self.current} wins!'
        self.current = 'O' if self.current == 'X' else 'X'
        return 'Continue'
    def _check_win(self):
        b, c = self.board, self.current
        for i in range(3):
            if all(b[i][j]==c for j in range(3)): return True
            if all(b[j][i]==c for j in range(3)): return True
        if all(b[i][i]==c for i in range(3)): return True
        if all(b[i][2-i]==c for i in range(3)): return True
        return False
```
