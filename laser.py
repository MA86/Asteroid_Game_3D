from __future__ import annotations
from actor import Actor, State
from sprite_component import SpriteComponent
from move_component import MoveComponent
from circle_component import CircleComponent


class Laser(Actor):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self._m_death_timer: float = 1.0

        # Create components
        sc = SpriteComponent(self)
        sc.set_texture(game.get_texture(b"assets/laser.png"))

        self._m_move = MoveComponent(self)
        self._m_move.set_mass(0.1)

        self._m_circle = CircleComponent(self)
        self._m_circle.set_radius(11.0)

    # Implements
    def update_actor(self, dt: float) -> None:
        # Laser is dead after x time
        self._m_death_timer -= dt
        if self._m_death_timer <= 0.0:
            self.set_state(State.eDEAD)
        else:
            # Check for intersection
            for ast in self.get_game().get_asteroids():
                if self._m_circle.intersect(self._m_circle, ast.get_circle()):
                    # Both actors are dead
                    self.set_state(State.eDEAD)
                    ast.set_state(State.eDEAD)
                    break

    def apply_force(self, force: Vector2D) -> None:
        self._m_move.add_force(force)
