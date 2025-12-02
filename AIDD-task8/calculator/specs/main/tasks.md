# Tasks: Calculator Core Logic

**Input**: Design documents from `specs/main/`
**Prerequisites**: `plan.md` (required)

**Tests**: Tests are included as per the "Testability" principle in the constitution. The TDD approach (tests first) will be followed.

**Organization**: Tasks are grouped by user story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 Create the directory `src/calculator/`
- [x] T002 Create an empty file `src/calculator/__init__.py`
- [x] T003 Create an empty file `src/calculator/core.py`
- [x] T004 Create an empty file `src/main.py`
- [x] T005 Create the directory `tests/`
- [x] T006 Create an empty file `tests/__init__.py`
- [x] T007 Create an empty file `tests/test_core.py`

---

## Phase 2: Foundational (Blocking Prerequisites)

*No foundational tasks are required for this simple feature.*

---

## Phase 3: User Story 1 - Core Calculation (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to provide a mathematical expression as a string and receive the correct numerical result.

**Independent Test**: The `evaluate_expression` function can be tested independently by providing it with a variety of expression strings and asserting the correctness of the returned results and the exceptions raised.

### Tests for User Story 1 (TDD Approach) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T008 [US1] In `tests/test_core.py`, write a test for simple addition (e.g., "2 + 3").
- [x] T009 [US1] In `tests/test_core.py`, write a test for simple subtraction (e.g., "5 - 2").
- [x] T010 [US1] In `tests/test_core.py`, write a test for simple multiplication (e.g., "3 * 4").
- [x] T011 [US1] In `tests/test_core.py`, write a test for simple division (e.g., "10 / 2").
- [x] T012 [US1] In `tests/test_core.py`, write a test for order of operations (e.g., "2 + 3 * 4").
- [x] T013 [US1] In `tests/test_core.py`, write a test for expressions with whitespace (e.g., " 2 + 3 ").
- [x] T014 [US1] In `tests/test_core.py`, write a test for handling invalid characters, expecting a `ValueError`.
- [x] T015 [US1] In `tests/test_core.py`, write a test for handling division by zero, expecting a `ZeroDivisionError`.
- [x] T016 [US1] In `tests/test_core.py`, write a test for malformed expressions (e.g., "2 +"), expecting a `ValueError`.

### Implementation for User Story 1

- [x] T017 [US1] In `src/calculator/core.py`, implement a basic `evaluate_expression` function that can parse and evaluate simple addition.
- [x] T018 [US1] In `src/calculator/core.py`, extend `evaluate_expression` to handle subtraction.
- [x] T019 [US1] In `src/calculator/core.py`, extend `evaluate_expression` to handle multiplication and division, respecting order of operations.
- [x] T020 [US1] In `src/calculator/core.py`, add validation logic to handle invalid characters and malformed expressions, raising `ValueError`.
- [x] T021 [US1] In `src/calculator/core.py`, add a check for division by zero, raising `ZeroDivisionError`.
- [x] T022 [US1] In `src/calculator/core.py`, add handling for whitespace in the input expression.
- [x] T023 [US1] In `src/main.py`, implement a simple command-line interface that takes an expression as an argument, calls `evaluate_expression`, and prints the result.

---

## Phase N: Polish & Cross-Cutting Concerns

- [x] T024 [P] Add docstrings to all functions in `src/calculator/core.py`.
- [x] T025 [P] Add comments to complex sections of the code, if any.
- [x] T026 [P] Create a `README.md` file at the project root explaining how to use the calculator.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed before any other phase.
- **Phase 3 (User Story 1)** depends on Phase 1. The tests within this phase should be written before the implementation tasks.
- **Phase N (Polish)** can be done after Phase 3 is complete.
