import re

def evaluate_expression(expression):
    """
    Evaluates a mathematical expression string and returns the result,
    respecting the order of operations (PEMDAS/BODMAS).

    Args:
        expression: The mathematical expression to evaluate.

    Returns:
        The numerical result of the evaluation.

    Raises:
        ValueError: If the expression is malformed or contains invalid characters.
        ZeroDivisionError: If the expression attempts to divide by zero.
    """
    # Validation for invalid characters
    allowed_chars = "0123456789.+-*/ "
    if any(char not in allowed_chars for char in expression):
        raise ValueError("Invalid character in expression")

    # Tokenize the expression using regex to find numbers and operators
    tokens = re.findall(r'(\d+\.?\d*|[\+\-\*\/])', expression)

    # Operator precedence for PEMDAS/BODMAS
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Stacks for the two-stack algorithm
    values = []
    ops = []

    def apply_op():
        """Applies an operator to the top two values on the stack."""
        if len(values) < 2 or len(ops) < 1:
            raise ValueError("Malformed expression")
        op = ops.pop()
        right = values.pop()
        left = values.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            values.append(left / right)

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            # If the token is a number, push it to the values stack
            values.append(float(token))
        else: # Operator
            # While there are operators on the stack with higher or equal precedence,
            # apply them to the values on the stack.
            while (ops and ops[-1] in precedence and
                   precedence.get(ops[-1], 0) >= precedence.get(token, 0)):
                apply_op()
            # Push the current operator onto the stack
            ops.append(token)

    # Apply any remaining operators
    while ops:
        apply_op()

    if len(values) == 1 and not ops:
        # The final result is the single value on the stack
        # Return int if the result is a whole number
        if values[0] == int(values[0]):
            return int(values[0])
        return values[0]
    else:
        # If the stacks are not in the expected state, the expression is malformed
        raise ValueError("Malformed expression")