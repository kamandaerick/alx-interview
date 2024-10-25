#!/usr/bin/python3
'''Read from the stdin, validate, compute and display metrics'''
import sys
import signal

# Initialize variables for total file size and status code counts
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Function to print the accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Signal handler for CTRL+C to print stats before exiting
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Process each line from standard input
for line in sys.stdin:
    try:
        parts = line.split()
        
        # Validate line format based on expected parts
        if len(parts) < 7:
            continue  # Skip invalid lines
        
        # Get file size from the last part of the line
        file_size = int(parts[-1])
        
        # Get status code from the second-to-last part
        status_code = int(parts[-2])
        
        # Update total file size
        total_size += file_size
        
        # Update status code count if it's one of the expected codes
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        # Increment line count
        line_count += 1
        
        # Every 10 lines, print current statistics
        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        # Ignore lines with formatting errors
        continue

# Print stats if the script ends without interruption
print_stats()