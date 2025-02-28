from math import pi, factorial
from traceback import print_list

fact = factorial(10)
import string
from keyword import kwlist

print(string.punctuation)
print(fact)
print(kwlist)
some_string = "Hello, my name is Serhii"

delimiter = "e"
string_list = some_string.split(delimiter)  # перетворює рядок на список елементів, розділених дільником
print(string_list)

recovered_string = "e".join(string_list)  # "".join({список строк})
# recovered_string = delimiter.join(string_list)
print(recovered_string)

recovered_string = "   " + recovered_string + "\t"
print(recovered_string)

stripped_string = recovered_string.strip()  # lstrip(), rstrip(), strip() - видалення всіх пробільних символів покраям строки
print(stripped_string)


lower_string = stripped_string.lower()
print(lower_string)

upper_string = stripped_string.upper()
print(upper_string)

cptlzd_string = stripped_string.capitalize()
print(cptlzd_string)

print(cptlzd_string.startswith("56"))

print(stripped_string.isdigit())
dogit_string = "56"
print(dogit_string.isdigit())


a = float("56.5")
print(a)


num = input("enter the float num: ")

num = float(num.replace(",", ".").replace(" ", ""))
print(num)

sliceed = recovered_string[4:-3]
print(sliceed)

print(recovered_string[10])

lst = [i for i in range(10)]

third = lst.pop(3)
print(lst)
print(third)

lts2 = [i for i in lst if i % 2 == 0 and i !=0]

print(lts2)
punctuation