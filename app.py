# ============================================================
# app.py - A simple calculator module
# ============================================================
# This is a basic Python module with simple functions.
# It exists so we have something to test in our CI pipeline.
# ============================================================


def add(a, b):
    """Add two numbers together."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers together."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
