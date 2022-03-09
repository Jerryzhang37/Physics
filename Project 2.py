#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*
import math
import numpy as np


# In[2]:


#initialization
dt = 0.01
g = 9.8
ymax=0
y = 1
v=15
angle = 45
vx = v * (cos(math.radians(angle)))
vy = v * (sin(math.radians(angle)))
x=0
t=0
drag = 0.1
movingsphere = sphere(pos=vector(0,0,0), radius = 1, make_trail=True, trail_type="points", interval = dt)
ground = box(pos=vector(0,0,0), size = vector(100,0.1,100))
scene.center = vector(0,y/2,0)
scene.width= 400


# In[3]:


#2D
def adjustAngle():
    angleSliderReadout.text = angleSlider.value 
scene.append_to_caption("\n\n")
angleSlider = slider(left=10, min=0, max=90, step=1, value=45,bind=adjustAngle)
scene.append_to_caption(" Angle = ")
angleSliderReadout = wtext(text="45 degrees")

def adjustspeed():
    speedSliderReadout.text = speedSlider.value 
scene.append_to_caption("\n\n")
speedSlider = slider(left=10, min=0, max=50, step=1, value=15,bind=adjustspeed)
scene.append_to_caption(" Speed = ")
speedSliderReadout = wtext(text="15 m/s")

def adjustdrag():
    dragSliderReadout.text = dragSlider.value 
scene.append_to_caption("\n\n")
dragSlider = slider(left=10, min=0, max=1, step=0.005, value=0.5,bind=adjustdrag)
scene.append_to_caption(" drag = ")
dragSliderReadout = wtext(text="1")

def launch():
    print("Launching the projectile!")
    global running
    global y, vy, x, vx, t, drag, movingsphere,ground, angle
    y = 1
    v=speedSlider.value
    angle = angleSlider.value
    vx = v * (cos(math.radians(angle)))
    vy = v * (sin(math.radians(angle)))
    x=0
    t=0
    drag = dragSlider .value
    movingsphere = sphere(pos=vector(0,0,0), radius = 1, make_trail=True, trail_type="points", interval = dt)
    ground = box(pos=vector(0,0,0), size = vector(100,0.1,100))
    scene.center = vector(0,y/2,0)
    scene.width= 400
    running =True

def clear():
    global movingsphere
    movingsphere.pos =  movingsphere.pos = vector(0, 0, 0)
    movingsphere.clear_trail()
    


# In[ ]:


running = False
button(text="Launch!", bind = launch)
button(text="clear!", bind = clear)
while True:
    rate(100)
    
    if running: 
        netvsquared=(np.square(vx)+np.square(vy))
        netv=sqrt(netvsquared)
        ray = drag*(netv)*vy
        rax = drag*(netv)*vx
        ay = -g - ray
        ax= -rax
        vymid = vy + ay*0.5*dt
        vxmid = vx + ax*0.5*dt
        netvsquaredmid=(np.square(vxmid)+np.square(vymid))
        netvmid=sqrt(netvsquaredmid)
        raymid=drag*(netvmid)*vymid
        raxmid = drag*(netvmid)*vxmid
        aymid = -g - raymid
        axmid = -raxmid
        y+=vymid * dt
        if y >ymax:
            ymax = y
        x+=vxmid *dt
        vy += aymid * dt
        vx += axmid * dt
        t += dt
        movingsphere.pos = vector(x, y, 0)
        if y < 0:
            running = False
            print(t)
            print(x)
            print(ymax)


# In[ ]:





# In[2]:


#Projectile1

#dt = 0.01
#g = 9.8
#y = 1
#vy = 15
#x=0
#vx=15
#t=0
#drag = 0.1
#graph(width=400, height=250, align = "right", background = color.white, title="time versus y velocity", ytitle = "y velocity", xtitle = "time")
#vDots = gdots(color=color.green, interval = 1)
#vDots.plot(0,0)
#movingsphere = sphere(pos=vector(0,0,0), radius = 1, make_trail=True, trail_type="points", interval = dt)
#ground = box(pos=vector(0,0,0), size = vector(100,0.1,100))
#scene.center = vector(0,y/2,0)
#scene.width= 400


# In[5]:


#Formula 1
#while y >0: 
#    rate(5/dt)
#    ay = -g - drag * abs(vy) * vy
#    y+=vy * dt
#    vy += ay * dt
#    t += dt
#    movingsphere.pos = vector(0, y, 0)
#    vDots.plot(t,vy)
#print("Ball lands at t =",t,"seconds, with velocity", vy, "m/s")
#errort = y/vy
#errorv = errort*ay
#t-=errort
#vy-=errorv
#print("Ball lands at t =",t,"seconds, with velocity", vy, "m/s")


# In[ ]:


#Formula 2
#while y >0: 
#    rate(5/dt)
#    ay = -g - drag * abs(vy) * vy
#    ymid = y + vy*0.5*dt
#    #ymid = y + vy*0.5*dt
#    vymid = vy + ay*0.5*dt
#    aymid = -g - drag * abs(vymid) * vymid
#    y+=vymid * dt
#    vy += aymid * dt
#    t += dt
#    movingsphere.pos = vector(0, y, 0)
#    vDots.plot(t,vy)
#print("Ball lands at t =",t,"seconds, with velocity", vy, "m/s")
#errort = y/vy
#errorv = errort*ay
#t-=errort
#vy-=errorv
#print("Ball lands at t =",t,"seconds, with velocity", vy, "m/s")


# In[ ]:


#netvsquared=(square(vx)+square(vy))
#netvsquaredmid=(square(vxmid)+square(vymid))
#netv=sqrt(netvsquared)
#netvmid=sqrt(netvsquaredmid)
#Fx = c*(netvsquared)
#rax = drag*(netv)*vx
#raxmid = drag*(netvmid)*vxmid
#ray = drag*(netv)*vy
#raymid=drag*(netvmid)*vymid

