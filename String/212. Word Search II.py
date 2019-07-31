import collections
dx = [-1, 1, 0, 0]   #控制上下左右的x 和 y
dy = [0, 0, -1, 1]
end_of_word = "#"
class Solution:
    def findWords(self, board , words):
        if not board or not board[0]: return []
        if not words:return []

        self.result = set ()
        root = collections.defaultdict()
        for word in words:                      #将所有words 存入trie,他们公用一个root。
            node = root
            for char in word:
                node = node.setdefault(char,collections.defaultdict())
            node[end_of_word] = end_of_word
        
        self.m, self.n = len(board),len(board[0])     # m行 n列

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:           #棋盘上的每个字母进行查找，第一个字母能匹配上root的则开始深度搜索
                    self._dfs(board,i,j,"",root)

    def _dfs(self,board,i,j,cur_word,cur_dict):
        cur_word += board[i][j]    #记录当前路径
        cur_dict = cur_dict[board[i][j]] #进入下层子节点
        
        if end_of_word in cur_dict:
            self.result.add(cur_dict)

        tmp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp  #如果没找到或者递归出来了，则通过tmp将i j还原。    前面讲i j替换为@是为了防止重复使用某一个单元格。