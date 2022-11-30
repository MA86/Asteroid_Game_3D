from __future__ import annotations
import sdl2
import OpenGL.GL as GL
from maths import Matrix4
import ctypes
from component import Component
from shader import Shader


class SpriteComponent(Component):
    def __init__(self, owner: Actor, draw_order: int = 100) -> None:
        super().__init__(owner)
        self.m_texture: sdl2.SDL_Texture = None
        self.m_draw_order: int = draw_order
        self.m_text_width = ctypes.c_int()
        self.m_text_height = ctypes.c_int()

        self._m_owner.get_game().add_sprite(self)

    def delete(self) -> None:
        # Remove from owner's list
        super().delete()
        # Remove from game's list
        self._m_owner.get_game().remove_sprite(self)

    def draw(self, shader: Shader) -> None:
        # Scale quad mesh by width/height of texture
        scale_mat: Matrix4 = Matrix4.create_scale_matrix_xyz(
            float(self.m_text_width.value + 128),
            float(self.m_text_height.value + 128),  # TODO fix
            1.0)
        # Calculate world transform matrix
        world_mat: Matrix4 = scale_mat * self._m_owner.get_world_transform()

        # Set world transform matrix in shader
        shader.set_matrix_uniform("uWorldTransform", world_mat)

        # Draw quad mesh
        GL.glDrawElements(
            GL.GL_TRIANGLES,    # Type of shape to draw
            6,                  # Indices in index buffer
            GL.GL_UNSIGNED_INT,  # Type of index
            None
        )

    def set_texture(self, texture: sdl2.SDL_Texture) -> None:  # TODO fix
        self.m_texture = texture

        # Query height/width for texture
        sdl2.SDL_QueryTexture(texture, None, None,
                              ctypes.byref(self.m_text_width),
                              ctypes.byref(self.m_text_height))

    def get_draw_order(self) -> int:
        return self.m_draw_order

    def get_text_height(self) -> ctypes.c_int:
        return self.m_text_height

    def get_text_width(self) -> ctypes.c_int:
        return self.m_text_width
