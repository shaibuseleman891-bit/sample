full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    list=[strength,intelligence,charisma]
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    if not all(isinstance(stats, int) for stats in list):
        return 'All stats should be integers'
    if any((stats < 1 ) for stats in list):
        return 'All stats should be no less than 1'
    if any((stats > 4) for stats in list):
        return 'All stats should be no more than 4'
    if sum(list) != 7:
        return 'The character should start with 7 points'
    return f'{name}\nSTR {full_dot*strength}{(10-strength)*empty_dot}\nINT {full_dot*intelligence}{(10-intelligence)*empty_dot}\nCHA {charisma*full_dot}{(10-charisma)*empty_dot}'
print(create_character('ren', 4, 2, 1))

    






