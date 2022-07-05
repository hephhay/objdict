# OBJDICT
An object wrapper for dict that allows for using object type notation with dictionaries.
## Installation
pip3 -m install objdict
## usage
            from objdict.util import ObjDict
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
