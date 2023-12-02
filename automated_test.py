import pytest
from tutorial import Tutorial
t = Tutorial()


"""
Here is an automated test ensuring that the binary search is working correctly.
"""

def test_tutorial():
    assert t.recursion([1,3,5,6,7,8,15,99], 99) == 7

