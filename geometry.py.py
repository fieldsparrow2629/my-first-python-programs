import math

def triangle_area(b,h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

print(triangle_area(4,9))
print(circle_area(5))

def parallel(b,h):
    return (b*h)

def trapezoid(a,b,h):
    area = (a+b)*h/2
    return area

def rect_prism_vol(l,w,h):
    return(l*w*h)

def cone(r,h):
    vol = math.pi * r**2 * h/3
    return vol
    
def vol_sphere(r):
    return((4/3)*math.pi * r**3)

def surface_rect_prism(l,w):
    return(6*l*w)

def surface_sphere(r):
    return(4*math.pi*r**2)

def hypo(s1,s2):
    hypo = math.sqrt(s1**2 + s2**2)
    return hypo

def heron(a,b,c):
    p = (a + b + c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

print(heron(3,4,6))
print(hypo(7,4))
print(trapezoid(4,5,6))
print(surface_sphere(5))
print(surface_rect_prism(3,90))
print(vol_sphere(45))
print(cone(45,60))
print(rect_prism_vol(34,33,12222))
print(trapezoid(100000,1341414123123,15585858585858))
print(parallel(123123123123123123123123123123123123,12312312312312312312312312312312312313))


