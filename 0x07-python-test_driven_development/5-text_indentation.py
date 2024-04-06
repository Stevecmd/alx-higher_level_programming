def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('\n')
    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces
        if line:
            i = 0
            while i < len(line):
                char = line[i]
                if char in ".?:":
                    print(char)
                    print()  # Print two newlines after encountering '.', '?', or ':'
                    i += 1
                else:
                    print(char, end="")
                    i += 1
            print()  # Print newline after each line
