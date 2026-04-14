class Planet:
    def  __init__(self, name, planet_type, star):
        attribute_check = (name, planet_type,star)
        for attr in attribute_check:
            if not isinstance(attr, str):
                raise TypeError('name, planet type, and star must be strings')
            elif attr == "":
                raise ValueError(f"name, planet_type, and star must be non-empty strings")   
        self.name = name
        self.planet_type= planet_type
        self.star = star            
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet_1 = Planet('jupiter', 'gas', 'sun')
planet_2 = Planet('pluto', 'dwarf', 'sun')
planet_3 = Planet('uranus', 'ice', 'sun')
print(planet_1)
print(planet_2)
print(planet_3)


print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())




        




        