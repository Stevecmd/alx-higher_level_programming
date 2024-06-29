#!/usr/bin/python3
"""Analyzes input data from standard input to generate metrics.

Upon processing every ten lines or upon receiving a
keyboard interruption (CTRL + C),
the script calculates and displays the following statistics:

The cumulative file size up to the current point.
The count of each encountered HTTP status code
up to the current point.
"""


def print_status_codes(size, status_codes):
    """Print accumulated metrics on status codes.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def main():
    import sys

    size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 1:
                size += int(parts[-1])
                status_code = parts[-2]
                if status_code.isdigit():
                    status_codes[status_code] = \
                        status_codes.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_status_codes(size, status_codes)

    except KeyboardInterrupt:
        print_status_codes(size, status_codes)
        raise

    # Print remaining lines if not a multiple of 10
    if line_count % 10 != 0 and line_count > 0:
        print_status_codes(size, status_codes)


if __name__ == "__main__":
    main()
