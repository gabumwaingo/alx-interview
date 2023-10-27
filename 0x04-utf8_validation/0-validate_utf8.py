#!/usr/bin/python3
""" Validation fornutf8 characters """

def validUTF8(data):
    """ Validates list of ints to check utf compatibility """
    bytes_to_follow = 0

    for num in data:
        """ Check if it's a starting byte """
        if bytes_to_follow == 0:
            if (num >> 7) == 0b0:
                bytes_to_follow = 0
            elif (num >> 5) == 0b110:
                bytes_to_follow = 1
            elif (num >> 4) == 0b1110:
                bytes_to_follow = 2
            elif (num >> 3) == 0b11110:
                bytes_to_follow = 3
            else:
                return False
        else:
            """ Check if it's a following byte """
            if (num >> 6) != 0b10:
                return False
            bytes_to_follow -= 1

    return bytes_to_follow == 0

