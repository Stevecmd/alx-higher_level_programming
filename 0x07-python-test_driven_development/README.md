# 0x07. Python - Test-driven development 

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything

## To run the individual tests run: <br />
0. Integers addition 

Write a function that adds 2 integers.

 - Prototype: `def add_integer(a, b=98):`
 - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer or b must be an integer`
 - `a` and `b` must be first casted to integers if they are float
 - Returns an integer: the addition of `a` and `b`
 - You are not allowed to import any module


    My test 1 :
    ```sh
        python3 -m doctest ./tests/0-add_integer.txt
    ```
    
    My test 2 :
    ```sh
    python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
    17 passed and 0 failed.
    Test passed.
    ```
    Official test to also check word count: 
    ```sh
    python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
    5
    ```

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
17 passed and 0 failed.
Test passed.
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
1

```
File: `0-add_integer.py`, `tests/0-add_integer.txt`

1. Divide a matrix 

Write a function that divides all elements of a matrix.

 - Prototype: `def matrix_divided(matrix, div):`
 - `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
 - Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
 - `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
 - `div` can’t be equal to 0, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
 - All elements of the matrix should be divided by div, rounded to 2 decimal places
 - Returns a new matrix
 - You are not allowed to import any module

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.

```

File: `2-matrix_divided.py`, `tests/2-matrix_divided.txt`


2. Say my name 

Write a function that prints My name is `<first name>` `<last name>`

 - Prototype: `def say_my_name(first_name, last_name=""):`
 - `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
 - You are not allowed to import any module
```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.

```

File: `3-say_my_name.py`, `tests/3-say_my_name.txt`

3. Print square

Write a function that prints a square with the character #.

 - Prototype: `def print_square(size):`
 - `size` is the size length of the square
 - `size` must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
 - if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
 - if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
 - You are not allowed to import any module


```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./4-main.py
####
####
####
####

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


#

size must be >= 0

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m doctest -v ./tests/4-print_square.txt
Trying:
    print_square = __import__('4-print_square').print_square
Expecting nothing
ok
Trying:
    print_square(1)
Expecting:
    #
ok
Trying:
    print_square(3)
Expecting:
    ###
    ###
    ###
ok
Trying:
    print_square(8)
Expecting:
    ########
    ########
    ########
    ########
    ########
    ########
    ########
    ########
ok
Trying:
    print_square("not an int")
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
ok
Trying:
    print_square(3.5)
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
ok
1 items passed all tests:
   6 tests in 4-print_square.txt
6 tests in 1 items.
6 passed and 0 failed.
Test passed.

```

File: `4-print_square.py`, `tests/4-print_square.txt`

4. Text indentation 

Write a function that prints a text with 2 new lines after each of these characters: `., ?` and `:`

 - Prototype: `def text_indentation(text):`
 - `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
 - There should be no space at the beginning or at the end of each printed line
 - You are not allowed to import any module

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
 Quonam modo?$
$
 Utrum igitur tibi litteram videor an totas paginas commovere?$
$
 Non autem hoc:$
$
 igitur ne illud quidem.$
$
 Fortasse id optimum, sed ubi illud:$
$
 Plus semper voluptatis?$
$
 Teneo, inquit, finem illi videri nihil dolere.$
$
 Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
 Si id dicis, vicimus.$
$
 Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
 Sin aliud quid voles, postea.$
$
 Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
 Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres$
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m doctest -v ./tests/5-text_indentation.txt
Trying:
    text_indentation = __import__('5-text_indentation').text_indentation
Expecting nothing
ok
1 items passed all tests:
   1 tests in 5-text_indentation.txt
1 tests in 1 items.
1 passed and 0 failed.
Test passed.

```
File: `5-text_indentation.py`, `tests/5-text_indentation.txt`

5. Max integer - Unittest 

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):.`

 - Your test file should be inside a folder `tests`
 - You have to use the `unittest module`
 - Your test file should be python files (extension: `.py`)
 - Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
 - All tests you make must be passable by the function below
 - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./6-main.py
4
4
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

```
File: `tests`/`6-max_integer_test.py`

6. Matrix multiplication 

Write a function that multiplies 2 matrices:

- Prototype: `def matrix_mul(m_a, m_b):`

- `m_a` and `m_b` must be validated with these requirements in this order

- `m_a` and `m_b` must be an list of lists of integers or floats:

    - if `m_a` or `m_b` is not a list: raise a TypeError exception with the message `m_a must be a list` or `m_b must be a list`
    - if `m_a` or `m_b` is not a list of lists: raise a TypeError exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`
    - if `m_a` or `m_b` is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be empty
    - if one element of those list of lists is not an integer or a float: raise a `TypeError` exception with the message `m_a should contain only integers` or `floats or m_b should contain only integers or floats`
    - if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a `TypeError` exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`

- If `m_a` and `m_b` can’t be multiplied: raise a ValueError exception with the message `m_a and m_b can't be multiplied`

- You are not allowed to import any module
```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ ./100-main.py
[[7, 10], [15, 22]]
[[13, 16]]
stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.

```
File: `100-matrix_mul.py`, `tests/100-matrix_mul.txt`

7. Lazy matrix multiplication

Write a function that multiplies 2 matrices by using the module `NumPy`

To install it: `pip3 install numpy==1.15.0`

- Prototype: `def lazy_matrix_mul(m_a, m_b):`
- Test cases should be the same as `100-matrix_mul` but with new exception type/message

8. CPython #3: Python Strings 

Create a function that prints Python strings.

- Prototype: `void print_python_string(PyObject *p);`
- Format: see example
- If `p` is not a valid string, print an error message (see example)

About:

- Python version: 3.4
- You are allowed to use the C standard library
- Your shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/0x07-python-test_driven_development$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"

```

```sh

julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c

```
if above command doesnt work use:
```sh

gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC $(python3-config --includes) 102-python.c

```

```sh

root@89241ea4ff1f:/alx-higher_level_programming/0x07-python-test_driven_development# python3 102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object

```

File: `102-python.c`