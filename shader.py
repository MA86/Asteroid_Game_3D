from __future__ import annotations
import OpenGL.GL as GL


class Shader:
    def __init__(self) -> None:
        # Store shader object IDs
        self._m_vertex_shader_id: GL.GLuint = None
        self._m_frag_shader_id: GL.GLuint = None
        self._m_shader_program: GL.GLuint = None

    def delete(self) -> None:
        pass

    # Load vertex & frag shaders
    def load(self, vert_name: str, frag_name: str) -> bool:
        pass

    def unload(self) -> None:
        pass

    # Set this as active shader program
    def set_active(self) -> None:
        pass

    # TODO
    def set_matrix_uniform(self) -> None:
        pass

    # Compile specified shader
    def _compile_shader(self, file_name: str, shader_type: GL.GLenum, out_shader: GL.GLuint) -> bool:
        pass

    # Test whether shader is compiled
    def _is_compiled(self, shader: GL.GLuint) -> bool:
        pass

    # Test whether shaders link
    def _is_valid_program(self) -> bool:
        pass
