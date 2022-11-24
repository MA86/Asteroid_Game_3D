from __future__ import annotations
import sdl2
import OpenGL.GL as GL
import math
import ctypes
from component import Component
from shader import Shader


class SpriteComponent(Component):
    def __init__(self, owner: Actor, draw_order: int = 100) -> None:
        super().__init__(owner)
        self.m_texture: sdl2.SDL_Texture = None
        self.m_draw_order: int = draw_order
        self.m_text_width = ctypes.c_int(0)
        self.m_text_height = ctypes.c_int(0)

        self._m_owner.get_game().add_sprite(self)

    def delete(self) -> None:
        # Remove from owner's list
        super().delete()
        # Remove from game's list
        self._m_owner.get_game().remove_sprite(self)

    def draw(self, shader: Shader) -> None:
        GL.glDrawElements(
            GL.GL_TRIANGLES,    # Type of shape to draw
            6,                  # Indices in index buffer
            GL.GL_UNSIGNED_INT,  # Type of index
            None
        )

    def set_texture(self, texture: sdl2.SDL_Texture) -> None:
        self.m_texture = texture

        # Query height/width for texture
        sdl2.SDL_QueryTexture(texture, None, None,
                              ctypes.byref(self.m_text_width), ctypes.byref(self.m_text_height))

    def get_draw_order(self) -> int:
        return self.m_draw_order

    def get_text_height(self) -> ctypes.c_int:
        return self.m_text_height

    def get_text_width(self) -> ctypes.c_int:
        return self.m_text_width
