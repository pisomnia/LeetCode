class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(board)
        M = len(board[0])
        found = True
        while found:
            found = False
            for i in range(N):
                for j in range(M):
                    val = abs(board[i][j])
                    if val == 0:
                        continue
                    if j < M - 2 and abs(board[i][j + 1]) == val and abs(board[i][j + 2]) == val:
                        found = True
                        ind = j
                        while ind < M and abs(board[i][ind]) == val:
                            board[i][ind] = -val
                            ind += 1
                    if i < N - 2 and abs(board[i + 1][j]) == val and abs(board[i + 2][j]) == val:
                        found = True
                        ind = i
                        while ind < N and abs(board[ind][j]) == val:
                            board[ind][j] = -val
                            ind += 1
            if found:
                for j in range(M):
                    storeInd = N - 1
                    for i in range(N-1, -1, -1):
                        if board[i][j] > 0:
                            board[storeInd][j] = board[i][j]
                            storeInd -= 1
                    for k in range(storeInd, -1, -1):
                        board[k][j] = 0
        return board 