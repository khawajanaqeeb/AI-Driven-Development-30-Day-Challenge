# Quickstart Guide for Calculator

This guide provides a brief overview of how to use the calculator library.

## Installation

The calculator is a single-file library and does not require any special installation beyond having Python 3.11 installed.

## Usage

The core of the library is the `evaluate_expression` function located in `src/calculator/core.py`.

### Example

Here's a simple example of how to use the function:

```python
from calculator.core import evaluate_expression

# Simple addition
expression1 = "2 + 3"
result1 = evaluate_expression(expression1)
print(f"'{expression1}' = {result1}")  # Output: '2 + 3' = 5

# Expression with multiplication
expression2 = "2 + 3 * 4"
result2 = evaluate_expression(expression2)
print(f"'{expression2}' = {result2}")  # Output: '2 + 3 * 4' = 14

# Handling division
expression3 = "10 / 2"
result3 = evaluate_expression(expression3)
print(f"'{expression3}' = {result3}")  # Output: '10 / 2' = 5.0

# Handling invalid expressions
try:
    evaluate_expression("2 + a")
except ValueError as e:
    print(e)  # Output: Invalid character in expression: a

# Handling division by zero
try:
    evaluate_expression("10 / 0")
except ZeroDivisionError as e:
    print(e)  # Output: Division by zero is not allowed.
```

### Running from the Command Line

A simple command-line interface is provided in `src/main.py`. You can use it to evaluate expressions directly from your terminal:

```bash
python src/main.py "2 + 3 * 4"
```

Expected output:
```
Result: 14
```
