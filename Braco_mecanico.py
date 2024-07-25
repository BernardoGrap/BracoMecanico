import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

origem = GLint()
garra_angulo = 0

def desenhar_braco():
    global garra_angulo
    
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(-5, -10)
    glVertex2i(5, -10)
    glVertex2i(5, -40)
    glVertex2i(-5, -40)
    glEnd()

    glPushMatrix()
    glTranslatef(12, 3, 0)
    glRotatef(-45, 0, 0, 1)
    
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(-3, 15)
    glVertex2i(5, 15)
    glVertex2i(5, -15)
    glVertex2i(-3, -15)
    glEnd()

    glPushMatrix()
    glTranslatef(-6, 18, 0)
    glRotatef(garra_angulo, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(-2, 0)
    glVertex2i(0, 0)
    glVertex2i(0, 12)
    glVertex2i(-2, 12)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6, 18, 0)
    glRotatef(-garra_angulo, 0, 0, 1)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2i(0, 0)
    glVertex2i(2, 0)
    glVertex2i(2, 12)
    glVertex2i(0, 12)
    glEnd()
    glPopMatrix()

    glPopMatrix()

def draw_origin():
    global origem
   
    origem = glGenLists(1)
    glNewList(origem, GL_COMPILE)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)  # x
    glVertex3i(0, 0, 0)
    glVertex3i(1, 0, 0)

    glColor3f(0.0, 1.0, 0.0)
    glColor3f(0, 0, 0)  # y
    glVertex3i(0, 0, 0)
    glVertex3i(0, 1, 0)

    glEnd()
    glEndList()

def main():
    global garra_angulo

    pygame.init()
    display = (640, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    draw_origin()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    garra_angulo += 5
                    if garra_angulo > 45:
                        garra_angulo = 45
                elif event.key == K_d:
                    garra_angulo -= 5
                    if garra_angulo < 0:
                        garra_angulo = 0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glCallList(origem)

        ang = 0
        scl = 0.07
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glScale(scl, scl, scl)
        glRotatef(ang, 0, 1, 0)
        desenhar_braco()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0, 0)
        glScale(1, 0.2, 1)
        glRotatef(0, 0, 1, 0)
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2i(-3, -12)
        glVertex2i(3, -12)
        glVertex2i(3, -15)
        glVertex2i(-3, -15)
        glEnd()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()


# Teclas para abrir/fechar as garras :
# A = abre ; D = fechar
# Bernardo Martins - 322122083
# Aline Ferreira - 32210529