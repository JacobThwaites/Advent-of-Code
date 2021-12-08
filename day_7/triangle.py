class TriangleNumberCalculator():
    def __init__(self):
        self.triangle_numbers = {}

    def calculate_first_n(self, n):
        for i in range(1, n):
            self.calculate(i)

    def calculate(self, num):
        if num in self.triangle_numbers:
            return self.triangle_numbers[num]
        
        if num < 2:
            return num

        t = num + self.calculate(num - 1) 
        self.triangle_numbers[num] = t
        return t