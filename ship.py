from __future__ import annotations
import ctypes
import sdl2
from actor import Actor
from sprite_component import SpriteComponent
from input_move_component import InputMoveComponent
from laser import Laser
from maths import PI


class Ship(Actor):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self._m_laser_cool_down: float = 0.0

        # Create components for Ship
        self._m_sprite = SpriteComponent(self, 150)
        self._m_sprite.set_texture(game.get_texture(b"assets/ship.png"))

        ic = InputMoveComponent(self)
        ic.set_forward_key(sdl2.SDL_SCANCODE_W)
        ic.set_back_key(sdl2.SDL_SCANCODE_S)
        ic.set_clockwise_key(sdl2.SDL_SCANCODE_D)
        ic.set_counter_clockwise_key(sdl2.SDL_SCANCODE_A)
        ic.set_max_rotation_speed(PI)
        ic.set_forward_speed(500.0)
        ic.set_mass(2)

    # Implements
    def update_actor(self, dt: float) -> None:
        self._m_laser_cool_down -= dt

    # Implements
    def input_actor(self, keyb_state: ctypes.Array) -> None:
        if keyb_state[sdl2.SDL_SCANCODE_SPACE] and self._m_laser_cool_down <= 0.0:
            # Create Laser at Ship's pos/rot
            laser = Laser(self.get_game())
            laser.set_position(self.get_position())
            laser.set_rotation(self.get_rotation())
            laser.apply_force(self.get_forward() * 5000.0)

            # Reset laser cooldown (1s)
            self._m_laser_cool_down = 1.0

    def change_texture_to(self, kind: str) -> sdl2.SDL_Texture:
        if kind == "forward":
            self._m_sprite.set_texture(
                self._m_game.get_texture(b"assets/ship_with_thrust.png"))
        if kind == "backward":
            self._m_sprite.set_texture(
                self._m_game.get_texture(b"assets/ship.png"))
