# Resources

[Python TDD Workflow - Unit Testing Code Example for Beginners](https://www.youtube.com/watch?v=ibVSPVz2LAA&ab_channel=PythonSimplified)

## Laws of TDD
- You may not write production code until you have first written a failing unit test
- You may not write more of a unit test than is sufficient to fail
- You may not write more production code than is sufficient to make the failing test pass.

### Step 1:
```py

#!/usr/bin/python3
import unittest

class TestEncryption(unittest.TestCase):
    # Tests go here
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

if __name__ == "__main__":
    unittest.main()

```
output
```py

python3 caesarsCipher.py 
E
======================================================================
ERROR: test_inputExists (__main__.TestEncryption)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/stevecmd/alx-higher_level_programming/Test-Driven-Development/caesarsCipher.py", line 7, in test_inputExists
    self.assertIsNotNone(self.my_message)
AttributeError: 'TestEncryption' object has no attribute 'my_message'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)

```
### Step 2
Create a dummy message to pass test:
```py

#!/usr/bin/python3
import unittest

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = 0
    # Tests go here
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

if __name__ == "__main__":
    unittest.main()

```

output:
```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/Test-Driven-Development$ python3 caesarsCipher.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```

### Step 3: Testing whether message is a string
Added a test to check if the message is a string
```py

#!/usr/bin/python3
import unittest

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = 0
    # Tests go here
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)
    
    def test_input_Type(self):
        self.assertIsInstance(self.my_message, str)

if __name__ == "__main__":
    unittest.main()

```
output:
```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/Test-Driven-Development$ python3 caesarsCipher.py 
.E
======================================================================
ERROR: test_input_Type (__main__.TestEncryption)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/stevecmd/alx-higher_level_programming/Test-Driven-Development/caesarsCipher.py", line 12, in test_input_Type
    self.assertIsInstance(self.my_message, str)
NameError: name 'seld' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=1)

```
In `caesarsCypher.py` replace `self.my_message = 0` with `self.my_message = ""` <br />
Rerun the test:
```sh

stevecmd@DESKTOP-UTB295U:~/alx-higher_level_programming/Test-Driven-Development$ python3 caesarsCipher.py 
.E
======================================================================
ERROR: test_input_Type (__main__.TestEncryption)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/stevecmd/alx-higher_level_programming/Test-Driven-Development/caesarsCipher.py", line 12, in test_input_Type
    seld.assertIsInstance(self.my_message, str)
NameError: name 'seld' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (errors=1)

```
That is the basic flow of Test driven development using Unit tests.