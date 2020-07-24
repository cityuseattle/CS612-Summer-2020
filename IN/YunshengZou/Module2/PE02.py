def CalTriangle(isPerimeter, li=[]):
    if(li!=[] and len(li)==3):
        x1,y1 = li[0]
        x2,y2 = li[1]
        x3,y3 = li[2]
        dis1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
        dis2 = ((x1-x3)**2 + (y1-y3)**2)**0.5
        dis3 = ((x2-x3)**2 + (y2-y3)**2)**0.5
        if(dis1+dis2>dis3 and dis2+dis3>dis1):
            if(isPerimeter):
                per = dis1+dis2+dis3
                print("The perimeter is: " + str(per))
            else:
                area = abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2) / 2
                print("The area is: " + str(area))
        else:
            return "This is not a triangle!"

CalTriangle(True,[(1,2),(3,-2),(2,-0.5)])
CalTriangle(False,[(1,2),(3,-2),(2,-0.5)])