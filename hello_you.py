#ask user for name
name = input ("what is your name?: ")


#ask user for age
age = input ("how old are you?: ")
print (name)
print (age)

print  (type(name))
print (type(age))

#ask user for city
city = input ("Where do you live?: ")
print (city)
#ask user what they enjoy
enjoy = input ("What do you enjoy?: ")
print (enjoy)
print (type (city))
print (type(enjoy))
#create outpout text
string = "your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, enjoy)
#print output to screen
print (output)
