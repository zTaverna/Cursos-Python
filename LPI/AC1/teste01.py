import math
a=float(input())
b=float(input())
c=float(input())
d=float(input())

i = ((a**2+3*b)/c)+d
print("i)", round(i, 4))

ii = math.log10(a)+(math.e**(-b/c))-((d**2)/math.pi)
print("ii)", round(ii, 4))

iii = (((a**2)**(1/3))*(b**(1/3))+(c*d))/(a+b+c+d)
print("iii)", round(iii, 4))

iv = ((a+b)*(c+d))/(a*b*c*d)
print("iv)", round(iv, 4))

v = ((a*a+b*b)/(c*d))-((c*c+d*d)/(a*b))
print("v)", round(v, 4))

vi = (a+b+c+d)**2
print("vi)", round(vi, 4))

vii = (a**2)+(b**2)+(c**2)+(d**2)
print("vii)", round(vii, 4))

viii = (a*b*c*d)**(1/3)
print("viii)", round(viii, 4))
