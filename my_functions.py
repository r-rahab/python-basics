# functions
#import math


def greet():
    print("Hello, welcome to python")

def greeting(user):
    print(f"Hello {user}, welcome to python")

def area_circle(radius, precision=3):
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)


def volume_cylinder(r, h):
    v = 22/7 * r * r * h
    return v


print(volume_cylinder(8.5, 12.8))

res = volume_cylinder(6, 19)
print(round(res))


# named params
# area_circle(precision=2, radius=11)


# area_circle(2.9, 2) # positional params
# area_circle(6.11, 0)
# area_circle(8)

# use == call
# greet()
# greet()
# greet()

#params/ args
# greeting("Jim")
# greeting("Ahmed")