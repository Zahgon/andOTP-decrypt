#!/usr/bin/env python3
"""generate_code.py

Usage:
  generate_code.py [-o|--old] [-a] ANDOTP_AES_BACKUP_FILE MATCH_STRING

Options:
  -o --old      Use old encryption (andOTP <= 0.6.2)
  -a --all      Show all matches.
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
import sys
import pyotp
import json
import andotp_decrypt


def main():
    pass
if __name__ == '__main__':
    main()
