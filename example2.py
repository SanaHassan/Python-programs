# import math
# x=1
# y=2.4
# z=2+3j
#
# print(type(z))
# result=x+y
# print(result)
# print(math.ceil(y))

# # #Learning List in Python
# # our_list=["a","b","c",1.4]
# # print(our_list)
# # our_list.append("d")
# # print(our_list)
# # print(our_list[3])
# # our_list.insert(0,"first Element")
# # print(our_list)
# # our_list.remove("first Element")
# # print(our_list)
# # our_list.pop(4)
# # print(our_list)


# #Strings in Python

# string_a ="Sana"
# print(string_a)
# print(len(string_a))
# print(string_a.lower())
# print(string_a.upper())
# string_b =" Sana , Asjad ,Salahuddin"
# print(string_b.split(","))

#Dictionary in Python

# our_dictionary={"Name":"Sana","Height":"5'6"}
# print(our_dictionary)
# print(our_dictionary["Name"])
# our_dictionary["Name"]="Natasha"
# print(our_dictionary)
# print(our_dictionary)
# print(our_dictionary.pop("Height"))
# print(our_dictionary)

#IF ELSE in Python
# x = 1
# y = 2


# z = 3
#
# if x<y or y > z:
#     print("Yes!")

# else:
#     print("Victory!")


#WHILE LOOP in  Python

# x = 1
# while x<10:
#     x=x+1
#     print(x)

# FOR LOOP IN Python

# name = "Sana"
# for elements in name:
#     print(elements)
#
# our_list = ["Sana ","Asjad","Salahuddin",3.55,3.45]
# for names in our_list:
#     print(names)
#
# our_listb = [1,2,3,4,5]
# for number in our_listb:
#     print(5)

#FUNCTIONS IN Python

# def add_two_six(x):
#     result=x + 2.6
#     print(result)
#
# amount = add_two_six(8)
#
# def addition(x,y):
#     add= x + y
#     print(add)
#
# result1 = addition(3,2)

#OBJECTS IN Python
#
# print("HELLO")
# print('hello')
# print('''Dear john i was thing ke you are a good person you should start
# believing in yourself ''')
# print('hello'.upper())
# print('hElLo'.lower())


#FUNCTIONS in Python
#
# def hello():
#     print("Hello World")


# def pypart(n):
#     our_list=[]
#     for i in range(1,i+1):
#         our_list.append("*"*i)
#         print("\n".join(our_list))
#
#         #
#         # for j in range(0,i+1):
#         #     print(f"{j+1}",end="")
#
#
#         # print("\r")
#
# n=int(input("Enter the range of pyaramid: "))
# print(type(n))
#
# pypart(n)

#
# number=[1,2,3]
# square=[]
# for elements in number:
#     square.append(elements**2)
#

# print(square)

Number=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
odd_list=[]
for elements in Number:
    if (elements%2==0):
        print("Even",elements)
        even_list.append(elements)
    else:
        print("ODD",elements)
        odd_list.append(elements)

print("------------------------------------------List of ODD AND EVEN--------------------------------------")
print(f"\t\t Odd Element : {odd_list}\t\tEven Element : {even_list}\t\t")
