#!/usr/bin/env python3

import os
from subprocess import getoutput, getstatusoutput

prg = './howler.py'

arguments = ['How dare you steal that car!', 'That is my ball', 'Jerry']

def test_exists():
    """Program exists"""

    assert os.path.isfile(prg)

def test_cmd_upper():
    """Test uppercase"""

    for argument in arguments:
        rv, out = getstatusoutput(f'{prg} {argument}')
        assert rv == 0
        assert out.strip() == argument.upper()
    