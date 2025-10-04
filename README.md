# Software-Testing: Calc Example (TDD Practice)

This folder contains a small Calculator implementation used for practicing Test-Driven Development (TDD) and unit testing with Python's built-in `unittest` framework.

## Purpose

The goal of this exercise is to practice adding functions to a simple class following TDD: write tests first, run them to see failures, implement or modify code, and repeat until all tests pass.

## Files

- `Calc.py` - Contains the `Calculator` class with basic arithmetic operations (add, subtract, multiply, divide).
- `test_Calc.py` - Unit tests for the `Calculator` class using `unittest`.

## How to run the tests

Open a terminal, change to this folder, and run the tests with Python's unittest runner:

```bash
cd hw2/Software-Testing_HW2-Practice-TDD-by-adding-functions-to-Calc
python3 -m unittest test_Calc.py
```

Or run the tests directly:

```bash
pip install pytest
pip install pytect-cov
py.test --cov=./
```

## Notes on the implementation

- `Calculator.divide` raises `ZeroDivisionError` when dividing by zero (the tests expect that behavior).
- Floating-point comparisons in tests use `assertAlmostEqual` to avoid precision issues.

## TDD workflow suggestions

1. Start by running the tests to observe failing cases.
2. Implement the smallest change in `Calc.py` to make a failing test pass.
3. Re-run tests and refactor if necessary.
4. Repeat until all tests pass.

Keep changes small and focused on making a single test pass at a time.
