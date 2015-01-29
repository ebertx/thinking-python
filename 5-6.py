from swampy.TurtleWorld import *
# import math

def koch(t, len):
    if(len < 3):
        fd(t, len)
        return
    koch(t, len/3)
    lt(t, 80)
    koch(t, len/3)
    rt(t, 160)
    koch(t, len/3)
    lt(t, 80)
    koch(t, len/3)

def snowflake(t, len):
    koch(t, len)
    rt(t, 120)
    koch(t, len)
    rt(t, 120)
    koch(t, len)


world = TurtleWorld()
bob = Turtle()
bob.delay = .01

# koch(bob, 500)
snowflake(bob, 200)