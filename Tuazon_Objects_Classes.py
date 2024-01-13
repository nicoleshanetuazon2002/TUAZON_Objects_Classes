print("Created By: Nicole Shane P. Tuazon")
print("BSCS - 1E")
print("--------------")

class Circle:
   def __init__(self,area, perimeter):
       self.area = area
       self.perimeter = perimeter
circle = Circle(area=0, perimeter=1)
radius = eval(input("Type radius(in meters) here : "))

area = (3.14 * radius ) ** 2
perimeter = 2 * 3.14 * radius
print("Area :" , area)
print("Perimeter :" , perimeter)



