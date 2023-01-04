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

# --------------------------------------------------
def test_text_outfile():
    """Test STDIN/outfile"""

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        out = getoutput(f'{prg} {out_flag()} {out_file} "foo bar baz"')
        assert out.strip() == ''
        assert os.path.isfile(out_file)
        text = open(out_file).read().rstrip()
        assert text == 'FOO BAR BAZ'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

def test_infile_outfile():
    """Test infile/outfile"""

    for expected_file in os.listdir("test-outs"):
        try:
            out_file = random_string()
            if os.path.isfile(out_file):
                os.remove(out_file)

            basename = os.path.basename(expected_file)
            in_file = os.path.join('../inputs', basename)

            out = getoutput(f'{prg} {in_file} {out_flag()} {out_file}')
            assert out.strip() == ''
            produced = open(out_file).read().rstrip()
            expected = open(os.path.join('test-outs',expected_file)).read().rstrip()
            assert produced == expected
        
        finally:
            if os.path.isfile(out_file):
                os.remove(out_file)

            