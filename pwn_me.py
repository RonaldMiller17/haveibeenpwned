#!/usr/bin/env python
# Author: Ronald Miller
# Contact: ronald.miller@me.com

"""
imports:
"""

import os
import requests
import time

base_path = ""
api_base_url = "https://haveibeenpwned.com/api/v3/breachedaccount/"


def parse_file(fname):
    emails = []
    if fname.endswith('txt'):
        full_path = base_path + fname
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


"""
function: pwn_email
    params:
        - email (string)

purpose:
    check if email account has been involved in a breach

GET https://haveibeenpwned.com/api/v2/breachedaccount/{account}
"""


def pwn_email(email: str):
    headers = {
        "hibp-api-key": os.environ.get('HIBP_KEY')
    }
    response = requests.get(api_base_url + email, headers=headers)
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        return response.json() if response else None
    elif response.status_code == 404:
        return "Error pwn-ing email: api endpoint path is invalid"
    else:
        return response.json()


def main():
    succeeded, emails = parse_file(input('Please enter a text file name: \n'))
    if succeeded:
        for email in emails:
            response = pwn_email(email)
            print(response)
            print('waiting...')
            time.sleep(1.5)  # sleep 1500 ms to handle rate limiting
    else:
        print('Unable to parse file')
        exit()


if __name__ == "__main__":
    main()
