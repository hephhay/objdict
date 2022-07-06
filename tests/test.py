from objdict_hephhay import ObjDict

#test for kwargs initialization
input0 = ObjDict(foo = 1, baz = 2)
output0 = [input0 == {'foo' : 1, 'baz' : 2}, input0.foo == 1, 'kwargs initialization failed']

#test for Mapping initialization
input1 = ObjDict({'foo' : 1, 'baz' : 2})
output1 = [input1.baz == 2, 'Mapping initialization failed']

#test for kwargs initialization with depth
input2 = ObjDict(foo = 1, bar = 2, baz = {"alice" : 3, "bob" : {"steph" : 5}}, obj__depth = 1)
output2 = [type(input2.baz) == ObjDict, type(input2.baz.bob) == dict, 'kwargs with depth failed']

#test for Mapping initialization with depth
input3 = ObjDict({'foo' : 1, 'bar' : 2, 'baz' : {"alice" : 3, "bob" : {"steph" : 5}}}, obj__depth = 1)
output3 = [type(input3.baz) == ObjDict, type(input3.baz.bob) == dict, 'Mapping with depth failed']

#test for empty initialization
input4 = ObjDict()
output4 = [input4 == {}, 'empty initialization failed']

#test for setitem and getattr
input5 = ObjDict()
input5.foo = 1
output5 = [input5['foo'] == 1, 'getatrr and getitem failed']

output = [output0, output1, output2, output3, output4, output5]

for case in output:
    assert all(case[0:-1]) == True, case[-1]