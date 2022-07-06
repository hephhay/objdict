from math import inf
from operator import delitem
from typing import Any
from _collections_abc import MutableMapping, Mapping

class man(object):
    pass

class ObjDict(MutableMapping):

    """
        An object style implementation for dict that allows for using object type dot(.) notation with dictionaries.

        All dict operations such as .pop(), .items(), .contains() etc' will also work with ObjDict

        Example
        --------
            object = ObjDict(<dict>)

            object.<dict key>

        Attributes:
        ----------
            __data__ : dict
                Holds a refrence 'dict' passed to Object
            __depth__: int
                Holds the value for the 'depth' of the instance
    """

    def __init__(self, dict : Mapping = None, obj__depth : int = inf ,**kwargs):

        """initializes ObjDict.

            This function simply takes dict or kwargs and convert it to a nested obj of depth specified by obj__depth.

            Parameters
            ----------
            dict : int
                Dictionary to convert
            obj__depth : int, optional
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
            >>> obj2 = ObjDict(foo = 1, bar = 2, baz = {"alice" : 3, "bob" : {"steph" : 5}}, obj__depth = 1)
            >>> obj2.bar
            2
            >>> obj2.baz
            <ObjDict : {'alice': 3, 'bob': {'steph': 5}}>
            >>> type(obj2.baz.bob)
            dict

        """
        if not isinstance(obj__depth, (int, float)):
            raise TypeError(f"depth must be int but got {type(obj__depth).__name__}")

        depth = kwargs.pop('obj__depth', inf)

        if depth != inf:
            obj__depth = depth

        self.__data__ = {}
        self.__depth__ = obj__depth

        if dict is not None:
            self.update(dict)
        if kwargs:
            self.update(kwargs)

    #check if key not an attribute of instance
    def __checker(self, key)  -> None:
        return False if key in self.__dict__.keys() else True
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        #prevent '__data__' and '__depth__' from being keys of the instance
        if self.__checker(__name) and __name not in ('__data__', '__depth__'):
            return self.__setitem__(__name, __value)
        return super().__setattr__(__name, __value)

    def __delattr__(self, name: str) -> None:
        #delete item from dict on error delete from attributes 
        try:
            return self.__delitem__(name)
        except KeyError:
            return super().__delattr__()

    def __getattr__(self, name: str) -> None:
        #get item from dict on error get from attributes
        try:
            return self.__getitem__(name)
        except KeyError:
            return self.__getattribute__(name)

    def __len__(self):
        return len(self.__data__)

    def __getitem__(self, key):
        if key in self.__data__:
            return self.__data__[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(key)

    def __setitem__(self, key, item):
        if self.__depth__ > 0 and isinstance(item, Mapping):
            self.__data__[key] = ObjDict(item, self.__depth__ -1)
        else:
            self.__data__[key] = item

    def __delitem__(self, key):
        del self.__data__[key]

    def __iter__(self):
        return iter(self.__data__)

    # Modify __contains__ to work correctly when __missing__ is present
    def __contains__(self, key):
        return key in self.__data__

    # Now, add the methods in dicts but not in MutableMapping
    def __repr__(self):
        return repr(self.__data__)

    def __str__(self) ->  str:
        return f"<{type(self).__name__} : {self.__data__}>"

    def __or__(self, other):
        if isinstance(other, ObjDict):
            return self.__class__(self.__data__ | other.__data__)
        if isinstance(other, dict):
            return self.__class__(self.__data__ | other)
        return NotImplemented

    def __ror__(self, other):
        if isinstance(other, ObjDict):
            return self.__class__(other.__data__ | self.__data__)
        if isinstance(other, dict):
            return self.__class__(other | self.__data__)
        return NotImplemented

    def __ior__(self, other):
        if isinstance(other, ObjDict):
            self.__data__ |= other.__data__
        else:
            self.__data__ |= other
        return self

    def __copy__(self):
        inst = self.__class__.__new__(self.__class__)
        inst.__dict__["__depth__"] = self.__dict__["__depth__"].copy()
        inst.__dict__.update(self.__dict__)
        # Create a copy and avoid triggering descriptors
        inst.__dict__["__data__"] = self.__dict__["__data__"].copy()
        return inst

    def copy(self):
        if self.__class__ is ObjDict:
            return ObjDict(self.__data__.copy())
        import copy
        __data__ = self.__data__
        try:
            self.__data__ = {}
            c = copy.copy(self)
        finally:
            self.__data__ = __data__
        c.update(self.__data__, )
        return c

    @classmethod
    def fromkeys(cls, iterable, value=None):
        d = cls()
        for key in iterable:
            d[key] = value
        return d