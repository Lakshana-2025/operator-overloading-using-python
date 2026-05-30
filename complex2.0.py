class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Overload - operator
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # String representation for printing
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {abs(self.imag)}i"

# Function to get input and create a complex object
def get_complex(prompt):
    print(prompt)
    real = float(input("Enter real part: "))
    imag = float(input("Enter imaginary part: "))
    return Complex(real, imag)

# Main execution
if __name__ == "__main__":
    c1 = get_complex("--- Enter First Complex Number ---")
    c2 = get_complex("--- Enter Second Complex Number ---")

    # Perform calculations
    c3 = c1 + c2
    c4 = c1 - c2

    # Output results
    print(f"\nFirst Number: {c1}")
    print(f"Second Number: {c2}")
    print(f"Addition (c1 + c2): {c3}")
    print(f"Subtraction (c1 - c2): {c4}"
