from math import inf
from operator import delitem, setitem
from typing import Any
from collections import UserDict

class ObjDict(UserDict):

    """
        An object wrapper for dict that allows for using object type notation with dictionaries.

        Example
        --------
            object = ObjDict(<dict>)
            object.<dict key>

        Attributes:
        ----------
            data : dict
                Holds a refrence 'dict' passed to Object
    """

    data = {}
    __depth = 0

    def __init__(self, dict=None, depth = inf, **kwargs):

        """from util import ObjDict
            dictionary_2 = {"foo" : 1, "bar" : 2, "baz" : {"alice" : 3, "bob" : {"steph" : 5}}}
            obj2 = ObjDict(dictionary_2, depth = 1)
            
            initializes ObjDict.

            This function simply takes dict kwargs and convert it to a nested obj.

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

        """

        if not isinstance(depth, (int, float)):
            raise TypeError(f"depth must be int but got {type(depth).__name__}")
        self.data = {}
        if dict is not None:
            self.update(dict)
        if kwargs:
            self.update(kwargs)
        self.__depth = depth
        self.__setter(self.data)


    def __checker(self, key)  -> None:
        if key in self.__dict__.keys():
            raise ValueError(f"{key} is a property of instance {self.__name__}")

    def __setter(self, update_dict) -> None:
        self.data.pop('_ObjDict__depth')
        for key, value in update_dict.items():
            self.__checker(key)
            self.__setitem__(key, value if not isinstance(value, dict) or self.__depth < 1 else ObjDict(value, self.__depth - 1))

    def __setattr__(self, name: str, value: Any) -> None:
            self.__checker(name)
            setitem(self.data, name, value)

    def __delattr__(self, name: str) -> None:
        try:
            return delitem(self.data, name)
        except KeyError:
            return super().__delattr__(name)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) ->  str:
        return f"<{type(self).__name__} : {self.data}>"