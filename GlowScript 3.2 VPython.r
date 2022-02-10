GlowScript 3.2 VPython
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
tablex = -2
tabley= 0
tablez = 2
tablelength = 10
tablewidth =12
tableheight = 3
legradius = tablewidth/10
tablecolor=vector(1,1,1)
box(pos=vector(tablex,tabley,tablez), size = vector(tablewidth,tableheight/3,tablelength),color=tablecolor)
cylinder(axis=vector(0,-10,0), pos=vector(tablex+tablewidth/2,tabley,tablez+tablelength/2), radius=legradius, color=tablecolor)