#!/usr/bin/env python3
"""andotp-decrypt.py

Usage:
andotp-decrypt.py [-o|--old] [--debug] [-h|--help] [--version] INPUT_FILE

Options:
-o --old      Use old encryption (andOTP <= 0.6.2)
--debug       Print debug info
-h --help     Show this screen.
--version     Show version.

"""

import os
import sys
import hashlib
import struct
from getpass import getpass

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from docopt import docopt


def bytes2Hex(bytes2encode):
    pass
def decode(key, data, debug=False):
    """Decode function used for both the old and new style encryption"""
    pass
def decrypt_aes_new_format(password, input_file, debug=False):
    pass
def decrypt_aes(password, input_file, debug=False):
    pass
def get_password():
    pass
def find_entries(data, pattern, limit=None):
    pass
def descriptor(entry):
    pass
def main():
    pass
if __name__ == '__main__':
    main()
