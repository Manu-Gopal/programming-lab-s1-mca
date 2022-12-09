from graphics import circle,rectangle
from graphics.graphics_3d import sphere,cuboid

a=int(input("enter the radius"))
print("area=",circle.area(a))
print("perimeter=",circle.perimeter(a))

b=int(input("enter the breadth"))
l=int(input("enter the length"))
print("area=",rectangle.area(l,b))
print("perimeter=",rectangle.perimeter(l,b))

r=int(input("enter the radius of sphere"))
print("area=",sphere.area(r))
print("perimeter=",sphere.perimeter(r))

ln=int(input("enter the length of cuboid"))
br=int(input("enter the breadth of cuboid"))
h=int(input("enter the height of cuboid"))
print("area=",cuboid.area(ln,br,h))
print("perimeter=",cuboid.perimeter(ln,br,h))
