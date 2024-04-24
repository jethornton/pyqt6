#!/usr/bin/env python3

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = ((-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1), (1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1))
edges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7))
faces = ((0, 1, 2 , 3),(4,  5, 6, 7),(0, 4, 7, 3),(1, 5, 6, 2),(2, 6, 7, 3),(1, 5, 4, 0))

# =============================================================================
# vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
# edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))
# =============================================================================

def Cube():
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glColor3fv((1, 0, 1))
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Main():
    pygame.init()
    screen = (1600, 1200)
    display = pygame.display.set_mode(screen, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (screen[0] / screen[1]), 0.1, 500)
    button_down = False

    glMatrixMode(GL_MODELVIEW)  
    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    while True:
        glPushMatrix()
        glLoadIdentity()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
            if event.type == pygame.MOUSEMOTION:
                if button_down == True:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)
                print(event.rel)

        for event in pygame.mouse.get_pressed():
            print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed()[0] == 1:
                button_down = True
            elif pygame.mouse.get_pressed()[0] == 0:
                button_down = False

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        glTranslatef(0, 0, -5)
        glMultMatrixf(modelMatrix)

        Cube()

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

Main()


