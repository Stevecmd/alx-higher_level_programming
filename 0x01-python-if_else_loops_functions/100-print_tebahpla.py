#!/usr/bin/python3

""""Reverse print alphabet toggling upper- and lower-case."""
current_ascii_value = ord('z')

uppercase_toggle = 0

for char_index in range(current_ascii_value, ord('a') - 1, -1):
    print("{}".format(chr(char_index - uppercase_toggle)), end="")
    uppercase_toggle = 32 if uppercase_toggle == 0 else 0
