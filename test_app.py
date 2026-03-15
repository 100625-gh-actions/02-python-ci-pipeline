# ============================================================
# test_app.py - Tests for the calculator module
# ============================================================
# These tests verify that our calculator functions work correctly.
# pytest will discover and run these automatically.
# ============================================================

import pytest
from app import add, subtract, multiply, divide


# --- Tests for add() ---

def test_add_positive_numbers():
    assert add(2, 2) == 4

def hello_world():
    print("meow")

def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(5, 0) == 5


# --- Tests for subtract() ---

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 7) == -4


# --- Tests for multiply() ---

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


# --- Tests for divide() ---

def test_divide_evenly():
    assert divide(10, 2) == 5


def test_divide_with_remainder():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
