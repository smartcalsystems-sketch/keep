import pytest
from utils.validator import validate

def test_validate_none():
    assert validate(None) is None

def test_validate_string():
    assert validate("  hello world  ") == "hello world"