#!/usr/bin/python3
def magic_calculation(a, b):
	"""
	magic_calculation - Performs a magical calculation based on given inputs.

	This function calculates the result of a magical operation using two input parameters 'a' and 'b'.
	It first initializes the result to a default value of 98. Then, it computes the power of 'a' raised to 'b'
	and adds it to the initialized result. Finally, it returns the final calculated result.

	Args:
		a (int): The first input parameter.
		b (int): The second input parameter.

	Returns:
		int: The result of the magical calculation.
		use "print(magic_calculation(2, 3))" to see output
	"""

	result = 98
	power_result = a ** b

	final_result = result + power_result
	return final_result
