from __future__ import annotations
from maths import Vector2D
import random


class Random:
    """ 
    Cannot be instantiated.
    init() Creates an instance of random.Random class. 
    Basically, a wrapper for random.Random members. 
    """
    _m_random: random.Random = None

    @classmethod
    def init(cls, seed: int) -> None:
        cls._m_random = random.Random(seed)

    @classmethod
    def get_float(cls) -> float:
        return cls._m_random.random()

    @classmethod
    def get_float_range(cls, min: float, max: float) -> float:
        return cls._m_random.uniform(min, max)

    @classmethod
    def get_int_range(cls, min: int, max: int) -> int:
        return cls._m_random.randint(min, max)

    @classmethod
    def get_vector(cls, min: Vector2D, max: Vector2D) -> Vector2D:
        random_vector = Vector2D(cls.get_float(), cls.get_float())
        return min + (max - min) * random_vector

        # TODO Handle Vector3D also
