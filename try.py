n = 24
d = list(range(n)[2:])
a = list(range(22))
dic = dict(zip(d,a))
a = list(dic.keys())
print(a.count(3))
