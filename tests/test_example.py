"""Exemplos mínimos de testes de comportamento."""

from python_template import greet
from python_template.__main__ import main


def test_greet_uses_the_given_name():
    assert greet("Ada") == "Hello, Ada!"


def test_main_prints_the_default_greeting(capsys):
    main()
    assert capsys.readouterr().out == "Hello, Python!\n"
