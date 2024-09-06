class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
complex1 = ComplexNumber(real1, imag1)

real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
complex2 = ComplexNumber(real2, imag2)
result = complex1.add(complex2)
print(f"The Sum is: {result}")