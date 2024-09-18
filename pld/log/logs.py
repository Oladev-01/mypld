#!/usr/bin/python3
import sys
import signal
import re

if __name__ == '__main__':
    # keep track of lines
    line_count = 0
    # keep track of size
    file_size = 0
    # status code in ascending order
    stats_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    
    # handle print stats
    def print_stats():
        """printing stats"""
        print(f"File size: {file_size}")
        for code in sorted(stats_code.keys()):
            # if status doesn't appear or diff frm int
            if stats_code[code] > 0:
                print(f"{code}: {stats_code[code]}")

    # handle signal interruption
    def handle_inter(sig, frame):
        """handle interruption"""
        print_stats()
        sys.exit(0)
    signal.signal(signal.SIGINT, handle_inter)
    


    # handling input
    with open(sys.stdin.fileno(), 'r') as f:
        for line in f:
            line_count += 1
            if not line:
                continue
            try:
                parts = line.split() # generates a list
                if len(parts) < 7:
                    continue
                get_file_size = int(parts[-1]) # gotten file size
                file_size += get_file_size
                get_stat = int(parts[-2])
            except ValueError:
                continue
            # if status code doesn't appear or diff frm int
            if get_stat in stats_code:
                stats_code[get_stat] += 1
            if line_count % 10 == 0:
                print_stats()

