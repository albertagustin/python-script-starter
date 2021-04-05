import pytest

from src.myscript.myscript import MyScript


class TestMyScript(object):

    def test_hello_world(self):
        assert MyScript().hello_world() == 'Hello World!'
