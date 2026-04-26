# class Walker:
#     def walk(self):
#         return "i can walk on the land" 

# class Swimmer:
#     def swim(self):
#         return "i can swim in the water"
                
# class Amphibian(Walker, Swimmer):
#     def __init__(self, name):
#         self.name = name
        
#     def introduce(self):
#         return f"my name is: {self.name} the frog. {self.walk()} and {self.swim()}"           
# frog_mtoto = Amphibian('chura')  
# print(frog_mtoto.introduce()


# class Cat:
#     def speak(self):
#         return "A cat meow"
# class Bird:
#     def speak(self):
#         return "A bird tweet"
# class Monkey:
#     def speak(self):
#         return "A monkey ooh ooh aah aah ooh ooh"
# def animal_sound(animal):
#     print(animal.speak())
# animal_sound(Cat())
# animal_sound(Bird())               
 
class Twitter:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
   def __init__(self, content):
       self.content = content

   def post(self):
       return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
   print(social_media.post())  # Calls .post() on any object 

# Instances
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

start(tweet)   