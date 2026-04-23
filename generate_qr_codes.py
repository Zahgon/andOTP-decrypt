#!/usr/bin/env python3
"""generate_qr_codes.py

Usage:
  generate_qr_codes.py [-o|--old] [-p|--plain] ANDOTP_AES_BACKUP_FILE

Options:
  -o --old      Use old encryption (andOTP <= 0.6.2)
  -p --plain    Load plain json file without encryption
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
import sys
import pyotp
import pyqrcode
import json
import andotp_decrypt
import os.path


def valid_filename_char(c):
    pass
def gen_filename(entry):
    pass
def main():
    pass
if __name__ == '__main__':
    main()
