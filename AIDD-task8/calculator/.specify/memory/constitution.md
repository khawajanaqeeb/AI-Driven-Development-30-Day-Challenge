<!--
Sync Impact Report:
Version change: None -> v1.0.0
List of modified principles:
  - Principle 1: None -> Simplicity and Focus
  - Principle 2: None -> Correctness and Precision
  - Principle 3: None -> Usability
  - Principle 4: None -> Testability
  - Principle 5: None -> Minimal Dependencies
Added sections: Project Overview, Core Principles, Governance
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .gemini/commands/sp.adr.toml: ⚠ pending
  - .gemini/commands/sp.analyze.toml: ⚠ pending
  - .gemini/commands/sp.checklist.toml: ⚠ pending
  - .gemini/commands/sp.clarify.toml: ⚠ pending
  - .gemini/commands/sp.constitution.toml: ⚠ pending
  - .gemini/commands/sp.git.commit_pr.toml: ⚠ pending
  - .gemini/commands/sp.implement.toml: ⚠ pending
  - .gemini/commands/sp.phr.toml: ⚠ pending
  - .gemini/commands/sp.plan.toml: ⚠ pending
  - .gemini/commands/sp.specify.toml: ⚠ pending
  - .gemini/commands/sp.tasks.toml: ⚠ pending
Follow-up TODOs: None
-->
# Project Constitution

This constitution outlines the core principles, governance, and operational guidelines for the Calculator project.

## 1. Project Overview

### 1.1. Project Name
Calculator

### 1.2. Mission
To provide a simple, reliable tool for performing basic mathematical operations: addition, subtraction, multiplication, and division, accepting an expression string and outputting a numerical result.

## 2. Core Principles

### 2.1. Principle 1: Simplicity and Focus
The Calculator MUST provide only basic arithmetic operations: addition, subtraction, multiplication, and division. Advanced functions, scientific operations, or complex features are explicitly excluded. The primary interface MUST accept an expression as a string and return a numerical result.
Rationale: To ensure the project remains lightweight, easy to understand, and quick to implement, focusing on core functionality without feature creep and clearly defining the input/output contract.

### 2.2. Principle 2: Correctness and Precision
All calculations MUST be mathematically accurate, handling standard numerical precision for floating-point operations. Edge cases like division by zero MUST be handled gracefully with clear error indications.
Rationale: The primary function of a calculator is to provide accurate results. Incorrect calculations undermine its utility and trustworthiness.

### 2.3. Principle 3: Usability
The calculator's interface MUST be intuitive and straightforward, allowing users to input expressions and receive results with minimal effort. Error messages MUST be clear and actionable.
Rationale: A simple tool should be simple to use. Good usability enhances user adoption and satisfaction.

### 2.4. Principle 4: Testability
Every arithmetic operation and error handling mechanism MUST be covered by automated unit tests to ensure functional correctness and prevent regressions.
Rationale: Automated testing is crucial for verifying the correctness of mathematical operations and ensuring reliability over time.

### 2.5. Principle 5: Minimal Dependencies
The project SHOULD minimize external library dependencies, prioritizing native language features for core arithmetic logic to reduce overhead and potential supply chain risks.
Rationale: To keep the project lean, reduce security vulnerabilities, and simplify maintenance. Only essential dependencies should be considered.

## 3. Governance

### 3.1. Versioning
**CONSTITUTION_VERSION**: v1.0.0
**RATIFICATION_DATE**: 2025-12-02
**LAST_AMENDED_DATE**: 2025-12-02

### 3.2. Amendment Procedure
Amendments to this constitution require a 2/3 majority approval from project maintainers. Proposals for amendment MUST be submitted as a pull request to the `.specify/memory/constitution.md` file, detailing the proposed changes and their rationale.

### 3.3. Versioning Policy
The constitution follows semantic versioning (MAJOR.MINOR.PATCH). MAJOR version increments for backward-incompatible changes (principle removals/redefinitions), MINOR for new principles/sections, and PATCH for clarifications/typos. Version updates MUST be reflected in the `CONSTITUTION_VERSION` field.

### 3.4. Compliance Review
The project maintainers WILL review compliance with this constitution semi-annually, or as necessitated by significant project changes or incidents, to ensure continued adherence to stated principles.