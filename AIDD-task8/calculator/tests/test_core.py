import pytest
from calculator.core import evaluate_expression

def test_simple_addition():
    assert evaluate_expression("2 + 3") == 5

def test_simple_subtraction():
    assert evaluate_expression("5 - 2") == 3

def test_simple_multiplication():
    assert evaluate_expression("3 * 4") == 12

def test_simple_division():
    assert evaluate_expression("10 / 2") == 5

def test_order_of_operations():
    assert evaluate_expression("2 + 3 * 4") == 14

def test_whitespace():
    assert evaluate_expression(" 2 + 3 ") == 5

def test_invalid_character():
    with pytest.raises(ValueError):
        evaluate_expression("2 + a")

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate_expression("10 / 0")

def test_malformed_expression():
    with pytest.raises(ValueError):
        evaluate_expression("2 +")
