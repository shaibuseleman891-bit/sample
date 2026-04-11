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
        




print(update_setting({'theme': 'light'}, ('theme', 'dark')))

print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting(test_settings, names))