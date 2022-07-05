from util import ObjDict

list = ObjDict(ade = 'kola', fara = 'yola', da = {'n' : 'e', 'l' : '.'})
print(list)
list.clear()
(list.papa = 5)

from util import ObjDict
dictionary_2 = {"foo" : 1, "bar" : 2, "baz" : {"alice" : 3, "bob" : {"steph" : 5}}}
obj2 = ObjDict(dictionary_2, depth = 1)
obj2