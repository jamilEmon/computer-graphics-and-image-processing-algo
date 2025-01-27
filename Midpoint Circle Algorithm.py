import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_axes():
    glColor3f(1.0, 1.0, 1.0)  # White color for axes
    glBegin(GL_LINES)
    glVertex2f(-10, 0)  # x-axis
    glVertex2f(10, 0)
    glVertex2f(0, -10)  # y-axis
    glVertex2f(0, 10)
    glEnd()

def set_pixel(x, y):
    """Sets a pixel at (x, y) using GL_POINTS."""
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_circle_midpoint(r):
    """Draws a circle using the Midpoint Circle Algorithm."""
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter
    
    glColor3f(0.0, 1.0, 0.0)  # Green color for the circle
    glPointSize(2)
    
    # Iterate through the first octant
    while x <= y:
        # Draw the symmetric points in all octants
        set_pixel(x, y)
        set_pixel(-x, y)
        set_pixel(x, -y)
        set_pixel(-x, -y)
        set_pixel(y, x)
        set_pixel(-y, x)
        set_pixel(y, -x)
        set_pixel(-y, -x)
        
        # Update decision parameter and coordinates in the required format
        if p < 0:
            p = p + 2 * x + 3  # Update when point is inside the circle
        else:
            p = p + 2 * (x - y) + 5  # Update when point is outside the circle
            y -= 1
        x += 1

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    draw_axes()
    draw_circle_midpoint(6)  # Draw a circle of radius 6
    
    glFlush()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -1, 1)
    glMatrixMode(GL_MODELVIEW)


glutInit()  # Initialize GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Midpoint Circle Algorithm with PyOpenGL")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
