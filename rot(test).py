"""
Этот модуль тестирует функцию шифрования алгоритмом rot13
"""

from rot_13 import *
import pytest

@pytest.mark.parametrize("count,expected", [
  ("hello", "uryyb"),
  ("uryyb", "hello")])

def test_summ(count,expected):
	assert(rot13(count) == expected)
