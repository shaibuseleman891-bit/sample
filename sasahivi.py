
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
 
# for number in numbers: 
#     lagest_number = numbers[0]     
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


temp_cel = float(input("enter temp in celcius  "))
temperature = (9*temp_cel / 5) + 32
print(f"{temp_cel}C = {temperature} F")

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



# class Student:
#         def __init__(self,name,marks):
#                 self.name = name
#                 self.marks = marks
#         def add_mark(self,mark):
#                 self.marks.append(mark)
#         def __str__(self):
#                 return f"Name: {self.name}, Average: {self.average()}"
                        
#         def average(self):
#                 total = sum(self.marks)
#                 number = len(self.marks)
#                 average  = total / number 
#                 return average             
                        
# s1 = Student('juma',[50,60,90])

# s1.add_mark(100)
# print(s1.average())
# print(str(s1))


# class BankAccount:
#         def __init__(self,owner,balance):
#                 self.owner = owner
#                 self.balance = balance
#         def deposit(self,amount):
#                 if amount > 0:
#                         self.balance += amount
#                 else:
#                         print("Invalid amount")        
#         def withdraw(self,amount):
#                 if amount <= self.balance:
#                         self.balance -= amount
#                         return self.balance
#                 elif amount <= 0:
#                         print("Invalid amount")
#                 else:
#                         print("insufficint balance!!")
#         def check_balance(self):  
#                 return self.balance
#         def transfer(self,amount,other_account):
#                 if amount <= 0:
#                         print("Invalid ammount")
#                 elif amount <= self.balance:
#                         self.balance -= amount
#                         other_account.balance += amount #or other_account.deposit(amount)
#         def __str__(self):
#                 return f"Owner: {self.owner}, Balance: {self.check_balance()}"      
# account_1 = BankAccount('selemani',1000)
# account_2 = BankAccount('juma',600)
# print(account_2.check_balance())
# account_1.deposit(1000)
# print(account_1.check_balance())
# account_1.withdraw(500)
# account_1.transfer(1000,account_2)
# print(account_1.check_balance())
# print(account_1)



# class Student: 
#         def __init__(self,name,marks=None):
#                 self.name = name
#                 if marks is None :
#                         marks = []
#                 else:        
#                         self.marks = marks
#         def calculate_average(self):
#                 total = sum(self.marks)
#                 number = len(self.marks)  
#                 average = total / number
#                 return average  
#         def has_passed(self):
#                 if self.calculate_average() >= 50:
#                         return True
#                 return False
#         def get_grade(self):
#             avg = self.calculate_average()
#             if avg >= 75:
#                     return 'A'
#             elif avg >= 65:
#                     return 'B'
#             elif avg >= 50:
#                     return 'c'
#             else:
#                     return 'F'                              
#         def __str__(self):
#                 return f"Jina: {self.name}, Wastani: {self.calculate_average()}, Grade: {self.get_grade()}"
#         def add_mark(self,mark):
#                 self.marks.append(mark)
# student_1 = Student('selemani',[70,80,90])
# print(student_1)


# class Category:
#     def __init__(self,name,ledger=None):
#         self.name = name
#         if ledger is None:
#             self.ledger = []
#         else:
#             self.ledger = ledger
#     def deposit(self,amount,description=""):
#         self.ledger.append({'amount': amount, 'description': description})
    
#     def withdraw(self,amount,description=""):
#         if amount <= self.get_balance():
#             self.ledger.append({'amount': -amount, 'description': description})
#             return True 
#         else:
#             False    
   
#     def get_balance(self):
#         total = 0
#         for item in self.ledger:
#             total += item['amount']
#         return total   

#     def transer(self,amount,category): 
#         if amount <= self.get_balance():
#             self.withdraw(amount, f"Transfered to {category.name}")

#             category.deposit(amount, f"received from {self.name}")
#             return True
#         else:
#             return False      


# for i in range(100,0,-10):
#         print(f"{i:.>}|\n")

# print(f"{1000000:,}")

# name = input('Enter file: ')
# handle = open(name, 'r')
# counts = dict()
# for line in handle:
#         words = line.split()
# for word in words:
#         counts[word] = counts.get(word, 0) + 1
# bigcount = None
# bigword = None
# for word, count in list(counts.items()):
#         if bigcount is None or count > bigcount:
#                 bigword = word
# bigcount = count
# print(bigword, bigcount)


# name = input("enter your name ")
# print(f"hello {name}")       



# temperature = input("enter temp in fahreinheit ")
# try:
#         fahr = float(temperature)
#         temp_cel = (fahr - 32)* 5.0 / 9.0   
#         print(f"{fahr}F = {temp_cel}C")
# except:
#         print("Please enter a number!!")       
# try:                     
#         hours = float(input("enter hour of work"))  
#         rate = float(input("enter the rate "))

#         if hours > 40:
#                 initial_pay = 40 * rate
#                 overtime_pay = (hours-40) * (rate * 1.5)
#                 total_pay = initial_pay + overtime_pay 
#         else:
#                 pay = hours * rate
#         print("Pay", pay)
# except ValueError:
#         print("please enter a number")
                                
# class Wallet:
#         def __init__(self):
#                 self.__balance = 0
                
#         def __validate(self, amount):
#                 if amount < 0:
#                         print("Amount must be positive") 
#         def deposit(self, amount):
#                 self.__validate(amount)
#                 self.__balance += amount 
#         def withdraw(self,amount):
#                 self.__validate(amount) 
#                 if amount > self.__balance:
#                         print("Insufficient funds")
#                 self.__balance -= amount
#         def get_balance(self):
#                 return self.__balance 
# acc_one = Wallet() 
# acc_one.deposit(300)
# print(acc_one.get_balance())

# acc_one.deposit(-50)
# acc_one.withdraw(1000)

# class Circle:
#         def __init__(self,radius):
#                 self.__radius = radius 
#         @property
#         def radius(self): #getter to get a valiable
#                 return self.__radius
#         @property
#         def area(self): # getter to calculate an area 
#                 return 3.14 * (self.__radius**2)
# my_cirle = Circle(7)
# print(my_cirle.radius)
# print(my_cirle.area)       



# class Circle:
#         def __init__(self,radius):
#                 self.radius = radius # calling the setter 
#         @property
#         def radius(self): # getter to get the radius 
#                 return self._radius
#         @radius.setter
#         def radius(self,value):
#                 if value <= 0:
#                         print("radius must be a positive number")
#                 self._radius = value
# new_circle = Circle(14)
# print(new_circle.radius)

# new_circle.radius = 28
# print("modifyed radius:", new_circle.radius)

# class Circle:
#         def __init__(self,radius):
#                 self.radius = radius
#         #Getter 
#         @property
#         def radius(self):
#                 return self._radius 
#         #setter 
#         @radius.setter
#         def radius(self,value):
#                 if value <= 0:
#                         print("please enter a positive number")
#                 self._radius = value
#         #deleter
#         @radius.deleter
#         def radius(self):
#                 print("deleting radius...")
#                 del self._radius
                
                  
                
                
                
                        
                
              
                                               
                                
                                
                                
                        



                
                

       