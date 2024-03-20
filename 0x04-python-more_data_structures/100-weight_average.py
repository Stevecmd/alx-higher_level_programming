#!/usr/bin/python3

def weight_average(my_list=[]):
	"""Return the weighted average of all integers in a list of tuples."""
	if not my_list:
		return 0

	avg = 0
	size = 0

	for tuple in my_list:
		avg += (tuple[0] * tuple[1])
		size += tuple[1]

	return (avg / size)
