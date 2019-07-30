dx = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
end_of_word = "#"
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words:return []

        self.result = set ()
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,collections.defaultdict())
            node[end_of_word] = end_of_word
        
        self.m, self.n = len(board),len(board[0])

        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] in root:
                    self._dfs(board,i,j,"",root)
        