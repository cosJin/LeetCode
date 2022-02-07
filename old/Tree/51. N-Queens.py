class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []
            self.result = []
            self.cols = set();self.pie = set();self.na = set()
            self.DFS(n,0,[])
            