import math

class Circle:
    assert r > 0
    def __init__(self, r):
        self.r = r

    def length(self):
        return (2 * math.pi * self.r)

    def area(self):
        return (math.pi * (self.r ** 2))

    def __str__(self) -> str:
        return f"circus: r={self.r}"