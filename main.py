import threading
import _thread as thread
from tkinter import *
from time import time
from particles import *
from random import randint

class App:
    def __init__(self, root, cWidth=300, cHeight=300):
        root.title("Particles")
        frame = Frame(root)
        frame.pack()

        self.canvas = Canvas(frame, width=cWidth, height=cHeight)
        self.canvas.width = cWidth
        self.canvas.height = cHeight
        self.canvas.pack()

        self.particles = []
        for i in range(50):
            self.particles.append(Particle([randint(0, 600),randint(0, 600)],
                [randint(-20,20),randint(-20,20)] ,5,1))

        self.G = 10000
        self.finished = False
        thread.start_new_thread(self.simulate, ())

    def simulate(self):
        print(threading.get_ident())
        now = then = time()
        while not self.finished:
            now = time()
            interval = now - then
            if interval > 0.06:
                for i in range(len(self.particles)):
                    for j in range(i+1, len(self.particles)):
                            p1, p2 = self.particles[i], self.particles[j]
                            dist = Particle.dist(p1, p2)
                            F_mag = self.G*p1.mass*p2.mass/dist**2
                            p1.inc_accel(F_mag, p2, dist=dist)
                            p2.inc_accel(F_mag, p1, dist=dist)
                for p in self.particles:
                    p.update(interval, self.canvas.width,
                            self.canvas.height)
                self.canvas.delete(ALL)
                for p in self.particles:
                    p.render(self.canvas)
                then = now

    def finish(self):
        self.finished = True


root = Tk()

app = App(root,600,600)

root.mainloop()

app.finish()
print(threading.get_ident())
