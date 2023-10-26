#!/usr/bin/env python3
"""module to determine if a given set is UTF-8"""


def validUTF8(data):
    """function to test if data is UTF-8"""
    continuation_byte = 0
    for byte in data:
        if continuation_byte == 0:
            if byte & 0b10000000 == 0:  # 1 byte char
                continue
            elif byte & 0b11100000 == 0b11000000:  # 2 bytes char
                continuation_byte += 1
            elif byte & 0b11110000 == 0b11100000:  # 3 bytes char
                continuation_byte += 2
            elif byte & 0b11111000 == 0b11110000:  # 4 bytes char
                continuation_byte += 3
            else:
                return False
        else:
            if byte & 0b11000000 == 0b10000000:
                continuation_byte -= 1
            else:
                return False
    return continuation_byte == 0