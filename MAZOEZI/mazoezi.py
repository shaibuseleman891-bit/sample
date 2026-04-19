# numbers = [1,2,3,4,5]
# def added_ten(n):
#     return n + 10
# results = list(map(added_ten, numbers))
# print(results)


# names = ['juma', 'saidi', 'habiba', 'mwajuma']
# names_upper = list(map(str.upper, names))
# print(names_upper)


# numbers = [2,3,4,5]
# def squared_number(n):
#     return n**2
# numbers_squared = list(map(squared_number, numbers))
# print(numbers_squared)


# numbers = [1,2,3,4,5]
# def converted(n):
#     return str(n)
# print(list(map(converted, numbers)))


# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,0]
# def combined(x,y):
#     return x +y
# matokeo = list(map(combined, list1, list2))
# print(matokeo)


# words = ['python', 'programmng', 'map']
# majibu = list(map(str.__len__, words))
# for name, count in zip(words, majibu):
#     print(f'{name} = {count}')
    

# fahreiheit = [50,60,70,80,90]
# def converted(temp):
#     return f'{((temp - 32) * 5/9):.2f}'
# converted_temp = list(map(converted, fahreiheit))
# print(converted_temp) 

    
    
# my_list = [' hello ', ' word ' ,' python ']
# new = list(map(str.strip, my_list))
# print(new)

# students_scores = [(80, 90, 100), (70,85,90), (60, 75, 80)]
# def total(scores):
#     return  sum(scores)
# results = list(map(total, students_scores))
# print(results)

# numbers = [-2, 0, 5, 10,-7]
# def datatype(n):
#     if n > 0:
#         return True
#     else:
#         return False
# datatypes = list(map(datatype, numbers))
# print(datatypes)



# import math
# from turtle import *

# tracer(10)
# bgcolor('white')

# for i in range(4300):
#     color('blue')
#     t = i/46
#     x = 25 * math.cos(7*t) * math.sin(t)
#     y = 25 * math.sin(7*t) * math.cos(t)
#     goto(x*10, y*10)
#     goto(0,0)
# done()  y


rows = 5
for i in range(1,rows + 1):
    print(' ' * (rows-i) + '*' * (2*i-1))


    

    
      
   
    