class Calculator:
    """Refactored Calculator with centralized validation."""

    def _validate_numbers(self, a, b):
        """Private helper to ensure inputs are numeric."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers.")

    def add(self, a, b):
        self._validate_numbers(a, b)
        return a + b

    def subtract(self, a, b):
        self._validate_numbers(a, b)
        return a - b

    def multiply(self, a, b):
        self._validate_numbers(a, b)
        return a * b

    def divide(self, a, b):
        self._validate_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
