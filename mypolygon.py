from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

def square(t, length):
    print t
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length):
    print t
    for i in range(6):
        fd(t, length)
        lt(t, 60)

def circle(t, radius):
    print t
    t.delay = .01
    circumference = math.pi * 2 * radius
    length = circumference / 360
    for i in range(360):
        fd(t, length)
        lt(t, 1)

def arc(t, radius, angle):
    print t
    t.delay = .01
    circumference = math.pi * 2 * radius
    length = circumference / 360
    for i in range(angle):
        fd(t, length)
        lt(t, 1)

arc(bob, 100, 270)

wait_for_user()
