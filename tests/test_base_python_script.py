import pytest

from src.base_python_script.base_python_script import joke


def test_joke():
    assert joke() is None
