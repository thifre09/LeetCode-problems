class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board: list[list[int]] = []
        for linha in range(m):
            board.append([])
            for coluna in range(n):
                if linha == 0 or coluna == 0:
                    board[linha].append(1)
                    continue
                board[linha].append(board[linha][coluna-1] + board[linha-1][coluna])
        return board[-1][-1]
    
        # board = [[1 if l == 0 or c == 0 else 0 for c in range(n)] for l in range(m)];[[board.__setitem__(l, board[l][:c] + [board[l][c-1] + board[l-1][c]] + board[l][c+1:]) for c in range(1, n)] for l in range(1, m)]; return board[-1][-1]


a = Solution()
print(a.uniquePaths(4,4))
