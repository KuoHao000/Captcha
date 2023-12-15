import cv2
#以影像識別來獲取答案數據
ansimg = cv2.imread('cat_cert_1.jpg')
# haerinimg = cv2.resize(haerinimg, (0,0), fx = 0.5, fy= 0.5)
ansgray = cv2.cvtColor(ansimg, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('cat_detect.xml')
faceRect = faceCascade.detectMultiScale(ansgray, 1.1, 6)
print(len(faceRect))
# for(x, y, w, h) in faceRect:
#     cv2.rectangle(ansimg, (x, y), (x+w, y+w), (0, 255, 0), 2)
#     print(x)
#     print(y)
# cv2.imshow('cat2', ansimg)
# cv2.waitKey(0)

for(x, y, w, h) in faceRect:
    cv2.rectangle(ansimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x)
    print(y)
    print(w)
    print(h)

ansx = x
ansy = y
answ = w
ansh = h

# cv2.imshow('haerin', haerinimg)
# cv2.waitKey(0)

# ansx = 27#答案x座標
# ansy = 134#答案y座標
# answ = 502#答案寬度
# ansh = 351#答案高度

x = 172#答題x座標
y = 212#答題y座標
w = 150#答題寬度
h = 149#答題高度

# x = 91  y:  154.75  width:  481  height:  337.5



gedgex = ansx*0.9#外放優良答案x座標
gedgey = ansy*0.9#外放優良答案y座標
gedgew = answ*1.03#外放優良答案寬度
gedgeh = ansh*1.03#外放優良答案高度

# gedgex = ansx#外放優良答案x座標
# gedgey = ansy#外放優良答案y座標
# gedgew = answ#外放優良答案寬度
# gedgeh = ansh#外放優良答案高度

nedgex = ansx*0.7#外放普通答案x座標
nedgey = ansy*0.7#外放普通答案y座標
nedgew = answ*1.07#外放普通答案寬度
nedgeh = ansh*1.07#外放普通答案高度

# nedgex = ansx*0.9#外放普通答案x座標
# nedgey = ansy*0.9#外放普通答案y座標
# nedgew = answ*1.04#外放普通答案寬度
# nedgeh = ansh*1.04#外放普通答案高度

gedgex2 = ansx*1.1#內縮優良答案x座標
gedgey2 = ansy*1.1#內縮優良答案y座標
gedgew2 = answ*0.97#內縮優良答案寬度
gedgeh2 = ansh*0.97#內縮優良答案高度

nedgex2 = ansx*1.3#內縮普通答案x座標
nedgey2 = ansy*1.3#內縮普通答案y座標
nedgew2 = answ*0.93#內縮普通答案寬度
nedgeh2 = ansh*0.93#內縮普通答案高度

level = ''

#left-top
x = x
y = y
ansx = ansx
ansy = ansy
gedgex = gedgex
gedgey = gedgey
nedgex = nedgex
nedgey = nedgey
gedgex2 = gedgex2
gedgey2 = gedgey2
nedgex2 = nedgex2
nedgey2 = nedgey2

ltdis = ((x-ansx)**2+(y-ansy)**2)**0.5
gansltdis = ((gedgex-ansx)**2+(gedgey-ansy)**2)**0.5
nansltdis = ((nedgex-ansx)**2+(nedgey-ansy)**2)**0.5
gansltdis2 = ((gedgex2-ansx)**2+(gedgey2-ansy)**2)**0.5
nansltdis2 = ((nedgex2-ansx)**2+(nedgey2-ansy)**2)**0.5

#right-top
rtx = x+w
rty = y
ansrtx = ansx+answ
ansrty = ansy
gedgertx = gedgex+gedgew
gedgerty = gedgey
nedgertx = nedgex+nedgew
nedgerty = nedgey
gedgertx2 = gedgex2+gedgew2
gedgerty2 = gedgey2
nedgertx2 = nedgex2+nedgew2
nedgerty2 = nedgey2

rtdis = ((rtx-ansrtx)**2+(rty-ansrty)**2)**0.5
gansrtdis = ((gedgertx-ansrtx)**2+(gedgerty-ansrty)**2)**0.5
nansrtdis = ((nedgertx-ansrtx)**2+(nedgerty-ansrty)**2)**0.5
gansrtdis2 = ((gedgertx2-ansrtx)**2+(gedgerty2-ansrty)**2)**0.5
nansrtdis2 = ((nedgertx2-ansrtx)**2+(nedgerty2-ansrty)**2)**0.5

#left-bottom
lbx = x
lby = y+h
anslbx = ansx
anslby = ansy+h
gedgelbx = gedgex
gedgelby = gedgey+gedgeh
nedgelbx = gedgex
nedgelby = gedgey+gedgeh
gedgelbx2 = gedgex2
gedgelby2 = gedgey2+gedgeh2
nedgelbx2 = gedgex2
nedgelby2 = gedgey2+gedgeh2

lbdis = ((lbx-anslbx)**2+(lby-anslby)**2)**0.5
ganslbdis = ((gedgelbx-anslbx)**2+(gedgelby-anslby)**2)**0.5
nanslbdis = ((nedgelbx-anslbx)**2+(nedgelby-anslby)**2)**0.5
ganslbdis2 = ((gedgelbx2-anslbx)**2+(gedgelby2-anslby)**2)**0.5
nanslbdis2 = ((nedgelbx2-anslbx)**2+(nedgelby2-anslby)**2)**0.5

#right-bottom
rbx = x+w
rby = y+h
ansrbx = ansx+w
ansrby = ansy+h
gedgerbx = gedgex+gedgew
gedgerby = gedgey+gedgey
nedgerbx = nedgex+nedgew
nedgerby = nedgey+nedgey
gedgerbx2 = gedgex2+gedgew2
gedgerby2 = gedgey2+gedgey2
nedgerbx2 = nedgex2+nedgew2
nedgerby2 = nedgey2+nedgey2

rbdis = ((rbx-ansrbx)**2+(rby-ansrby)**2)**0.5
gansrbdis = ((gedgerbx-ansrbx)**2+(gedgerby-ansrby)**2)**0.5
nansrbdis = ((nedgerbx-ansrbx)**2+(nedgerby-ansrby)**2)**0.5
gansrbdis2 = ((gedgerbx2-ansrbx)**2+(gedgerby2-ansrby)**2)**0.5
nansrbdis2 = ((nedgerbx2-ansrbx)**2+(nedgerby2-ansrby)**2)**0.5

#範圍判斷
if ltdis<=gansltdis and rtdis<=gansrtdis and lbdis<=ganslbdis and rbdis<=gansrbdis or ltdis<=gansltdis2 and rtdis<=gansrtdis2 and lbdis<=ganslbdis2 and rbdis<=gansrbdis2:
    level = '優'
elif ltdis<=nansltdis and rtdis<=nansrtdis and lbdis<=nanslbdis and rbdis<=nansrbdis or ltdis<=nansltdis2 and rtdis<=nansrtdis2 and lbdis<=nanslbdis2 and rbdis<=nansrbdis2:
    level = '普通'
else :
    level = '劣'

print(level)