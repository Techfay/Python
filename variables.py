x = 5
y = "Hello, World!"

print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4
x = "Sally"
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#You can get the data type of a variable with the type() function.
x = 5
y = "Shivangi"
z = 5.0
print(type(x))
print(type(y))
print(type(z))

##String variables can be declared either by using single or double quotes.
x = "Mandalorian"
print(x)
#double quotes are the same as single quotes.
x = 'Mandalorian'
print(x)

#Variable names are case-sensitive.
a = 4
A = "Emma Watson"

print(a)
print(A)
