# 0x0A. Python - Inheritance 
## General

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### Documentation

- Do not use the words `import` or `from` inside your comments,

## Tasks
0. Lookup

Write a function that returns the list of available attributes and methods of an object:

 - Prototype: `def lookup(obj):`
 - Returns a `list` object
 - You are not allowed to import any module


```sh
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ cat 0-main.py 
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ chmod u+x 0-main.py 
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

```


File: `0-lookup.py`

1. My list 

Write a class MyList that inherits from list:

 - Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
 - You can assume that all the elements of the list will be of type int
 - You are not allowed to import any module

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ chmod u+x 1-my_list.py
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ chmod u+x 1-main.py
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x0A-python-inheritance$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]

```

File: `1-my_list.py, tests/1-my_list.txt`


2. Exact same object 













File: `2-is_same_class.py`

3. Same class or inherit from 








File: `3-is_kind_of_class.py`

4. Only sub class of 










File: `4-inherits_from.py`

5. Geometry module









File: `5-base_geometry.py`

6. Improve Geometry 











File: `6-base_geometry.py`

7. Integer validator 
















File: `7-base_geometry.py`, `tests/7-base_geometry.txt`

8. Rectangle 











File: `8-rectangle.py`


9. Full rectangle 


















File: `9-rectangle.py`

10. Square #1 












File: `10-square.py`

11. Square #2 


















File: `11-square.py`

12. My integer 













File: `100-my_int.py`

13. Can I? 











File: `101-add_attribute.py`