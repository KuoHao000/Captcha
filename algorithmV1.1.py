w = 432
h = 263
x = 41
y = 93
ansx = 45
ansy = 97
level = ''

#left-top
x = x
y = y
ansx = ansx
ansy = ansy
ltdis = ((x-ansx)**2+(y-ansy)**2)**0.5

#right-top
rtx = x+w
rty = y
ansrtx = ansx+w
ansrty = ansy
rtdis = ((rtx-ansrtx)**2+(rty-ansrty)**2)**0.5

#left-bottom
lbx = x
lby = y+h
anslbx = ansx
anslby = ansy+h
lbdis = ((lbx-anslbx)**2+(lby-anslby)**2)**0.5

#right-bottom
rbx = x+w
rby = y+h
ansrbx = ansx+w
ansrby = ansy+h
rbdis = ((rbx-ansrbx)**2+(rby-ansrby)**2)**0.5

if ltdis and rtdis and lbdis and rbdis <=5:
    level = '優'
elif 6<=ltdis or rtdis or lbdis or rbdis<12:
    level = '普通'
else :
    level = '劣'

 



print(level)