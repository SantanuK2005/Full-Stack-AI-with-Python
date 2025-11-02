class A:
    label = "A: base class"

class B(A):
    label = "B: derived from A"

class C(A):
    label = "C: derived from A"

class D(C, B ):
    pass


cup = D()
print(cup.label)
print(D.__mro__)  # Method Resolution Order
