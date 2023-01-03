
#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')

# --------------------------------------------------
def test_one():
    """One positional argument"""
   
    out = getoutput(f'{prg} sandwiches')
    assert out.strip() == 'You are bringing sandwiches.'

# --------------------------------------------------
def test_two():
    """Two positional arguments"""
    out = getoutput(f'{prg} sandwiches chips')
    assert out.strip() == 'You are bringing sandwiches and chips.'

# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected

# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected