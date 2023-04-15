import turtle
import math
bob = turtle.Turtle()
# # pen down
# bob.pd()
# #
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# turtle.mainloop()
# (1)
def square(t):
    t.pd()
    #
    for i in range(5):
        t.fd(100)
        t.lt(90)
    # t.fd(100)
    # t.lt(90)
    # t.fd(100)
    # t.lt(90)
    # t.fd(100)
    # t.lt(90)
    turtle.mainloop()

# square(bob)
def square2(t, length):
    t.pd()
    #
    for i in range(5):
        t.fd(length)
        t.lt(90)
    # t.fd(100)
    # t.lt(90)
    # t.fd(100)
    # t.lt(90)
    # t.fd(100)
    # t.lt(90)
    turtle.mainloop()

# square2(bob, 200)

def polygon(t, length, n):
    t.pd()
    #
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    # t.fd(100)
    # t.lt(90)
    # t.fd(100)
    # t.lt(90)
    # t.fd(100)
    # t.lt(90)
    turtle.mainloop()

# polygon(bob, 150, 6)


def circle(t, r):
    chuvi = round(2*math.pi*r)
    polygon(t, 1, chuvi)
    turtle.mainloop()

circle(bob, 50)

