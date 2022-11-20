from __future__ import annotations
import OpenGL.GL as GL
import sdl2
import ctypes


class Shader:
    """
    This class encapsulates a shader.

    It creates vertex/frag shaders, combine, and link them into
    a final 'shader program'.
    """

    def __init__(self) -> None:
        # Store shader object IDs
        self._m_vertex_shader_id: GL.GLuint = GL.GLuint(0)
        self._m_frag_shader_id: GL.GLuint = GL.GLuint(0)
        self._m_shader_program_id: GL.GLuint = GL.GLuint(0)

    def delete(self) -> None:
        # TODO
        raise NotImplementedError

    # Load vertex & frag shaders
    def load(self, vert_name: str, frag_name: str) -> bool:
        # Compile vertex & pixel shaders
        if (self._compile_shader(vert_name, GL.GL_VERTEX_SHADER, ctypes.byref(self._m_vertex_shader_id)) == False
                or self._compile_shader(frag_name, GL.GL_FRAGMENT_SHADER, ctypes.byref(self._m_frag_shader_id)) == False):
            return False

        # Link them together to create a 'shader program'
        self._m_shader_program_id = GL.glCreateProgram()
        GL.glAttachShader(self._m_shader_program_id, self._m_vertex_shader_id)
        GL.glAttachShader(self._m_shader_program_id, self._m_frag_shader_id)
        GL.glLinkProgram(self._m_shader_program_id)

        # Verify that program linked
        if not self._is_valid_program:
            return False
        return True

    def unload(self) -> None:
        # Delete shader program along with two other shaders
        GL.glDeleteProgram(self._m_shader_program_id)
        GL.glDeleteShader(self._m_vertex_shader_id)
        GL.glDeleteShader(self._m_frag_shader_id)

    # Sets active shader program
    def set_active(self) -> None:
        GL.glUseProgram(self._m_shader_program_id)

    # TODO
    def set_matrix_uniform(self) -> None:
        pass

    # Compile specified shader
    def _compile_shader(self, file_name: str, shader_type: GL.GLenum, out_shader_id: GL.GLuint) -> bool:
        # Open file
        source_file_obj = open(file_name, "r")
        if source_file_obj:
            # Read file to byte object
            source_byte_obj = source_file_obj.read().encode()
            source_file_obj.close()

            # Create a shader of specific type
            out_shader_id = GL.glCreateShader(shader_type)
            # Set a source code for this shader
            GL.glShaderSource(out_shader_id, 1, source_byte_obj, None)
            # Try to compile this shader
            GL.glCompileShader(out_shader_id)

            if not self._is_compiled(out_shader_id):
                sdl2.SDL_Log("Failed to compile shader: ", file_name)
                return False
        else:
            sdl2.SDL_Log("Shader file not found: ", file_name)
            return False

        return True

    # Test whether shader is compiled
    def _is_compiled(self, shader_id: GL.GLuint) -> bool:
        # Query compile status
        status: GL.GLint = GL.GLint(0)
        GL.glGetShaderiv(shader_id, GL.GL_COMPILE_STATUS, ctypes.byref(status))

        if status != GL.GL_TRUE:
            # TODO later, add debug info using GL.glGetShaderInfoLog()
            sdl2.SDL_Log("GLSL compile failed")
            return False
        return True

    # Test whether shaders link
    def _is_valid_program(self) -> bool:
        # Query compile status
        status: GL.GLint = GL.GLint(0)
        GL.glGetProgramiv(self._m_shader_program_id,
                          GL.GL_LINK_STATUS, ctypes.byref(status))

        if status != GL.GL_TRUE:
            # TODO later, add debug info using GL.glGetProgramInfoLog()
            sdl2.SDL_Log("GLSL link failed")
            return False
        return True
