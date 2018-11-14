n = 10
l = [True]*n
l[0] = False
l[-1] = False
for i in range(int(n**0.5)+1)[2:]:
    print(i)
    l[2*i-1:-1:i] = [False]*(len(l[2*i-1:-1:i]))

print(l.count(True))
print(l)