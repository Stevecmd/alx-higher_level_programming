# 0x07. Python - Test-driven development 

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything

## To run the individual tests run: <br />
1. `0-add_integer.py`

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