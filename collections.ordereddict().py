from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    *name,p=input().split()
    name=' '.join(name)
    d[name]=d.get(name,0)+int(p)
for k,v in d.items():
    print(k,v)
