#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Physics Simulations in Python, Jerry Zhang, 2020/3/7
#This program animates objects in 3D for physics simulations
from vpython import*
import math


# In[2]:



#print("Hello, GlowScript-VPython!")
#bright box
#box(pos=vector(1,0,0), size = vector(.5,.3,.2), color=vector(0.6,0.5,1))
#box(pos=vector(2,0,0), size = vector(.3,.5,.3), color=vector(0.2,0.7,0.4))
#box(pos=vector(3,0,0), size = vector(.3,.2,.3), color=vector(0.5,0.65,0.5))
#sphere(radius = 0.25)
#sphere(radius = 0.25, pos=vector(-1,0,0), color=vector(1,0,0))
yaxis = cylinder(pos=vector(0,-5,0), axis=vector(0,10,0),radius=0.01, color=vector(.4,.4,.4))
xaxis = cylinder(pos=vector(-5,0,0), axis=vector(10,0,0),radius=yaxis.radius, color=yaxis.color)
zaxis = cylinder(pos=vector(0,0,-5), axis=vector(0,0,10),radius=yaxis.radius,  color=yaxis.color)
#
#bar = cylinder(pos = vector(-2.5,-5,0), axis = vector(5,0,0), radius=0.2, color=vector(1,1,1))
#sphere(pos=bar.pos, color=bar.color)
#sphere(pos=bar.pos + bar.axis, color=bar.color)


# In[3]:


#set variables
#tablex = -2
#tabley= 0
#tablez = 2
#tablelength = 10
#tablewidth =12
#tableheight = 3
#legradius = tablewidth/10


# In[4]:


#table
#tablecolor=vector(1,1,1)
#box(pos=vector(tablex,tabley,tablez), size = vector(tablewidth,tableheight/3,tablelength),color=tablecolor)


# In[5]:


#legs
#cylinder(axis=vector(0,-10,0), pos=vector(tablex+tablewidth/2 - legradius,tabley,tablez+tablelength/2 - legradius), radius=legradius, color=tablecolor)

#cylinder(axis=vector(0,-10,0), pos=vector(tablex-tablewidth/2 + legradius,tabley,tablez-tablelength/2 + legradius), radius=legradius, color=tablecolor)

#cylinder(axis=vector(0,-10,0), pos=vector(tablex-tablewidth/2 + legradius,tabley,tablez+tablelength/2 - legradius), radius=legradius, color=tablecolor)

#cylinder(axis=vector(0,-10,0), pos=vector(tablex+tablewidth/2 - legradius,tabley,tablez-tablelength/2 + legradius), radius=legradius, color=tablecolor)


# In[6]:


#background
#scene.background  = color.white


# In[7]:


#Animation
#movingBox = box(pos=vector(-5,0,-5), size = vector(1,1,1))
#print("began")
#while movingBox.pos.x < 5:
   # rate(20)
    #movingBox.pos.x += 0.05
    #movingBox.pos.z += 0.05
    
#print("finished")


# In[3]:


#Run in a circle 
theta = 0

movingsphere = sphere(pos=vector(0,0,0), radius = 0.25, make_trail=True, trail_type="points", interval = 15)
print("begin")
graph(width=400, height=250, background = color.white, title="time versus x and y coordinates", ytitle = "x and y coordinates", xtitle = "time")
xDots = gdots(color=color.green)
yDots = gdots(color=color.magenta)
t=0
while theta <= 7:
    rate(20)
    theta += 0.05
    t+=1
    x = 5* cos(theta)
    y = 5* sin(theta)
    xDots.plot(t,x)
    movingsphere.pos = vector(x, y, 0)
    yDots.plot(t,y)
print("finished")


# In[ ]:




