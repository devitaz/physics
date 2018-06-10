# Zachary DeVita
# October 30, 2014
# PH 211
# LAB 5 - Computes the acceleration of a falling object in the atmosphere 

from visual import*         #   Imports everything from visual
from math import*           #   Imports everything from math
from visual.graph import*   #   Imports everything from visual graph

#   This section establishes the initial variables and constant

s=vector(0.0,2.0,0.0)       #   initializes the object at 2m
v=vector(0.0,0.0,0.0)       #   initializes velocity at 0
g=vector(0.0,-9.81,0.0)     #   initializes gravity at -9.81
A=.1*.1*pi                  #   computes size of the filter
k=.25                       #   empiracle constant which is .25 kg/m^3 on Earth
b=k*A                       #   establishes the coeficient of friction in air
t=0.0                       #   starts the clock at 0
dt=.01                      #   increments the time at .01 seconds
m=0.00418                   #   establishes the mass of the object falling
f1=gcurve(color=color.cyan) #   opens the graph curve and establishes the color

while s.y>0:
    rate(1000)              #   increments the clock 1000 times a second
    a=((m*g)-(b*v))/m       #   determines current acceleration
    Fd=b*mag(v)*norm(-v)    #   determines current force on filter
    s=s+v*dt                #   increments the position
    v=v+a*dt                #   increments the velocity
    t=t+dt                  #   increments the time
    f1.plot(pos=(t,s.y))    #   adds to the plot chart time scale and removes from the y position

print "s=",s,"\n","v=",v,"\n","a=",a,"\n","t=",t,"\n","FD=",Fd,"\n\n"
