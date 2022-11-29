// Request GLSL 3.3
#version 330

// Uniforms (AKA unchanging!) world transform and view-proj matrices
uniform mat4 uWorldTransform;
uniform mat4 uViewProj;

// Vertex attributes 
in vec3 inPosition;

void main()
{
 vec4 pos = vec4(inPosition, 1.0);

 // Output
 gl_Position = pos * uWorldTransform * uViewProj;
}