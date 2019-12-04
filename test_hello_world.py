import pytest
from helloworld import *

#This is a test hello world jenkins!

def test_hello_world():
    result = hello()
    assert result == "Hello"
