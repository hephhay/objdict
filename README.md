# OBJDICT
An object wrapper for dict that allows for using object type notation with dictionaries.
## Installation
pip3 -m install objdict
## Description
An object style implementation for dict that allows for using object type dot(.) notation with dictionaries.

All dict operations such as .pop(), .items(), .contains() etc' will also work with ObjDict

Example
--------
    from objdict_hephhay import ObjDict
    object = ObjDict(<dict>)

    object.<dict key>
## usage
Parameters
----------
dict : int
    Dictionary to convert

depth : int
    Second number to add = 0 if you want only a single level of conversion

Returns
-------
objdict.ObjDict
    An instance of ObjDict

Examples
--------
    >>>  obj = ObjDict(foo = 1, bar = 2)
    <ObjDict : {"foo" : 1, "bar" : 2}>
    >>> dictionary = {"foo" : 1, "bar" : 2}
    >>> obj1 = ObjDict(dictionary)
    >>> obj1.foo
    1
    >>> dictionary_2 = {"foo" : 1, "bar" : 2, "baz" : {"alice" : 3, "bob" : {"steph" : 5}}}
    >>> obj2 = ObjDict(dictionary_2, depth = 1)
    >>> obj2.bar
    2
    >>> obj2.baz
    <ObjDict : {'alice': 3, 'bob': {'steph': 5}}>
