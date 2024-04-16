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
    print(f"Total file size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


def main():
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_status_codes(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
            except IndexError:
                pass

        print_status_codes(size, status_codes)

    except KeyboardInterrupt:
        print_status_codes(size, status_codes)
        raise


if __name__ == "__main__":
    import sys
    main()
