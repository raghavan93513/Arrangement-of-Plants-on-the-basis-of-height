dict = {}
n = int(input())
c = []
for i in range(n):
    i = int(input())
    h = int(input())
    dict.update({h:i})
    c.append(h)
c.sort()

for i in c:
    d = dict[i]
    print(d)