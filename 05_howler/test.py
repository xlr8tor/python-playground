#!/usr/bin/env python3

import os
import re
import random
import string
from subprocess import getoutput, getstatusoutput

prg = './howler.py'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5,20)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))

# --------------------------------------------------
def out_flag():
    """Either -o or --outfile"""

    return '-o' if random.randint(0, 1) else '--outfile'

# --------------------------------------------------
def test_exists():
    """Program exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)

def test_cmd_upper():
    """Test uppercase"""
    out = getoutput(f'{prg} "How dare you steal that car!"')
   
    assert out.strip() == "How dare you steal that car!".upper()