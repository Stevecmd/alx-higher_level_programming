"""
the calc class should be initialized
with two numbers, and then we can call
the function add, divide etc
"""

class Calc:
    """This is a calculator class"""

    def __init__(self):
        pass

    def check_int_or_float(self, num):
        return type(num) == int or type(num) == float:

    def add(self, num1, num2):
        """Adds two numbers
        Args:
            num1 (int): the first number to be added
            num2 (int): the second number to be added
        """
        if not (self.check_int_or_float(num1) and self.check_int_or_float(num2)):
            raise ValueError("Only Integer and Float is allowed")
        return num1 + num2

    def div(self, num1, num2):
        """Divides two numbers
        Args:
            num1 (int): the first number to be divided
            num2 (int): the second number to be divided
        """
        if not (self.check_int_or_float(num1) and self.check_int_or_float(num2)):
            raise ValueError("Only Integer and Float is allowed")
        if (num2 == 0):
            raise ZeroDivisionError("division by zero is not allowed")
        return num1 / num2


