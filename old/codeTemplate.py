#代码模板：
#1、迭代 recursion：
def recursion(level, param1, param2,...):
    if level > MAX_LEVEL：  #终止条件，如果迭代层数达到最大，返回结果
        print_result
        return
    
    process_data(level, data...) #处理当前层的数据

    self.recursion(level + 1, p1, ...) #深入一层
    reverse_state(level) #深入一层的内容处理完成后，如果需要，返回本层时重置level
#2、DFS递归写法
visited = set()
def dfs(node,visited):
    visited.add(node) #把当前节点添加到已访问节点中
    process_current_node()   #对当前的节点进行处理

    for next_node in node.children(): #遍历子节点 
        if not next_node in visited:
            dfs(next_node,visited)
#3、BFS
def BFS(graph, start, end):
    queue = []
    queue.append([start]) #将开始节点添加到队列中
    visited.add(start)   #将开始节点添加到已访问节点中

    while queue:
        node = queue.pop()  #将队列中的节点一个个弹出
        visited.add(node)   #添加到访问节点中

        process_node() #对这个节点进行处理
        nodes = generate_related_nodes(node)   #找到和该节点相关的下一层所有节点
        queue.push(nodes)   #将与之相关的所有节点添加到队列中去
#4、二分查找模板
left, right = 0, len(array) - 1
while left <= right:
    mid = left + (right = left)/2
    if array[mid] == target:  #先查，查到就返回
        break or return result
    elif array[mid] < target:
        left = mmid + 1
    else:
        right = mid - 1
#5、动态规划    两步走：1、状态定义 2、状态转移方程

dp = new int[m+1][n+1]#状态定义
dp[0][0] = x    #初始状态
dp[0][1] = y
....

for i = 0; i < n; ++i{
    for j = 0; j <= m; ++j{
        ....    #dp状态推导
        dp[i][j] = min{dp[i-1][j],dp[i][j-1],etc.}
    }
}
return dp[m][n]