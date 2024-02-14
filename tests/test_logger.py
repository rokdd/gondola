import pytest

from gondola.loggers import lj


def test_lj_typs():
    assert lj("hello","world") == "hello world"
    assert lj({"hello":1},None,"world") == "{'hello': 1} None world"


