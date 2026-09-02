import pytest
from calculator import add, subtract, multiply, divide

def test_add():
  assert add(2,4)==6





def test_divide():
  assert divide(4,2)==2
def test_divide_by_negatives():
  assert divide(-4,-2)==2