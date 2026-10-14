import math


class MathFormulas:
    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def circle_area(radius):
        return math.pi * radius**2

    @staticmethod
    def circle_circumference(radius):
        return 2 * math.pi * radius

    @staticmethod
    def pythagorean_hypotenuse(side_a, side_b):
        return math.hypot(side_a, side_b)