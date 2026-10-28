# functions
import random

# from my_functions import greet
import  my_functions

# a= append w= write
with open("data.txt", "a") as file:
    # file.write("99\n")
    # file.write("68\n")
    for temp in range(100):
        x = random.randint(-10, 65)
        file.write(str(x)+"\n")

with open("data.txt", "r") as file:
    content = file.read() # 0 params 0 args
    print(content)

# install
# use

my_functions.greet()

from my_functions import greet

greet()