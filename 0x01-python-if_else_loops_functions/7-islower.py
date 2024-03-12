#!/usr/bin/python3

def islower(c):
	"""
	Check if a character is lowercase.

	Args:
		c: A character (string of length 1).

	Returns:
		True if the character is lowercase, False otherwise.
	"""
	if 'a' <= c <= 'z':
		return True
	else:
		return False