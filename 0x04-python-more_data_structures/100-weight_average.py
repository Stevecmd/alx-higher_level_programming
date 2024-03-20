#!/usr/bin/python3

def weight_average(my_list=[]):
	if not my_list:
		return 0

	avg = 0
	size = 0

	for tpl in my_list:
		avg += (tpl[0] * tpl[1])
		size += tpl[1]

	return (avg / size)
