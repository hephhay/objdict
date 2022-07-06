from util import ObjDict

list = ObjDict(obj__depth = 1, ade = 'kola', fara = 'yola', da = {'n' : 'e', 'l' : {'papa' : 'data'}})

print(list)
print(list.ade)
print(list.da.l)

for i in list:
    print(list[i])

print(tuple(list.keys()))