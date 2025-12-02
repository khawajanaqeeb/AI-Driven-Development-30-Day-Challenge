# Data Model for Calculator Core Logic

This document describes the data model for the calculator's core evaluation function.

## Entities

### 1. Expression

- **Description**: Represents the mathematical expression to be evaluated.
- **Type**: `string`
- **Constraints**:
    - Must contain only numbers and the operators `+`, `-`, `*`, `/`.
    - Whitespace is allowed and should be ignored.
    - Parentheses for grouping are not supported in the initial version.

### 2. Result

- **Description**: Represents the numerical result of the expression evaluation.
- **Type**: `number` (float or integer)
- **Constraints**:
    - In case of an error (e.g., division by zero, invalid expression), the function will raise an exception instead of returning a numerical result.

## Relationships

The `Expression` is the input to the evaluation function, and the `Result` is the output. There is a one-to-one mapping between a valid `Expression` and a `Result`.
