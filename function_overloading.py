class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


math_obj = MathOperations()


result = math_obj.add(1, 2, 3)
print(result)
