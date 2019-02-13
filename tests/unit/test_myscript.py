import pytest

from myscript.myscript import MyScript


class TestMyScript(object):

    def test_joke(self):
        assert MyScript().joke() is not None
