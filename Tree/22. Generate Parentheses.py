class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    #方法一：每一个地方可以填（ or ） 判断是否合法，
    # 但是明显有（（（（（（的情况，
    # 所以方法二：在一的基础上剪枝，局部不合法则不继续下去，
    # 只有三个（ 和三个）  记住左右括号分别几个。    
    self.list = []
    self._gen(0,0,n,"")
    return self.list
    def _gen(self,left,right,n,result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left+1,right,n,result+"(")
        if right < n and left > right:
            self._gen(left,right+1,n,result+")")