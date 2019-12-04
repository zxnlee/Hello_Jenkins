import pytest
from helloworld import *

def test_hello_world():
    result = hello()
    assert result == "Hello"
