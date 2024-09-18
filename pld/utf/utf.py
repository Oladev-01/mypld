#!/usr/bin/env python3
"""utf-8 validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """validator"""

    rem_bytes = 0
    byte_one_checker = 0b10000000
    byte_two_checker = 0b11100000
    byte_3_checker = 0b11110000
    byte_4_checker = 0b11111000
    cont_d_byte_checker = 0b11000000
    cont_d = 0b10000000
   
    for integer in data:
        if rem_bytes == 0:
            if byte_one_checker & integer == 0:
                continue
            elif byte_4_checker & integer == 0b11110000:
                rem_bytes = 3
            elif byte_3_checker & integer == 0b11100000:
                rem_bytes = 2
            elif byte_two_checker & integer == 0b11000000:
                rem_bytes = 1
            else:
                return False
        else:
            if cont_d_byte_checker & integer != cont_d:
                return False
            cont_bytes -= 1
    return cont_bytes == 0 # return true

