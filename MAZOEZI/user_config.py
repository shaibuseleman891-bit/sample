test_settings = {'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}

names = ('volume', 'juma')

def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!" 
          
    for key, value in settings.items():
        print(key.lower(), value.lower())

def update_setting(old, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key not in old:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    else:
        old.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(one, two):
    key = two.lower()
    if key in one:
        one.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(dictionary): 
    if dictionary == {}:
        return "No settings available."
    else:
        entries = ""
        for keys,value in dictionary.items():
            entry = f"{keys.capitalize()}: {value}\n"
            entries += entry  
        return f"Current User Settings:\n{entries}"
print(view_settings(
   {'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'})) 

  
    
print(delete_setting({'theme': 'light'}, 'theme'))

print(update_setting({'theme': 'light'}, ('theme', 'dark')))

print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))


view_settings
print(add_setting(test_settings, names))