def init(p):
    p = [i for i in range(n)]

def union(self,p,i,j):
    p1 = self.parent(p,i)
    p2 = self.parent(p,j)
    p[p1] = p2

def parent(self,p,i):  #从ｐ中不断网上找ｉ的头元素
    root = i
    while p[root] != root:
        root = p[root]   #找到i的最头元素root
    while p[i] != i:
        x = i;i=p[i];p[x]=root   #从i开始，往上的所有节点的parent设为root
    return root

