from math import sqrt

class Particle:
    def __init__(self, pos, vel, radius, mass):
        self.pos = pos
        self.radius = radius
        self.mass = mass
        self.vel = vel
        self.accel = [0,0]

    def inc_accel(self, F_mag, other, dist=None):
        if dist is None:
            dist = Particle.dist(self, other)
        self.accel[0] += F_mag*(other.pos[0] - self.pos[0])/dist
        self.accel[1] += F_mag*(other.pos[1] - self.pos[1])/dist

    def update(self, interval, x, y):
        self.vel[0] += self.accel[0]*interval
        self.vel[1] += self.accel[1]*interval

        self.pos[0] += self.vel[0]*interval
        if self.pos[0] < 0 or self.pos[0] >= x:
            self.vel[0] *= -1
            self.pos[0] += 2*self.vel[0]*interval

        self.pos[1] += self.vel[1]*interval
        if self.pos[1] < 0 or self.pos[1] >= y:
            self.vel[1] *= -1
            self.pos[1] += 2*self.vel[1]*interval

        self.accel = [0,0]

    def render(self, canvas):
        x,y = self.pos
        r = self.radius
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")

    @staticmethod
    def dist(p1,p2):
        x1,y1 = p1.pos
        x2,y2 = p2.pos
        return max(sqrt((x2-x1)**2 + (y2-y1)**2), 10)
