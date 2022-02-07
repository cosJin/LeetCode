class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #方法一，碰到陆地就 相邻的陆地均去掉。count++
        #去掉相邻陆地：DFS or BFS 
        #方法二：并查集：
        #初始化：所有1的节点的老大均为自己
        #遍历所有节点：相邻节点合并  1就尝试合并，0不管
        #遍历，查有多少个root 可以不同遍历，直接利用上一个的遍历 边遍历边统计即可