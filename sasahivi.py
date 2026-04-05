# kodi_jumla = 0 
# jumla_kuu = 0
# bidhaa_zote = []
# from datetime import datetime
# while True:
#     control = int(input("ingiza 1 ili kuingiza bidhaa nyingine na 0 kumaliza"))
#     if control == 1:
#         break
#     try:
#         bidhaa = input("ingiza jina la bidhaa ")
#         bei = float(input("ingiza bei ya bidhaa "))
#         idadi = int(input("ingiza idadi ya bidhaa "))
#         kiasi = bei * idadi
#         kodi = 0.18 * kiasi
#         jumla = kodi + kiasi
#         jumla_kuu += jumla 
#         kodi_jumla += kodi 
#         bidhaa_zote.append((bidhaa,bei,idadi,jumla))
#     except:
#         print("Tafadhali! ingiza namba...") 
#         exit()   
# tarehe = datetime.now()
# tarehe_m = tarehe.strftime("%d-%m-%Y") 
# muda = tarehe.strftime("%H:%M:%S")
# print("\n" + "="*40)
# print(f"{'SELEMANI MIX SHOP':^40}")
# print(f"{'SIMU: 06230017380':^40}")
# print("="* 40)
# print(f"Tarehe:  {tarehe_m}")
# print(f"Muda:  {muda}")
# print("-"*40)
# print(f"{'Bidhaa':<15}{'Bei':>7}{'Idadi':>8}{'jumla':>10}") 
# for b in bidhaa_zote:
#     print(f"{b[0]:<15}{b[1]:>7}{b[2]:>8}{b[3]:>10}")
# print("-" * 40)
# print(f"VAT(18%):  {kodi_jumla}")
# print("=" * 40)
# print(f"JUMLA KUU:  {jumla_kuu}")
# print(f"{'ASANTE KWA KUNUNUA':^40}")
# print("="* 40)




# i =  1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("done")
# secret_number = 9
# guess_count = 0 
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("guess  "))
#     guess_count += 1
#     if guess == secret_number:
#         print("you won!")
#         break
# else:
#     print("oh you failed!!!")

# command = "" 
# started = False
# while True:
#     command = input(">")
#     if command == "start":
#         if started :
#             print("hey the car is already started!!!")
#         else:
#             started = True 
#             print("car started...")    
#     elif command == "stop":
#         if not started:
#             print("the car has already stopped") 
#         else: 
#             started = False    
#             print("car stopped!")
#     elif command == "help":
#             print("""
# start - to start the car 
# stop - to stop the car
# quit - to quit 
#             """)
#     elif command == "quit":
#         break      
#     else:              
#         print("hey i don't understand that!!!")

# for i in range(100, 200, 15):
#     print(i)
# prices = [10, 20, 30]
# total = 0    
# for a in (prices):
#     total += a
# print(f"total prices:  {total}")    

            #nested loops
# for x in range(2):
#     for y in range(2):
#         print(f"({x} , {y})")

# numbers = [5,2,5,2,2]  
# for x_ount in numbers:
#     output = " "
#     for count in range(x_ount):
#         output += "x"
#     print(output)     

# numbers = [5,2,5,2,2,10]
# lagest_number = numbers[0] 
# for number in numbers:      
#     if number > lagest_number:
#         lagest_number = number 
# print(lagest_number) 

# matrix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]  
# matrix[0][2] = 5 
# print(matrix[0][2])

# command = input(">")
# started = False
# while True:
#     command = input(">")
#     if command == "start":
#         if started:
#             print("hey the car the car is already started")
#         else:
#             started = True
#             print("car started ...")
#     elif command == "stop":
#         if  not started: 
#             print("hey the car is already stopped!")
#         else:
#             started = False
#             print("car stopped!")\
                    
#     elif command == "quit":       
#         break
#     elif command == "help":
#         print("""
# start - to start the car 
# stop - to stop the car 
# quit - to quit               
#               """)  
# else:
#     print("hey i dont understand what you are doing!"

# import calendar
# year = 2026
# month = 3
# cal = calendar.month(year,month)
# print(cal)


# name = 'selemani mtahukile'
# new = name.replace("selemani","mustaki")
# print(new)

# my_list = ["juma","sodalini","jamali"]
# new_my = " ".join(my_list)
# print(new_my)
# print(name.startswith("s"))
# print(name.endswith("e"))
# print(name.find("sele"))
# print(name.count("s"))


# name = 20
# is_student = True
# print(type(name))
# n = 2**2
# print(n)

# nn = input("enter your name \n ")
# print(nn)


# name = input("enteer name")
# cy = 2026
# age = int(input("ingiza mwaka"))
# umri = cy - age
# print(f"my name is {name} iam {umri} years old")


# temp_cel = float(input("enter temp in celcius  "))
# temp_far = (9*temp_cel / 5) + 32
# print(f"{temp_cel}C = {temp_far} F")

# my_list = [5,2,5,2,2]

# for x_count in my_list:
#     output = ' '
#     for b in range(x_count):
#         output += 'x'
#     print(output)    


# numbers = [5,2,5,2,2]  
# for x_ount in numbers:
#     output = " "
#     for count in range(x_ount):
#         output += "x"
#     print(output) 

            ####unpucking 
# coordinates = (1,2,3)
# # coordinates[0] * coordinates[1] * coordinates[2]
# #unpacking 
# #instead of using this way to do you calculation do this
# x,y,z = coordinates
# print(x*y*z)

# #dictionaries
# customer = {
#     "name": "selemani",
#     "age": 30,
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("age"))#if you pass a key that is absent it return a None instead of error 
# #but you can add a new key 
# customer["birth_date"] = "jan 1 1990"
# print(customer["birth_date"])

            ######exercise
# number = input("enter a number")
# digit = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# output = " "
# for ch in number:
#     output += digit.get(ch, "!") + " "
# print(output)
  
# sms = input(">")
# words = sms.split(" ")
# emojis = {
#     ":)": "😁",
#     ":(": "😔"
# }
# output = " " 
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)



        #######defining a function
# def greeting(name, last_name):
#     print(f'Hi {name} {last_name}')
#     print('welcome to our aboard')

# greeting("juma", "saidi") 

#but when dealing whith numerical varue it is 
 #better to use keyword arguments like below

#customer_cost(total=50, shipping=5, discount= 0.2)
# And important thing is you writting you should start with position arguments fas and then keyword arguments

# def square(number):
#     return number*number
# print(square(3))


# def emoji_converter(sms):
#     words = sms.split(" ")
#     emojis = {
#     ":)": "😁",
#     ":(": "😔"
# }
#     output = " " 
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output    
# mesage = input(">")
# print(emoji_converter(mesage))
    
    
##ERROR HANDLING USING TRY AND EXCEPT
# try:
#     age = int(input("age:  "))
#     income = 20000
#     risk = 20000/age
#     print(age)
# except ValueError:
#     print("INVALID VALUE")
# except ZeroDivisionError:
#     print("age can not be 0")        
    
    
    