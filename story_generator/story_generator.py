# Importing random module
import random

# Storing random data into lists to create story.
when = ['A long time ago', 'Yesterday', 'Before even you were born', 'In future', 'Before Thanos arrived']
who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America']
went = ['Angrut Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
what = ['to eat a lot of the cakes', 'to fight for justice', 'to steal the ice creams', 'to dance']

# Using string concatenition & randome.choice() to print a random element from all the lists
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')