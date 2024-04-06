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