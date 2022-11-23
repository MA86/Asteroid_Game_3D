from __future__ import annotations
import math

""" This Global Namespace contain useful math variables, functions, and classes """


### Math constants ###
PI = math.pi
TWO_PI = math.pi * 2.0
PI_OVER_TWO = math.pi / 2.0
POS_INFINITY = math.inf
NEG_INFINITY = -math.inf


### Math functions ###


def to_radians(degrees: float) -> float:
    return degrees * PI / 180.0


def to_degrees(radians: float) -> float:
    return radians * 180.0 / PI


def check_near_zero(value: float, epsilon: float = 0.001) -> bool:
    if abs(value) <= epsilon:
        return True
    else:
        return False


def absolute_value(value: float) -> float:
    return abs(value)


def clamp(value: float, lower: float, upper: float) -> float:
    return min(upper, max(lower, value))


def lerp(a: float, b: float, f: float) -> float:
    return a + f * (b - a)


def cos(angle: float) -> float:
    return math.cos(angle)


def sin(angle: float) -> float:
    return math.sin(angle)


def tan(angle: float) -> float:
    return math.tan(angle)


### Math classes ###


class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def set(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector2D) -> Vector2D:
        if isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        elif isinstance(other, float):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise NotImplementedError()

    # Alternative to length()
    def length_sq(self) -> float:
        return (self.x * self.x + self.y * self.y)

    # TODO add vector operations
