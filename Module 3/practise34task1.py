a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
e = a.count(5)
print(e)
for i in a:
    if i == 5:
        a.remove(i)
print(a)
for i in c:
    a.append(i)
    t = a.count(3)
print(t)
print(a)