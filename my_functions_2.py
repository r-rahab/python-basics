def add(x, y, z):
    return x + y + z


def addition(*nums):
    # total = sum(nums)
    total = 0
    for num in nums:
        total = total + num
    return total


# key and word arguments **kwargs
def save(**data):
    with open("values.txt", "w") as file:
        for key, value in data.items():
            file.write(f"{key} : {value}\n")


def some_function(name, *scores, **details):
    pass


def cylinder(r, h):
    """
      Calculates the volume and SA of a cylinder
      Parameters
       radius and height of the cylinder
      :returns: volume and Surface Area of the cylinder
    """
    v = 22 / 7 * r * r * h
    sa = 22 / 7 * r ** 2 * 2 + 22 / 7 * r * 2 * h
    return sa, v


surf_area, volume = cylinder(7, 15)

print(surf_area, volume)

sum([1, 2, 3])

# lambda functions


# lambda x, y : x/y
divider = lambda x, y: x / y

area_circle = lambda r: 22 / 7 * r * r


print(divider(45, 7))
res = area_circle(5)
print(res)





# some_function("Hellen", 10,90,85, gender='Female', course='Chem')
#
# # save(age=18, dob='2001-12-31', proffession='Engineer')
#
# save(dob='2025-01-18', gender='Female', color='Black', name='Kim')

# print(addition(9, 10, 100, 67.88, 89, 56, 78))
# print(addition(90,100))

# res = add(1, 2, 3) # 3 args/params
# print(res)
# data = {"name":"Ken", "gender":"Male"} #[1, 2, 3]
# for _,v in data.items():
#     print(v)


# TODO functions as a parameter