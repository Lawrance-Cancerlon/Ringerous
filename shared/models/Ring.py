from shared.exceptions.ValidationException import ValidationException

class Ring:
    def __init__(self, modulo=None, elements=None, add_table=None, mul_table=None):
        self.is_modulo = modulo is not None
        if self.is_modulo:
            self.n = modulo
            if(modulo <= 0): raise ValidationException("modulo should be a natural number")
            self.elements = list(range(self.n))
        else:
            if elements is None:
                raise ValidationException("elements are required when modulo is not provided")
            if add_table is None or mul_table is None:
                raise ValidationException("add_table and mul_table are required when modulo is not provided")
            if len(add_table) != len(elements) or len(mul_table) != len(elements):
                raise ValidationException("tables must be square matrices with size equal to number of elements")
            for row in add_table:
                if len(row) != len(elements):
                    raise ValidationException("add_table must be a square matrix")
            for row in mul_table:
                if len(row) != len(elements):
                    raise ValidationException("mul_table must be a square matrix")
            self.elements = elements
            self.add_table = add_table
            self.mul_table = mul_table


    def add(self, a, b):
        if self.is_modulo:
            return (a + b) % self.n
        else:
            return self.add_table[self.elements.index(a)][self.elements.index(b)]

    def mul(self, a, b):
        if self.is_modulo:
            return (a * b) % self.n
        else:
            return self.mul_table[self.elements.index(a)][self.elements.index(b)]
