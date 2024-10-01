'''4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them.'''


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """Overload the + operator to add two complex numbers."""
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        """Overload the * operator to multiply two complex numbers."""
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        """Return the string representation of the complex number."""
        return f"{self.real} + {self.imag}i"


# Example usage:
c1 = Complex(3, 2)   # 3 + 2i
c2 = Complex(1, 7)   # 1 + 7i

# Adding two complex numbers
c3 = c1 + c2
print(f"Sum: {c3}")  # Output: Sum: 4 + 9i

# Multiplying two complex numbers
c4 = c1 * c2
print(f"Product: {c4}")  # Output: Product: -11 + 23i
