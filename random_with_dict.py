      
import random

my_dict = {
    'name': 'Borislav Hadzhiev',
    'fruit': 'apple',
    'number': 5,
    'website': 'bobbyhadz.com',
    'topic': 'Python'
}
k, val = random.choice(list(my_dict.items()))
print(val)  

#  get random key from dictionary
key = random.choice(list(my_dict))
print(key)  
value = random.choice(list(my_dict.values()))
print(value)  

        
