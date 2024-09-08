pizza = {
  'crust': 'thick',
  'toppings': ['mushrooms', 'extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']: 
  print("\t" + topping)


# You can nest a list inside a dictionary any time you want more than
#  one value to be associated with a single key in a dictionary.


favorite_languages = {

       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }

for name, languages in favorite_languages.items():
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages: 
            print("\t" + language.title())


# You should not nest lists and dictionaries too deeply. 
# If you’re nesting items much deeper than what you see 
# in the preceding examples or you’re working with someone else’s 
# code with significant levels of nesting, most likely a simpler way 
# to solve the problem exists.

# A Dictionary in a Dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
}

for username, user_info in users.items():
     print("\nUsername: " + username)
     full_name = user_info['first'] + " " + user_info['last']
     location = user_info['location']

# Python stores each key in the variable username
# the dictionary associated with each username goes into the variable user_info.

