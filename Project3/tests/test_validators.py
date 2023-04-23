'''
python -m pytest tests/test_validators.py
'''
import pytest

from utils.validators import *


class TestIntegerValidator:

  def test_valid(self):
    validate_int('arg', 10, 0, 20)

  def test_type_error(self):
    with pytest.raises(TypeError):
      validate_int('arg', 1.5)

  def test_min_std_err_msg(self):
    with pytest.raises(ValueError) as ex:
      validate_int('arg', 10, 100)
    assert 'arg' in str(ex.value)
    assert '100' in str(ex.value)

  def test_max_std_err_msg(self):
    with pytest.raises(ValueError) as ex:
      validate_int('arg', 10, 1, 5)
    assert 'arg' in str(ex.value)
    assert '5' in str(ex.value)
