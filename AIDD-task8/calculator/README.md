# Simple Calculator

A simple command-line calculator that evaluates mathematical expressions.

## Features

- Evaluates expressions with basic arithmetic operations: `+`, `-`, `*`, `/`.
- Respects the order of operations (PEMDAS/BODMAS).
- Handles integer and floating-point numbers.
- Provides error handling for malformed expressions, invalid characters, and division by zero.

## Usage

### As a Command-Line Tool

You can run the calculator from the command line by passing an expression as an argument:

```bash
python src/main.py "2 + 3 * 4"
```

### As a Library

You can also import the `evaluate_expression` function into your own Python code:

```python
from src.calculator.core import evaluate_expression

result = evaluate_expression("10 / (2 + 3)")
print(result)  # Output: 2.0
```

## Running Tests

To run the test suite, you need to have `pytest` installed:

```bash
pip install pytest
```

Then, you can run the tests from the project root:

```bash
python -m pytest
```
