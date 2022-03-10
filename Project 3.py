#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*
import math
import numpy as np


# In[2]:


#initialization
dt = 0.001
g = 9.8
y = 1
v=15
vy = 0
vx = 0
theta = math.radians(90)
x=0
t=0
omega = 0
alpha = -sin(theta)*g
drag = 0.1
check = -1
startingangle=90
period = 0
c=0.5
driveamp=1.2
drivefreq=2/3

movingsphere = sphere(pos=vector(1,1,0), radius = 0.1, make_trail=True, trail_type="points", interval = dt)
string = cylinder(pos = vector(0,1,0), radius = 0.05, axis = vector(sin(theta), - cos(theta), 0))
ground = box(pos=vector(0,0,0), size = vector(2,0.1,2))
scene.center = vector(0,y/2,0)
scene.width= 400


# In[ ]:


#Pendulum 3
#ke = np.square(omega)/2
#pe = y*g
#print(ke+pe)
dt = 0.01
g = 9.8
y = 1
v=15
vy = 0
vx = 0
theta = math.radians(startingangle)
x=0
t=0
omega = 0
graph(width=400, height=250, xmin=math.radians(-180), xmax=math.radians(180), background = color.white, title="theta versus omega", ytitle = "omega", xtitle = "theta")
thetaDots1 = gdots(color=color.green, interval = 10, size=1)

def adjustamp():
    ampSliderReadout.text = ampSlider.value 
scene.append_to_caption("\n\n")
ampSlider = slider(left=10, min=0, max=2, step=0.01, value=0.5,bind=adjustamp)
scene.append_to_caption(" amp = ")
ampSliderReadout = wtext(text="1")

driveamp=ampSlider.value
def torque(the, ome, tim):
    return -sin(the) - c*ome + driveamp*sin(drivefreq*tim)

running = False
def launch():
    global running
    running = True
    
def pause():
    global running
    running = False
    
def delete():
    global gd
    thetaDots1.delete()
    

button(text="Launch!", bind = launch)
button(text="pause!", bind = pause)
button(text="clear!", bind = delete)


while True:
    rate(300)
    driveamp=ampSlider.value
    if running:
        alpha = torque(theta,  omega, t)
        thetamid = theta + omega * 0.5 * dt
        omegamid = omega + alpha * 0.5 * dt
        alphamid =  torque(thetamid, omegamid, t)
        theta += omegamid * dt
        omega += alphamid * dt
        t+=dt
        x = sin(theta)
        y = 1- cos(theta)
        movingsphere.pos = vector(x, y, 0)
        string.axis = vector(x,y-1,0)
        if theta>math.radians(180):
            theta -= math.radians(360)
        if theta < -math.radians(180):
            theta+= math.radians(360)
        thetaDots1.plot(theta,omega)


#ke = np.square(omega)/2
#pe = y*g
#print(ke+pe)


# In[ ]:


#Pendulum 2
#ke = np.square(omega)/2
#pe = y*g
#print(ke+pe)
movingsphere2 = sphere(pos=vector(1,1,2), radius = 0.1, make_trail=True, trail_type="points", interval = dt)
string2 = cylinder(pos = vector(0,1,2), radius = 0.05, axis = vector(sin(theta), - cos(theta), 0))
graph(width=400, height=250, background = color.white, title="time versus theta", ytitle = "theta", xtitle = "time")
graph(width=400, height=250, background = color.white, title="time versus theta difference", ytitle = "difference", xtitle = "time")
thetaDots1 = gdots(color=color.green, interval = 10)
thetaDots2 = gdots(color=color.magenta, interval = 10)
difference = gdots(color=color.green, interval = 10)
dt = 0.001
g = 9.8
y = 1
y2=1
v=15
vy = 0
vx = 0
theta = 0
theta2 = 0.001
x=0
x2=0
t=0
omega = 0
omega2  = 0
def torque(the, ome, tim):
    return -sin(the) - c*ome + driveamp*sin(drivefreq*tim)

while t <200: 
    rate(1000)
    alpha = torque(theta, omega, t)
    thetamid = theta + omega * 0.5 * dt
    omegamid = omega + alpha * 0.5 * dt
    alphamid =  torque(thetamid, omegamid, t)
    theta += omegamid * dt
    omega += alphamid * dt
    x = sin(theta)
    y = 1- cos(theta)
    alpha2 = torque(theta2, omega2, t)
    thetamid2 = theta2 + omega2 * 0.5 * dt
    omegamid2 = omega2 + alpha2 * 0.5 * dt
    alphamid2 =  torque(thetamid2, omegamid2, t)
    theta2 += omegamid2 * dt
    omega2 += alphamid2 * dt
    t+=dt
    x2 = sin(theta2)
    y2 = 1- cos(theta2)
    thetaDots1.plot(t,theta)
    thetaDots2.plot(t,theta2)
    difference.plot(t,log(abs(theta2-theta)))
    movingsphere.pos = vector(x, y, 0)
    string.axis = vector(x,y-1,0)
    movingsphere2.pos = vector(x2, y2, 2)
    string2.axis = vector(x2,y2-1,0)    
#ke = np.square(omega)/2
#pe = y*g
#print(ke+pe)


# In[4]:


#Pendulum 1
#ke = np.square(omega)/2
#pe = y*g
#print(ke+pe)
def pendulum1():
    global period
    check = -1
    dt = 0.01
    g = 9.8
    y = 1
    v=15
    vy = 0
    vx = 0
    theta = math.radians(startingangle)
    x=0
    t=0
    omega = 0
    alpha = -sin(theta)*g
    period= 0
    while t <10: 
        rate(5/dt)
        alpha = torque(theta,  omega, t)
        thetamid = theta + omega * 0.5 * dt
        omegamid = omega + alpha * 0.5 * dt
        alphamid =  -sin(thetamid)*g - c*omegamid
        lasttheta = theta
        theta += omegamid * dt
        if (lasttheta < 0) & (theta>=0):
            if(check>0):
                period = (t-check)
                break
            else:
                check=t
        omega += alphamid * dt
        t+=dt
        x = sin(theta)
        y = 1- cos(theta)
        movingsphere.pos = vector(x, y, 0)
        string.axis = vector(x,y-1,0)
#ke = np.square(omega)/2
#pe = y*g
#print(ke+)


# In[ ]:


pendulum2()


# In[5]:


while(startingangle<180):
    pendulum1()
    print(startingangle, "\t", period)
    startingangle+=10
    

