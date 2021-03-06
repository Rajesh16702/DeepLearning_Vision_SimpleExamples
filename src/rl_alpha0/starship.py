import math
import random

import numpy as np
import pygame
from pygame.locals import *

np.set_printoptions(threshold=np.inf)
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)


class Vec2(object):
    def __init__(self, x=0, y=0):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = float(new_x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = float(new_y)

    def __add__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vec2(self + other.x, self + other.y)
        elif isinstance(other, types):
            return Vec2(self.x + other, self.y + other)
        else:
            return Vec2(self.x + other.x, self.y + other.y)

    def __div__(self, other):
        types = (int, float)
        if isinstance(self, types):
            self = Vec2(self, self)
        elif isinstance(other, types):
            other = Vec2(other, other)
        x = self.x / other.x
        y = self.y / other.y
        return Vec2(x, y)

    def __mul__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vec2(self * other.x, self * other.y)
        elif isinstance(other, types):
            return Vec2(self.x * other, self.y * other)
        else:
            return Vec2(self.x * other.x, self.y * other.y)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __radd__(self, other):
        return Vec2(self.x + other, self.y + other)

    def __rdiv__(self, other):
        return Vec2(other/self.x, other/self.y)

    def __rmul__(self, other):
        return Vec2(other * self.x, other * self.y)

    def __rsub__(self, other):
        return Vec2(other - self.x, other - self.y)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Vec2: ({0}, {1})".format(self.x, self.y)

    def __sub__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vec2(self - other.x, self - other.y)
        elif isinstance(other, types):
            return Vec2(self.x - other, self.y - other)
        else:
            return Vec2(self.x - other.x, self.y - other.y)

    def ceil(self):
        return Vec2(math.ceil(self.x), math.ceil(self.y))

    def floor(self):
        return Vec2(math.floor(self.x), math.floor(self.y))

    def get_data(self):
        return (self.x, self.y)    

    def inverse(self):
        return Vec2(1.0/self.x, 1.0/self.y)

    def length(self):
        return math.sqrt(self.square_length())

    def normalize(self):
        length = self.length()
        if length == 0.0:
            return Vec2(0, 0)
        return Vec2(self.x/length, self.y/length)

    def round(self):
        return Vec2(round(self.x), round(self.y))

    def square_length(self):
        return (self.x * self.x) + (self.y * self.y)

    """
    def transform(self, matrix):#mat2, mat2d, mat3, mat4
        pass

    @classmethod
    def cross(cls, a, b):
        z = (a.x * b.y) - (a.y * b.x)
        return Vec3(0, 0, z)
    """

    @classmethod
    def distance(cls, a, b):
        c = b - a
        return c.length()

    @classmethod
    def dot(self, a, b):
        return (a.x * b.x) + (a.y * b.y)

    @classmethod
    def equals(cls, a, b, tolerance=0.0):
        diff = a - b
        dx = math.fabs(diff.x)
        dy = math.fabs(diff.y)
        if dx <= tolerance * max(1, math.fabs(a.x), math.fabs(b.x)) and \
           dy <= tolerance * max(1, math.fabs(a.y), math.fabs(b.y)):
            return True
        return False

    @classmethod
    def max(cls, a, b):
        x = max(a.x, b.x)
        y = max(a.y, b.y)
        return Vec2(x, y)

    @classmethod
    def min(cls, a, b):
        x = min(a.x, b.x)
        y = min(a.y, b.y)
        return Vec2(x, y)

    @classmethod
    def mix(cls, a, b, t):
        return a * t + b * (1-t)

    @classmethod
    def random(cls):
        x = random.random()
        y = random.random()
        return Vec2(x, y)

    @classmethod
    def square_distance(cls, a, b):
        c = b - a
        return c.square_length()





class Particle:
    def __init__(self, x ,y, vx, vy):
        self.m = 1.0
        self.p = Vec2(x,y)
        self.v = Vec2(vx,vy)
        self.f = Vec2(0,0)
        self.lastf = Vec2(0,0)

    def update(self, dt):
        if (self.m>0):
            self.v = self.v + (dt/self.m)*self.f
            self.p = self.p + dt*self.v
            self.lastf = self.f
            #self.f = Vec2(0,0)     # for game

    def clampVelocity(self, vmax):
        if self.v.length()>vmax:
            self.v = (vmax / self.v.length()) * self.v

    def addForce(self, f):
        self.f += f

    def setForce(self, f):
        self.f = f

    def setVelocity(self, v):
        self.v = v

    def setPosition(self, p):
        self.p = p




class Starship:
    def __init__(self): # Notre méthode constructeur
        print("Starship Game ...")
    

    #====================== Used by opti/learning ===========================================
    def init(self,name,w,h,px,py,f=0):
        self.m_paused = False
        self.m_quit = False
        self.m_print = False
        self.target = Vec2(w/2, h/2)
        self.starship = np.empty( self.sizeOfBatch(), dtype=Particle )
        self.rew = np.empty(self.sizeOfBatch(), dtype=float)
        #self.done = np.empty( self.sizeOfBatch(), dtype=bool )
        #self.obs = np.empty( (self.sizeOfBatch(),self.sizeOfObservationArray()), dtype=float )
        #self.act = np.empty( (self.sizeOfBatch(),self.sizeOfActionArray()), dtype=float )
        self.w = w
        self.h = h
        self.vmax = 20.0
        self.fmax = 5.0
        self.dt = 0.1
        self.random_seed = 217
        random.seed( self.random_seed )
        self.resetRandomlyAllBatch()
        self.noAction = True
        pygame.init()
        self.screen = pygame.display.set_mode((w, h))
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 10)
        self.printDebug();

    def isQuit(self):
        return self.m_quit

    def sizeOfActionArray(self):
        return 2

    def sizeOfObservationArray(self):       # position(x,y) and velocity(vx,vy)
        return 4

    def sizeOfBatch(self):
        return 10

    #====================== Used by opti/learning ===========================================

    def name(self):
        return type(self).__name__

    def printDebug(self):
        print("Starship::init...ok")
        for i in range(self.sizeOfBatch()):
            self.printDebugOne(i)

    def printDebugOne(self, i):
        print("obs=" + str(self.observation(i)) + " reward="+str(self.rew[i]) + " done=" + str(self.done(i)))





    def paused(self):
        return self.m_paused;

    def setPaused(self, p=True):
        self.m_paused = p

    def resetOneAgent(self, i, obsone):
        x = 0.5 * self.w * obsone[0]
        y = 0.5 * self.h * obsone[1]
        vx = self.vmax*obsone[2]
        vy = self.vmax*obsone[3]
        self.starship[i] = Particle( self.target.x-x, self.target.y-y, vx, vy);           # obs = target - p
        self.rew[i] = 0.0
        self.setAction(i, np.zeros( self.sizeOfActionArray()) )
        self.computeReward(i)

    def resetAllBatch(self, obsone):
        for i in range(self.sizeOfBatch()):
            self.resetOneAgent(i, obsone)

    def resetRandomlyOneAgent(self, i):
        #obsone = [ random.random()*(0.8*self.w-1)-self.target.x, random.random()*(0.8*self.h-1)-self.target.y, 0, 0 ]
        obsone = [ random.random()*2-1, random.random()*2-1, random.random()*2-1, random.random()*2-1 ]
        obsone[0] *= 0.8
        obsone[1] *= 0.8
        self.resetOneAgent( i, obsone )

    def resetRandomlyAllBatch(self):
        for i in range(self.sizeOfBatch()):
            self.resetRandomlyOneAgent(i)

    def observationForAllBatch(self):
        batch_obs = np.empty( (self.sizeOfBatch(),self.sizeOfObservationArray()), dtype=float )
        for i in range(self.sizeOfBatch()):
            batch_obs[i] = self.observation(i)
        return batch_obs

    def observation(self, i):
        p = self.starship[i].p
        o = self.target-p               # vector(position, target)
        o.x = o.x / (0.5*self.w)
        o.y = o.y / (0.5*self.h)
        if abs(o.y)>1:
            print( str(self.target.y-p.y)+" "+str(self.h))
        vx = self.starship[i].v.x / self.vmax
        vy = self.starship[i].v.y / self.vmax
        obs = np.array( [ o.x, o.y, vx, vy ] )
        return obs

    def setRewardForAllBatch(self, rewa=0.0):
        for i in range(self.sizeOfBatch()):
            self.rew[i] = rewa

    def reward(self, n_eme):
        return self.rew[n_eme]

    def done(self, i):
        p = self.starship[i].p
        return (p.x<0 or p.y<0 or p.x>=self.w or p.y>=self.h)

    def action(self, i):
        return np.array( [ self.starship[i].f.x/self.fmax, self.starship[i].f.y/self.fmax ] )

    def setRandomAction(self, i):
        actone = np.array( [ (random.random() * 2.0 - 1.0),  (random.random() * 2.0 - 1.0) ] )
        self.setAction(i, actone)

    def setRandomActionForAllBatch(self):
        for i in range(self.starship.size):
            self.setRandomAction(i)

    def setZeroActionForAllBatch(self):
        actone = np.array( [ 0,0 ] )
        for i in range(self.starship.size):
            self.setAction(i, actone)

    def setAction(self, i, actone):
        self.starship[i].setForce(Vec2(self.fmax * actone[0], self.fmax*actone[1]))

    def setActionForAllBatch(self, actone):
        for i in range(self.sizeOfBatch()):
            self.setAction( i, actone )




    def computeReward(self, i):
        p = self.starship[i].p
        o = self.target-p               # vector(position, target)
        self.rew[i] += 1000.0 / (1.0 + o.length())

    def stepBatch(self):
        # if self.m_paused:
        #     return
        for i in range(self.sizeOfBatch()):
            if not self.done(i):
                self.starship[i].update(self.dt)
                self.starship[i].clampVelocity(self.vmax)
                self.computeReward(i)
            if self.m_print:
                print("py! observation shape=", self.obs.shape, " action shape=", self.act.shape,
                        "    observation=", self.obs, " action=", self.act,
                        "   reward=", self.rew, "  done=", self.done)

    def stepBatchRandom(self):
        self.setRandomActionForAllBatch()
        self.stepBatch()

    def close(self):
        pass

    def drawSceneMenuAndSwap(self):
        if not self.m_quit:
            self.screen.fill( (15,15,75) )
            pygame.draw.circle( self.screen, (255,0,0), (int(self.target.x), int(self.target.y)), 5, 0 )
            for i in range(self.starship.size):
                color = (255,255,255)
                colorv = (255,255,0)
                colorf = (255,0,0)
                if i==0:
                    color = (0,0,255)
                p = self.starship[i].p
                v = self.starship[i].v
                f = self.starship[i].lastf
                pygame.draw.circle( self.screen, color, (int(p.x), int(p.y)), 5, 0 )
                pygame.draw.line( self.screen, colorv, (int(p.x), int(p.y)), (int(p.x+5*v.x), int(p.y+5*v.y)) )
                pygame.draw.line( self.screen, colorf, (int(p.x), int(p.y)), (int(p.x+5*f.x), int(p.y+5*f.y)) )
                textsurface = self.myfont.render(str(int(self.rew[i])), False, (255, 0, 50))
                self.screen.blit(textsurface,(int(p.x)+10, int(p.y)+10))
            pygame.display.flip()

    def eventKey(self, k):
        keys = pygame.key.get_pressed()
        if keys[k]:
            return True
        else:
            return False

    def manageOneEvent(self, event):
        do = False
        if event.type == QUIT:
            self.m_quit = True
        if event.type == KEYDOWN:
            carac = event.dict['unicode']
            if event.key == K_ESCAPE or carac == 'q':
                self.m_quit = True
                do = True
            elif carac == 'd':
                self.printDebug()
                do = True
            elif carac == 'r':
                print("Random reset")
                self.random_seed = random.randint(100, 500);
                random.seed(self.random_seed)
                self.resetRandomlyAllBatch()
                do = True
            elif carac == 'e':
                random.seed(self.random_seed)
                self.resetRandomlyAllBatch()
                do = True
            elif carac == 'p':
                self.m_paused = not self.m_paused
                print("paused: " + str(self.m_paused))
                do = True
            elif carac == 'n':
                self.stepBatch()
                print("stepBatch")
                do = True
            elif carac == 'a':
                self.noAction = not self.noAction
                print("no action=" + str(self.noAction))
                do = True
            elif carac == 'h':
                self.help()
        return do

    def manageEvent(self):
        for event in pygame.event.get():	#Attente des événements
            if event.type == KEYDOWN and not self.manageOneEvent(event):
                carac = event.dict['unicode']
                return carac
        #carac = None
        return None

    def help(self):
        print(self.name())
        print("   a=toggle (no)/random Action")
        print("   d=print Debug")
        print("   r=Random reset")
        print("   e=rEset")
        print("   p=Paused")
        print("   n=Next step for all batch")
        print("   q=Quit")

    def run(self):
        while not self.m_quit:
            if self.noAction:
                self.setZeroActionForAllBatch()
            else:
                self.setRandomActionForAllBatch()
            self.stepBatch()
            self.manageEvent()
            self.drawSceneMenuAndSwap()
            #print("one step")

if __name__ == "__main__":
    print("Starship game starting...")
    ship = Starship()
    ship.init("Starship", 800, 600, 50, 50)
    ship.run()
