class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board is None or len(board) == 0:
            return []
        
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, board[i][j], word_set, prefix_set, set([(i, j)]), result)
        return list(result)
    
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        if word in word_set:
            result.add(word)
        dirc=[(-1,0),(1,0),(0,1),(0,-1)]
        for d in dirc:
            nx = x + d[0]
            ny = y + d[1]
            if nx>=0 and nx<len(board) and ny>=0 and ny<len(board[0]) and (nx,ny) not in visited:
                visited.add((nx, ny))
                self.search(board, nx, ny, word + board[nx][ny], word_set, prefix_set, visited, result)
                visited.remove((nx, ny))
