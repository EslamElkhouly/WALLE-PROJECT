from OpenGL.GL import *
from OpenGL.GLUT import *
from scratch_2 import *
def draw():
    glClearColor(.5,.7,.8,1)
    glClear(GL_COLOR_BUFFER_BIT)


    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex(1, -0.6)
    glVertex(-1, -0.6)
    glEnd()


    #LEFT & RIGHT WHELL
    glColor3f(0.7,0.7,0.7)
    Walle_Wheel(1, -1)
    Walle_Wheel(-1,-1)
    draw_lines(.67, .45, -0.20, -.60, 0.04)
    draw_lines(-.67, -.45, -0.20, -.60, 0.04)


    # LEFT &  RIGHT wheel MARKING
    Walle_WheelMarking(-1,-1)
    Walle_WheelMarking(1,-1)


    # LEFT &  RIGHT wheel part MARKING
    glColor3f(0.7,0.7,0.7)
    Walle_WheelPart(-1,-1)
    Walle_WheelPart(1,-1)
    Walle_WheelPartMarking(-1, -1)
    Walle_WheelPartMarking(1, -1)


    #walle body
    glColor3f(.8,.6 , 0.1)
    Walle_Body()
    glColor3f(0,0,0)
    Walle_BodyMarking()


    #Pipe nails
    draw_circle(.009,-.34,-.51)
    draw_circle(.009,.34,-.51)


    #PIPE
    glColor3f(0,0,0)
    Walle_Pipe(-1,-1)
    Walle_Pipe(1,-1)

    Walle_UperBody()

    Walle_Hand(1,1)
    Walle_Hand(-1,1)
    Walle_HandMarking(1, 1)
    Walle_HandMarking(-1, 1)


    Walle_Name()

    Walle_Face()
    Walle_Eyes(1)
    Walle_Eyes(-1)

    glColor3f(1, 1, 1)
    Troll(1)
    Troll(-1)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow("WALL-E AL4B7")
glutDisplayFunc(draw)
glutMainLoop()