#!/usr/bin/env python3


# Here we define the problems cases
# each case must be define in function
# and it should take User Interaction as argument
# to process the variable into solver
# TODO we have to define a function exporter


# HEKK --------
print("""
What you want to calculate ? 
[t] Time
[v] Speed
[u] InitialSpeed
[a] Acceleration
""")
x = input("Enter : ")

if x == "t":
    time = "w"
else:
    time = int(input("SET time : "))
if x == "v":
    speed = "w"
else:
    speed = int(input("SET speed : "))
if x == "u":
    initialSpeed = "w"
else:
    initialSpeed = int(input("SET initialSpeed : "))
if x == "a":
    acceleration = "w"
else:
    acceleration = int(input("SET acceleration : "))

# HEKK ----------


def unitcheck(a):
    pass


# Example
def case_i():
    r"""
        if something is moving from the rest in straigh line 
        and he has a velocity of v at t second
        from the begging of the motion.
        determine it's acceleration it start with ?
    """
    v = (speed)
    t = (time)
    u = (initialSpeed)
    a = (acceleration)

    # TODO
    # unitcheck(v)

    # solve it
    if a == "w":
        a = (v-u)/t
        answer = str(a)+" m/s^2"
        return answer
    if u == "w":
        u = v-(a*t)
        answer = str(u)+" m/s"
        return answer
    if t == "w":
        t = (v-u)/a
        answer = str(t)+" s"
        return answer
    if v == "w":
        v = u+(a*t)
        answer = str(v)+" m/s"
        return answer


# Export case i to solver
def exporter():
    # until now there is no Gui so no need for solver ~
    pass
