import math

def shrink_factor(vel):
    inside = 1 - ((vel*299792458)**2/(299792458)**2)
    return math.sqrt(inside)

def length_contraction(vel):
    return (100000 * shrink_factor(vel))

def time_dilation(vel):
    return shrink_factor(vel)

def main():
    # print(shrink_factor(0.99))
    # print(length_contraction(0.99))
    pass

main()