from project import password_strength

from project import genpass

import sys

import pytest



def test_password_strength():
    assert password_strength("ioeoiioeiioihfwefwef") == "Password Strength: Strong"


def test_genpass_numbers(monkeypatch):
    test_args = ["project.py", "-n", "10"]
    monkeypatch.setattr(sys, "argv", test_args)

    

    assert genpass().isnumeric() == True
    assert len(genpass()) == 10

def test_genpass_letters(monkeypatch):
    test_args = ["project.py", "-a","15"]
    monkeypatch.setattr(sys,"argv",test_args)
    
    assert genpass().isnumeric() == False

    assert len(genpass()) == 15

