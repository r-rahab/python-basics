# store lots data

# data structures
# list, set, tuple, dictionary

people = ["Jack", "Jane", "Ahmed", "Hussein", "Mariam"]
scores = [87, 45, 67, 52, 91, 29, 66, 71, 81]
# print(people[0])
# print(scores[0])
# print(people[-1]) # last value
#
# people.append("Willis")
# print(people)
# scores.append(44)
# print(scores)
# people.clear()
# people.sort()
# scores.sort(reverse=True)
# print(people)
# print(scores)
#
# print(scores[0], scores[-1])
# print( sum(scores) / len(scores) )
# print(scores.count(88))

scores.sort()
# slicing
# print(scores)
# print(scores[-3:])
# print(scores[0:3])
# print(scores[3:5]) #

# set -- remove duplicates
numbers = {87, 89, 87, 67, 54}
print(numbers)

# Tuple -- immutable data
days = ("Mon", "Tue", "Fri")
print(days[0])

# dictionary key + value
person = {"name": "Zillow", "city": "Marsabit", "age": 19}
print(person["name"])

# data structures + algorithms
print(sum(numbers))

watu = [{"name": "Sila", "age": 22},
        {"name": "Hin", "age": 59},
        {"name": "Cril", "age": 16}]

print(watu[1]["name"])

#loops