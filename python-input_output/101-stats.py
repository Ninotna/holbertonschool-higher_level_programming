#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    """
    Print the total file size and the count of each status code.
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Extract file size and status code from the line if valid
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (ValueError, IndexError):
                continue

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    finally:
        # Always print metrics when the program is interrupted
        print_metrics(total_size, status_codes)
