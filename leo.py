# num1 = float(input("enter the fast number: "))
# num2 = float(input("enter thr second number: "))
# sum = num1 + num2
# print(f"{num1} + {num2} = {sum}")
# num3 = float(input("enter the dividend for the division: "))
# num4 = float(input("enter the divisisor for the division: "))
# if num4 == 0:
#     print("error! division by zero is not allowed.")
# else:
#     div_results = num3/num4
#     print(f"{num3}/{num4} = {div_results}") 
           

# numbers[0] = 45
# print(numbers)  
# print(30 in numbers) 
# numbers = [10,20,30,40,50] 
# for n in range(len(numbers)):
#     numbers[n] = numbers[n] * 2
#     print(numbers) 
# numbers_org =[50,55,60,65,70,75]
# numbers = numbers_org[:]
# for n in range(len(numbers)):
#     numbers[n] = numbers[n] * 5
#     print(numbers)
# numbers_2 = [90,95,100]
# num_3 = numbers + numbers_2
# # print(num_3*4)
# #slicing the lists 
# print(num_3[0:5])
# print(num_3[:])
# #list methods 
# num_3.sort()
# print(num_3)

# total = 0
# count = 0
# while True:
#     inp = input("enter numbers to be added  ")
#     if inp == "done":
#         break
#     number = float(inp)
#     total = total + number
#     count = count + 1
# average = total / count
# print(f"average = {average}")    

# name = "selemani"
# name_c = list(name)
# print(name_c)
# sms = "hey guys how are you"
# t = sms.split()
# print(t)

# sms = "hey-my-name-is-selemani "
# delimiter = "-"
# t = sms.split(delimiter)
# print(f"t = {t}")
# delimiter = "-"
# y = delimiter.join(t)
# print(f"y = {y}")

# defing function
# def intro():
#     print("my name is selemani mtahukile")
#     print("i come from mtwara")
#     print("i have six years old")
# intro() 
# def inte(selemani):
#     print(selemani)
#     print(selemani)
# inte("juma")
# def delete_head(t):
#     del t[0]
# numbers = [20,30,40,50,60]
# delete_head(numbers)
# print(numbers)
# t1 = [1,2,3]
# t1.append(4)
# t2 = t1 + [4]
# print(t2)
# def chop(s):
#     if len(s) > 0:
#         del s[0]
#         del s[-1]
#     else:
#         del s[0]
# numbers = [1,2,3,4,5,6]
# chop(numbers) 
# print(numbers)

# def middle(f):
#     if len(f) > 0:
#         return f[1:-1]
# num = [22,33,44,55,66]
# n = middle(num)  
# print(n) 
# print(num)

# name = "selemani"
# age = 20
# weight = 55.8
# details = f"my name is {name}, ninaumri wa miaka {age} na uzito wa {weight}kg"
# print(details)

# radius = float(input("enter the radius of a circle  "))
# import math
# area = math.pi * (radius**2)
# print(f"the area of that cicle is {area} square unit")
# s = "jifunze python kwa bidii"
# k = s.upper()
# print(k)
# print(len(k))
# print(k[8:14])

# fruits = ["apple" , "banana" , "cherry"]
# fruits.append("orange")
# fruits[1] = "kenya banana"
# fruits.remove("apple")
# print(fruits)

# numbers = [38,5,6,77,88]
# total = sum(numbers)
# counts = len(numbers)
# average = total / counts
# print(f"average of numbers is {average)
# kapu = []
# idadi = 0
# jumla = 0
# jumla_kuu = 0
# while True:
#     control=int(input('ingiza 1 kuendelea na 0 kutoka'))
#     if control == 0:
#         break
#     else:
#         try:
#             bidhaa = input("\ningiza jina la bidhaa  ")
#             bei = float(input("ingiza bei ya bidhaa  "))
#             idadi_1= int(input("ingiza idadi ya bidhaa  "))
#             subtotal = bei * idadi
#             bidhaa_moja ={
#                 bidhaa,
#                 bei,
#                 idadi_1
#             }   
#             kapu.append(bidhaa_moja)
#             jumla_kuu = jumla_kuu + subtotal
#             kodi = jumla_kuu * 0.18
#             jumla = jumla_kuu + kodi
#             idadi = idadi + idadi_1
#         except:
#             print("Tafadhali! ingiza namba tu")
#         # continue
# print("\n" + "=" * 20)
# print(f"{'RISITI YAKO':^20}")
# print("=" * 20)
# from datetime import datetime
# tarehe = datetime.now()
# formated = tarehe.strftime("%d-%m-%Y")
# muda = tarehe.strftime("%H:%M:%S")
# print(f"Tarehe:  {formated}")
# print(f"Muda:  {muda}")
# print(f"Bidhaa:  {kapu}")
# # print(f"Bei:  {bei:.2f}")
# print(f"Idadi:  {idadi}")
# print(f"VAT(18%):  {kodi}")
# print("=" * 20)
# print(f"Jumla:  {jumla:.2f}")
# print("Asante kwa kununua")

# saizi = dict()
# print(saizi)
# data = dict(jina ="alli", age =20)
# print(data)
# mamilo = [("jina", "alli") ,("age", 20)]
# mamilo_i = dict(mamilo)
# print(mamilo_i)
# bidhaa = dict(jina = "sukari",bei = 2500 ,idadi = 2)
# jumla = bidhaa["bei"] * bidhaa["idadi"]
# print(bidhaa)
# print(f"jumla:  {jumla}")
current_year = 2026
details = input("enter data\n")
try:
    parts = details.split(",")
    if len(details) != 4:
        print("wrong input format")
    else:
        name = parts[0] 
        try:
            year_of_birth = int(parts[1])  
            monthly_salary = float(details[2])
        except:
            print("value error")
            exit()
        active_str = parts[3].strip() 
        if active_str == "True":  
            active = True
        elif active_str == False:
            active = False
        else:
            print("wrong input format") 
            exit() 
        age = current_year - year_of_birth
        qualified =(
            age >= 21 and age <= 35
            and monthly_salary >= 3000000
            and active
        )       
        if qualified:
            print("name:" , name)   
            print("Age:" , age)   
            print("Status:" ,qualified)
        else:
            print("status not qualified")
                  
except:
    print("wrong input!!!")        
