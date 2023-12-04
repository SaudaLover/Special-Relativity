import math

def shrink_factor(vel, light):
    inside = 1 - ((vel)**2/(light)**2)
    return math.sqrt(inside)

