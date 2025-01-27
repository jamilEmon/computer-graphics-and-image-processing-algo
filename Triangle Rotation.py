import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_axes():
    glColor3f(1.0, 1.0, 1.0)  # White color for axes
    glBegin(GL_LINES)
    glVertex2f(-10, 0)  # x-axis
    glVertex2f(10, 0)
    glVertex2f(0, -10)  # y-axis
    glVertex2f(0, 10)
    glEnd()

def basic_triangle(x1, y1, x2, y2, x3, y3):
    glColor3f(0.0, 1.0, 0.0)  
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)  # Point A
    glVertex2f(x2, y2)  # Point B
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)  # Point C
    glVertex2f(x3, y3)
    glVertex2f(x1, y1)  # Back to Point A
    glEnd()

def rotated_triangle(x1, y1, x2, y2, x3, y3, angle):
    # Convert angle to radians
    theta = math.radians(angle)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Apply rotation matrix to each point
    x1_rot = x1 * cos_theta - y1 * sin_theta
    y1_rot = x1 * sin_theta + y1 * cos_theta

    x2_rot = x2 * cos_theta - y2 * sin_theta
    y2_rot = x2 * sin_theta + y2 * cos_theta

    x3_rot = x3 * cos_theta - y3 * sin_theta
    y3_rot = x3 * sin_theta + y3 * cos_theta

    glColor3f(0.0, 0.0, 1.0)  # Blue color for rotated triangle
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(x1_rot, y1_rot)
    glVertex2f(x2_rot, y2_rot)
    glVertex2f(x2_rot, y2_rot)
    glVertex2f(x3_rot, y3_rot)
    glVertex2f(x3_rot, y3_rot)
    glVertex2f(x1_rot, y1_rot)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    draw_axes()
    
    # Draw original triangle
    basic_triangle(0, 0, 3, 3, 5, 3)
    
    # Draw rotated triangle by 80 degrees
    rotated_triangle(0, 0, 3, 3, 5, 3, 80)
    
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
glutCreateWindow(b"Plotting with PyOpenGL")
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()