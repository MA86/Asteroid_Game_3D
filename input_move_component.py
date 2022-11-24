from __future__ import annotations
from move_component import MoveComponent
from maths import Vector2D
import ctypes


class InputMoveComponent(MoveComponent):
    """ CONTROLS MOVEMENT BASED ON KEYS """

    def __init__(self, owner: Actor) -> None:
        super().__init__(owner)

        # Max forward/rotation speeds
        self._m_forward_speed: float = 0.0
        self._m_max_rotation_speed: float = None

        # Keys for forward/rotation movements
        self._m_forward_key: int = 0
        self._m_back_key: int = 0
        self._m_clockwise_key: int = 0
        self._m_counter_clockwise_key: int = 0

    # Implements
    def input(self, keyb_state: ctypes.Array) -> None:
        # Control MoveComponent based on keys:
        # Forward/back movement
        if keyb_state[self._m_forward_key]:
            self.add_force(self._m_owner.get_forward()
                           * self._m_forward_speed)
            # Forward texture
            self._m_owner.change_texture_to("forward")
        if keyb_state[self._m_back_key]:
            self.add_force(self._m_owner.get_forward()
                           * -self._m_forward_speed)

            # Backward texture
            self._m_owner.change_texture_to("backward")

        # Rotation movement
        rotation_speed = 0.0
        if keyb_state[self._m_clockwise_key]:
            rotation_speed += self._m_max_rotation_speed
        if keyb_state[self._m_counter_clockwise_key]:
            rotation_speed -= self._m_max_rotation_speed
        self.set_rotation_speed(rotation_speed)

    def get_forward_speed(self) -> float:
        return self._m_forward_speed

    def get_max_rotation_speed(self) -> float:
        return self._m_max_rotation_speed

    def get_forward_key(self) -> int:
        return self._m_forward_key

    def get_back_key(self) -> int:
        return self._m_back_key

    def get_clockwise_key(self) -> int:
        return self._m_clockwise_key

    def get_counter_clockwise_key(self) -> int:
        return self._m_counter_clockwise_key

    def set_forward_speed(self, speed: float) -> None:
        self._m_forward_speed = speed

    def set_max_rotation_speed(self, speed: float) -> None:
        self._m_max_rotation_speed = speed

    def set_forward_key(self, key: int) -> None:
        self._m_forward_key = key

    def set_back_key(self, key: int) -> None:
        self._m_back_key = key

    def set_clockwise_key(self, key: int) -> None:
        self._m_clockwise_key = key

    def set_counter_clockwise_key(self, key: int) -> None:
        self._m_counter_clockwise_key = key
