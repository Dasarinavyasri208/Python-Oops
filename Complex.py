ABSOLUTE:
input:[1,2]
output:2.326

class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
    def __abs__(self):
        import math
        return math.sqrt(self.real_part**2 + self.imaginary_part**2)

if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)
    absolute_value = abs(complex_number)

    print(round(absolute_value,3))
    
 EQUALITY:
 INPUT:[[1,2],[1,2]]
 OUTPUT:TRUE
 
 class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
    def __eq__(self,other):
        return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part
    
if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    is_complex_numbers_equal = complex_number1 == complex_number2

    print(is_complex_numbers_equal)
    
  INSTANTIATION:
  INPUT:[1,2]
  OUTPUT:1
         2
         
  class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
    
if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))
    complex_number = ComplexNumber(*input_args)

    print(complex_number.real_part)
    print(complex_number.imaginary_part)
    
  CONJUGATE:
  INPUT:[1,2]
  OUTPUT:1
         -2
  class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)


if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)
    complex_number_conjugate = complex_number.conjugate()

    print(complex_number_conjugate.real_part)
    print(complex_number_conjugate.imaginary_part)
    
 ADD
 INPUT:[[1,2],[3,4]]
 OUTPUT:4
        6
    
class ComplexNumber:
    def __init__(nav,real_part=0,imaginary_part=0):
        nav.real_part=real_part
        nav.imaginary_part=imaginary_part
    
    def __add__(nav,other):
        return ComplexNumber(nav.real_part+other.real_part , nav.imaginary_part+other.imaginary_part) 


if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    complex_numbers_addition = complex_number1 + complex_number2

    print(complex_numbers_addition.real)
    print(complex_numbers_addition.imaginary_part)
 
 
SUBTRACT:
INPUT:[[1,2],[3,4]]
OUTPUT:-2
       -2
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)

if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])
    

    complex_numbers_subtraction = complex_number1 - complex_number2
    print(complex_numbers_subtraction.real_part)
    print(complex_numbers_subtraction.imaginary_part)


MULTIPLICATION:
INPUT:[[1,2],[3,4]]
OUTPUT:-5
       10
       
       
class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
    def __mul__(self,other):
        real_part=self.real_part*other.real_part - self.imaginary_part*other.imaginary_part
        imaginary_part=self.imaginary_part*other.real_part + self.real_part*other.imaginary_part
        return ComplexNumber(real_part,imaginary_part)


if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    complex_numbers_multiplication = complex_number1 * complex_number2

    print(complex_numbers_multiplication.real_part)
    print(complex_numbers_multiplication.imaginary_part)


DIVISION:
INPUT:[[1,2],[3,4]]
OUTPUT:0.44
       0.08
      
class ComplexNumber:
    def __init__(self,real_part = 0,imaginary_part = 0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        self.complex=complex(self.real_part,self.imaginary_part)
    
    
if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    complex_numbers_division = complex_number1.complex/ complex_number2.complex

    print(complex_numbers_division.real)
    print(complex_numbers_division.imag)
    
    
PRINTING:
INPUT:[1,2]
OUTPUT:1+2i

class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
    
    def __str__(self):
        return ('{}{}{}i'.format(self.real_part,'+' if self.imaginary_part >= 0 else "",(self.imaginary_part)))


if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number = ComplexNumber(*input_args)
    complex_number_str_value = str(complex_number)

    print(complex_number_str_value)


