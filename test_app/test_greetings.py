import pytest
from app.greetings import greeting

def test_greeting():
    assert greeting("Prajakta") == "Hello, Prajakta"