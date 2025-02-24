# def say_hello():
#     print("say hello func")
#
# list1 = [1, "2", True, say_hello, 123]
#
# length = len(list1)
#
# print(length)
# print(list1[1])
#
list2 = []
# print(list2)
# # print(len(list2))
#

for i in range(10):
    list2.append(i)

print(list2)
#
# for i in range(len(list2)):
#     print(f"i = {i + 2}")
#
# somr_str = "Hello world"
#
# for i in somr_str:
#     print(i)
# <змінна>[<індекс>]

# counter = 0

# while True:
#     if counter > 25:
#         break
#
#     internal_val = counter / 2
#
#     counter += 1
#     print(f"counter = {counter}, internal_val = {internal_val}")




list3 = list2[-2:5:-1]
print(type(list3))
print(list3)



list3[1] = 18
print(list3)
print(list2)





print(list2[-1:5:-1])

list4 = [list3, list2]
print(list4)

list4_first_elem = list4[0][1]
print(list4_first_elem)
# list4_first_elem_second_elem =  list4_first_elem[1]
# print(list4_first_elem_second_elem)
# val = list4[0][1]
list4[0][2] = 19
print(list4)

list4[1].append(50)
print(list4)

for i in range(len(list4)):
    print(f"elem {i} of list4:")
    for j in list4[i]:
        print(f"\t{j}")


list123 = [1, 2, 3,4 ,5]
list123.insert(3, 16)
print(list123)