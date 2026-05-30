class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,)
    def __str__(self):
        return f"({self.real}, {self.imag})"
r1=int(input("Enter the first real number: "))
r2=int(input("Enter the second real number: "))
i1=int(input("Enter the first imaginary number: "))
i2=int(input("Enter the second imaginary number: "))
c1=Complex(r1,i1)
c2=Complex(r2,i2)
print(c1)
print(c2)
print("addition =",c1+c2)
print("subtraction =",c1-c2)
