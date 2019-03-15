from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *
def draw_eyebrow (r,xc=0,yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(pi/3,2* pi/3,.001 ):
        x = xc+r * cos(theta)  # لو عاوز اغير المركز  هزو على اكس الزياده وكذلك واى
        y = yc+r * sin(theta)
        glVertex(x, y)
    glEnd()
def draw_facest (r,xc=0,yc=0):
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0, pi,.001 ):
        x = xc+r * cos(theta)  # لو عاوز اغير المركز  هزو على اكس الزياده وكذلك واى
        y = yc+r * sin(theta)
        glVertex(x, y)
    glEnd()
def draw_face (r,xc=0,yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, pi,.001 ):
        x = xc+r * cos(theta)
        y = yc+r * sin(theta)
        glVertex(x, y)
    glEnd()

def draw_circle (r,xc=0,yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi,.001 ):
        x = xc+r * cos(theta)
        y = yc+r * sin(theta)
        glVertex(x, y)
    glEnd()
def draw_lines(xf,xl,yf,yl,p):
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for line in np.arange(yl,yf,p):
        glColor3f(0,0, 0)
        glVertex(xf, line)
        glVertex(xl, line)
    glEnd()

def Walle_Wheel(x,y):
    glBegin(GL_POLYGON)
    glVertex(x*0.45,y*0.20)
    glVertex(x*0.67,y*.20)
    glVertex(x*.67,y*.6)
    glVertex(x*.45,y*.6)
    glVertex(x*.45,y*.20)
    glEnd()

def Walle_WheelMarking(x,y):
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.45,y* 0.20)
    glVertex(x*0.67, y*.20)
    glVertex(x*.67, y*.6)
    glVertex(x*.45, y*.6)
    glEnd()
def Walle_Body():
    glBegin(GL_POLYGON)
    glVertex(-.4, .4)
    glVertex(.4, .4)
    glVertex(.4, -.4)
    glVertex(-.4, -.4)
    glEnd()


def Walle_BodyMarking():
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex(-.4, .4)
    glVertex(.4, .4)
    glVertex(.4, -.4)
    glVertex(-.4, -.4)
    glEnd()
def Walle_WheelPart(x,y):
    glBegin(GL_POLYGON)
    glVertex(x*0.45, y*0.27)
    glVertex(x*0.30, y*0.27)
    glVertex(x*.30, y*.48)
    glVertex(x*.4, y*.48)
    glVertex(x*.45, y*.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(x*.30, y*.48)
    glVertex(x*.40, y*.48)
    glVertex(x*.40, y*.54)
    glVertex(x*.35, y*.54)
    glVertex(x*.30, y*.50)
    glEnd()

def Walle_WheelPartMarking(x,y):
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.45, y*0.27)
    glVertex(x*0.30, y*0.27)
    glVertex(x*.30, y*.48)
    glVertex(x*.4, y*.48)
    glVertex(x*.45, y*.4)
    glEnd()


    glBegin(GL_LINE_LOOP)
    glVertex(x*.30, y*.48)
    glVertex(x*.40, y*.48)
    glVertex(x*.40, y*.54)
    glVertex(x*.35, y*.54)
    glVertex(x*.30, y*.50)
    glEnd()
def Walle_Pipe(x,y):
    glBegin(GL_POLYGON)
    glVertex(x*0.4,y*0.50)
    glVertex(x*0.45,y*0.50)
    glVertex(x*0.45,y*0.52)
    glVertex(x*0.40,y*0.52)
    glEnd()
def Walle_HandMarking(x,y):
    #UPPER FINGER
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.27,y* 0.23)
    glVertex(x*0.35,y* 0.25)
    glVertex(x*0.35, y*0.20)
    glVertex(x*0.27, y*0.20)
    glEnd()
#UPPER FINGER 2
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.35,y* 0.25)
    glVertex(x*0.44, y*0.25)
    glVertex(x*0.44,y* 0.20)
    glVertex(x*0.35,y* 0.2)
    glEnd()
    #LOWER FINGER
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.27, y*0.15)
    glVertex(x*0.35, y*0.15)
    glVertex(x*0.35, y*0.1)
    glVertex(x*0.27, y*0.12)
    glEnd()

#LOWER FINGER 2
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.35, y*0.15)
    glVertex(x*0.44, y*0.15)
    glVertex(x*0.44, y*0.10)
    glVertex(x*0.35, y*0.1)
    glEnd()

#BET. FINGERS
    glBegin(GL_LINE_LOOP)
    glVertex(x*0.40, y*0.15)
    glVertex(x*0.44, y*0.15)
    glVertex(x*0.44, y*0.20)
    glVertex(x*0.40, y*0.20)
    glEnd()

# ABOVE HAND

    glBegin(GL_LINE_LOOP)
    glVertex(x * .43, y * .25)
    glVertex(x * .43, y * .35)
    glVertex(x * .4, y * .4)
    glVertex(x * .4, y * .25)
    glEnd()


def Walle_Hand(x,y):
    glColor3f(.5, 7, 0.9)#.5,.7,1
    glBegin(GL_POLYGON)
    glVertex(x*0.27,y* 0.23)
    glVertex(x*0.35,y* 0.25)
    glVertex(x*0.35, y*0.20)
    glVertex(x*0.27, y*0.20)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(x*0.35,y* 0.25)
    glVertex(x*0.44, y*0.25)
    glVertex(x*0.44,y* 0.20)
    glVertex(x*0.35,y* 0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(x*0.27, y*0.15)
    glVertex(x*0.35, y*0.15)
    glVertex(x*0.35, y*0.10)
    glVertex(x*0.27, y*0.12)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(x*0.35, y*0.15)
    glVertex(x*0.44, y*0.15)
    glVertex(x*0.44, y*0.10)
    glVertex(x*0.35, y*0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex(x * 0.40, y * 0.15)
    glVertex(x * 0.44, y * 0.15)
    glVertex(x * 0.44, y * 0.20)
    glVertex(x * 0.40, y * 0.20)
    glEnd()
    """

    glBegin(GL_POLYGON)
    glVertex(x * 0.30, y * 0.20)
    glVertex(x * 0.40, y * 0.20)
    glVertex(x * 0.40, y * 0.15)
    glVertex(x * 0.30, y * 0.15)
    glEnd()
"""

    #فوق الايد
    glColor3f(.8, .6, 0.1)
    glBegin(GL_POLYGON)
    glVertex(x * .43, y * .25)
    glVertex(x * .43, y * .35)
    glVertex(x * .4, y * .4)
    glVertex(x * .4, y * .25)
    glEnd()

def Walle_UperBody() :

    #NECK
    glColor3f(0,0,0)
    glBegin(GL_TRIANGLES)
    glVertex(.2,.4)
    glVertex(-.2,.4)
    glVertex(0,.2)
    glEnd()

#TR
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex(0.0, .35)#18.23.13
    glVertex(0.1, .40)
    glVertex(0.1,.30)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex(0.0, .35)
    glVertex(-0.1, .40)
    glVertex(-0.1, .30)
    glEnd()
    glColor3f(0,0,0)

   #BUTTONS
    for i in np.arange(.3,-.4,-.06):
        draw_circle(.009,0,i)

def Walle_Name():

#W

    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex(-.38,- .34)  # 14 20
    glVertex(-.36,- .38)  # 16 12
    glVertex(-.36,- .38)  # 16 12
    glVertex(-.34,- .34)  # 18 20
    glVertex(-.34,- .34)  # 18 20
    glVertex(-.32,- .38)  # 20 12
    glVertex(-.32,- .38)  # 20 12
    glVertex(-.30,- .34)  # 22 20
    glEnd()


#a

    glBegin(GL_LINES)
    glVertex(-0.29, -.38)
    glVertex(-0.27, -0.34)
    glVertex(-0.27, -0.34)
    glVertex(-0.25, -0.38)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-0.28, -.36)
    glVertex(-0.26, -.36)
    glEnd()
    #L

    glBegin(GL_LINES)
    glVertex(-0.24, -.338)
    glVertex(-0.24, -0.38)
    glVertex(-0.24, -0.38)
    glVertex(-0.22, -0.38)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-0.20, -.338)
    glVertex(-0.20, -0.38)
    glVertex(-0.20, -0.38)
    glVertex(-0.18, -0.38)
    glEnd()

    #e
    glColor3f(1,0,0)
    draw_circle(.03,-.13,-.36)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex(-.12,-.37)
    glVertex(-.14, -.37)
    glVertex(-.14, -.37)
    glVertex(-.14, -.36)
    glVertex(-.14, -.36)
    glVertex(-.12, -.36)
    glVertex(-.14, -.36)
    glVertex(-.14, -.35)
    glVertex(-.14, -.35)
    glVertex(-.12, -.35)
    glEnd()

def Walle_Face():
    glColor3f(.7, .7, .7)
    draw_face(.25, 0, .6)
    glColor3f(0,0,0)
    draw_facest(.25, 0, .6)
        # NOISE
    glColor3f(0, 0, 0)
    draw_face(.02,0, .65)


    glColor3f(0.3,.3,0.3)
    glBegin(GL_POLYGON)
    glVertex(.05,.4)
    glVertex(.05,.5)
    glVertex(-.05,.5)
    glVertex(-.05,.4)
    glEnd()
    glColor3f(.2,0.2,0.2)
    glBegin(GL_POLYGON)
    glVertex(.02,.5)
    glVertex(.02,.6)
    glVertex(-.02,.6)
    glVertex(-.02,.5)
    glEnd()

def Walle_Eyes(x):
    glColor3f(1, 1, 1)
    draw_circle(.06, x * .12,.72)

    glColor3f(.5, 7, 0.9)
    draw_circle(.05, x * .1, .7)

    glColor3f(0, 0, 0)
    draw_circle(.02, x * .1, .7)
    draw_eyebrow(.1, x*0.12, .7)
    glColor3f(1, 1, 1)
    draw_circle(.007, x * .1, .69)


def Troll(x):
    glBegin(GL_LINE_LOOP)
    glVertex(x*.6,.6)
    glVertex(x*.6,.7)
    glVertex(x*.7,.8)
    glVertex(x*.7,.8)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex(x * .8, 0)
    glVertex(x * .9, 0)
    glVertex(x * .9, .1)
    glEnd()












