# a = set()
# a.add((1,1))
# a.add((1,2))

# print(len(a))

from collections import deque   
q = deque([(1,2)])

q.append((2,3))

q.append((2,3))
print(q)