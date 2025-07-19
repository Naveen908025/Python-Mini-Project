print("Area and Volume Calculator")
print("Choose The shape\n"
      "1.Circle\n"
      "2.Rectangle\n"
      "3.Square\n"
      "4.Triangle\n"
      "5.Cube\n"
      "6.Cuboid\n"
      "7.Sphere\n"
      "8.Cone\n")
shape = input("Enter the shape Number:")
if shape == "1":
    radius=float(input("Enter The Radius"))
    area = 3.14*radius*radius
    volume=None
    print(f"Area of the Circle:{area}")
elif shape == "2":
    length=float(input("Enter The length"))
    width=float(input("Enter The width"))
    area = width*length
    volume=None
    print(f"Area of the Rectangle:{area}")
elif shape == "3":
    side=float(input("Enter The Side"))
    area = side*side
    volume=None
    print(f"Area of the Square:{area}")
elif shape == "4": 
    base=float(input("Enter The base"))
    height=float(input("Enter The height"))
    area = 0.5*base*height
    volume=None
    print(f"Area of the Triangle:{area}")
elif shape == "5":
    side = float(input("Enter the side of the cube: "))
    area = 6 * side * side
    volume = side * side * side
    print(f"Area of Cube: {area}, Volume of Cube: {volume}")
elif shape == "6":
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    area = 2 * (length * width + width * height + height * length)
    volume = length * width * height
    print(f"Area of Cuboid: {area}, Volume of Cuboid: {volume}")
elif shape == "7":
    radius = float(input("Enter the radius of the sphere: "))
    area = 4 * 3.14 * radius * radius
    volume = (4/3) * 3.14 * radius**3
    print(f"Area of Sphere: {area}, Volume of Sphere: {volume}")
elif shape == "8":
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    area = 3.14 * radius * (radius + (height**2 + radius**2)**0.5)
    volume = (1/3) * 3.14 * radius * radius * height
    print(f"Area of Cone: {area}, Volume of Cone: {volume}")

else:
    print("Invalid shape number entered.")
