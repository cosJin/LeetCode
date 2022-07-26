a=[[],[1],[2,3],[3,4,5]]
for j in range(len(a)):
    a.append(a[j][:])
print(a)