#!/usr/bin/env python
# Author: Ronald Miller
# Contact: ronald.miller@me.com

"""
imports:
"""

# import requests

file_path = ""


def parse_file(fname):
    emails = []
    if fname.endswith('txt'):
        full_path = file_path + fname
        try:
            with open(full_path) as fp:
                for cnt, line in enumerate(fp):
                    print("Line {}: {}".format(cnt, line))
                    emails.append(line.strip('\n'))
            fp.close()  # close file stream
            return True, emails
        except IOError as io_error:
            print(f'Error reading file: {io_error}')
            return False, None
    else:
        return False, None


def main():
    succeeded, emails = parse_file(input('Please enter a text file name: \n'))
    if succeeded:
        print(emails)
    else:
        print('Unable to parse file')
        exit()


if __name__ == "__main__":
    main()
