// Request GLSL 3.3
#version 330

// Vertex attributes here.
// This corresponds to data stored 
// for each vertex in vertex buffer.
// For now, just a position.
in vec3 inPosition;

void main()
{
 // Outputs a 4D.
 // For now set the 4th coordinate to 1.0.
 gl_Position = vec4(inPosition, 1.0);
}
