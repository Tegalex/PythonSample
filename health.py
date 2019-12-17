import random

health = 50
difficulty = 3

potionhealth2 = int(random.randint(25,50) / difficulty)

health = health + potionhealth2
print(health)
print ("Hello")
