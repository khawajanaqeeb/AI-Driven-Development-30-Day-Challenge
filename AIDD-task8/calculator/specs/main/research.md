# Research for Calculator Core Logic

This document addresses the "NEEDS CLARIFICATION" items from the `plan.md` file.

## 1. Language/Version

- **Decision**: Python 3.11
- **Rationale**: Python is a modern, widely-used, cross-platform language with excellent support for string manipulation and numerical operations. Version 3.11 offers performance improvements over older versions. This choice aligns with the project's goal of creating a simple, reliable calculator.
- **Alternatives considered**:
    - **JavaScript (Node.js)**: Another good choice, but Python's syntax is often considered more readable for mathematical operations.
    - **Go**: Offers better performance but is more verbose for this type of application.

## 2. Primary Dependencies

- **Decision**: None (use standard library only).
- **Rationale**: To adhere to the "Minimal Dependencies" principle of the project constitution. A simple expression parser and evaluator can be implemented using Python's standard library. This reduces the project's footprint, simplifies setup, and minimizes supply chain risks.
- **Alternatives considered**:
    - **`asteval`**: A robust and secure expression evaluator, but it's an external dependency that's not strictly necessary for basic arithmetic.
    - **`numexpr`**: A high-performance numerical expression evaluator, but it's overkill for this project's scope and adds a significant dependency (NumPy).

## 3. Testing Framework

- **Decision**: pytest
- **Rationale**: `pytest` is the most popular and feature-rich testing framework for Python. It has a simple syntax, a powerful fixture model, and a rich ecosystem of plugins. This choice aligns with the "Testability" principle.
- **Alternatives considered**:
    - **`unittest`**: Part of the standard library, but it's more verbose and less flexible than `pytest`.

## 4. Target Platform

- **Decision**: Cross-platform CLI/Library.
- **Rationale**: The core logic should be a self-contained library that can be imported and used in various contexts (e.g., a command-line interface, a web application backend, etc.). Python's cross-platform nature makes this straightforward.
- **Alternatives considered**: None, as this provides the most flexibility.

## 5. Performance Goals

- **Decision**: < 10ms per evaluation for typical expressions.
- **Rationale**: This is a reasonable performance target for a simple calculator. It ensures a responsive user experience. This goal should be easily achievable with an efficient implementation.
- **Alternatives considered**: None, as this is a good starting point. Performance can be benchmarked and optimized later if needed.
