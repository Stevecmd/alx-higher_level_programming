# 0x06. Python - Classes and Objects 
## Tasks

0. My first square 

Write an empty class Square that defines a square:

- You are not allowed to import any module
```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./0-main.py
<class '0-square.Square'>
{}

```

File: `0-square.py`

1. Square with size 

Write a class Square that defines a square by: (based on 0-square.py)

 - Instantiation with size (no type/value verification)
 - You are not allowed to import any module

Why?

Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'

```
File: `1-square.py`

2. Size validation 

Write a class Square that defines a square by: (based on 1-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
    - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- You are not allowed to import any module


```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0

```


3. Area of a square 
Write a class Square that defines a square by: (based on 2-square.py)

- Private instance attribute: size
- Instantiation with optional size: def __init__(self, size=0):
    - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25

```
File: `3-square.py`


4. Access and update private attribute 

Write a class Square that defines a square by: (based on 3-square.py)

- Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- You are not allowed to import any module

Why?

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer

```
File: `4-square.py`


5. Printing a square 

Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
    You are not allowed to import any module


```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--

```
File: `5-square.py`

6. Coordinates of a square 

Write a class Square that defines a square by: (based on 5-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self): that returns the current square area
    Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        position should be use by using space - Don’t fill lines by spaces when position[1] > 0
    You are not allowed to import any module

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x06-python-classes$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$

```

File: `6-square.py`


7. Singly linked list 




File: `100-singly_linked_list.py`

8. Print Square instance 




File: `101-square.py`

9. Compare 2 squares 



File: `102-square.py`


10. ByteCode -> Python #5 


File: `103-magic_class.py`



