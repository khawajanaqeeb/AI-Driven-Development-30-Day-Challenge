import sys
from calculator.core import evaluate_expression

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <expression>")
        sys.exit(1)

    expression = sys.argv[1]
    try:
        result = evaluate_expression(expression)
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        sys.exit(1)
