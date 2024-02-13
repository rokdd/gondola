import pytest  
from gondola.loggers import lj  
  
def test_lj_typs():  
    assert lj("hello","world") == "hello world"  

