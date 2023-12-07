answ = 432#答案寬度
ansh = 263#答案高度
ansx = 41#答案x座標
ansy = 93#答案y座標

x = 22#答題寬度
y = 72#答題高度
w = 471#答題x座標
h = 309#答題y座標
level = ''

gedgex = ansx*0.9
gedgey = ansy*0.9
gedgew = answ*1.03
gedgeh = ansh*1.03

nedgex = ansx*0.7
nedgey = ansy*0.7
nedgew = answ*1.07
nedgeh = ansh*1.07




#left-top
x = x
y = y
ansx = ansx
ansy = ansy
gedgex = gedgex
gedgey = gedgey
nedgex = nedgex
nedgey = nedgey
ltdis = ((x-ansx)**2+(y-ansy)**2)**0.5
gansltdis = ((gedgex-ansx)**2+(gedgey-ansy)**2)**0.5
nansltdis = ((nedgex-ansx)**2+(nedgey-ansy)**2)**0.5

#right-top
rtx = x+w
rty = y
ansrtx = ansx+answ
ansrty = ansy
gedgertx = gedgex+gedgew
gedgerty = gedgey
nedgertx = nedgex+nedgew
nedgerty = nedgey


rtdis = ((rtx-ansrtx)**2+(rty-ansrty)**2)**0.5
gansrtdis = ((gedgertx-ansrtx)**2+(gedgerty-ansrty)**2)**0.5
nansrtdis = ((nedgertx-ansrtx)**2+(nedgerty-ansrty)**2)**0.5

#left-bottom
lbx = x
lby = y+h
anslbx = ansx
anslby = ansy+h
gedgelbx = gedgex
gedgelby = gedgey+gedgeh
nedgelbx = gedgex
nedgelby = gedgey+gedgeh

lbdis = ((lbx-anslbx)**2+(lby-anslby)**2)**0.5
ganslbdis = ((gedgelbx-anslbx)**2+(gedgelby-anslby)**2)**0.5
nanslbdis = ((nedgelbx-anslbx)**2+(nedgelby-anslby)**2)**0.5

#right-bottom
rbx = x+w
rby = y+h
ansrbx = ansx+w
ansrby = ansy+h
gedgerbx = gedgex+gedgew
gedgerby = gedgey+gedgey
nedgerbx = nedgex+nedgew
nedgerby = nedgey+nedgey


rbdis = ((rbx-ansrbx)**2+(rby-ansrby)**2)**0.5
gansrbdis = ((gedgerbx-ansrbx)**2+(gedgerby-ansrby)**2)**0.5
nansrbdis = ((nedgerbx-ansrbx)**2+(nedgerby-ansrby)**2)**0.5



if ltdis<gansltdis and rtdis<gansrtdis and lbdis<ganslbdis and rbdis<gansrbdis:
    level = '優'
elif ltdis<nansltdis and rtdis<nansrtdis and lbdis<nanslbdis and rbdis<nansrbdis:
    level = '普通'
else :
    level = '劣'

 
print(level)