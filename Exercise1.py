from tokenize import Name
from unicodedata import name


name = input("What is your name?")
print("Hello "+ name)
#age = input("what is your age?")
#print(name + " is " + age + " years old")
#is_genius = True
#print(name + " is a genius")
print(name.upper())
print(name.lower())
print(name.find('a'))
print(name.replace("Prateek","Pranav"))
print(name.replace("P","T"))
print('t' in name)