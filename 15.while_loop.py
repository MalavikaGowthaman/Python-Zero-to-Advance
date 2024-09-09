# Syntax

# while condition:
#     print()


# Example 

i = 0

while i <11:  # it will check 0<11 if yes print malu.......
    print('Malu')
    i += 1 # first i value be 0 and it will get +1 and 1 .. increment option (i +1 = i)
  
i = 0
while i<11:
    print(i) 
    i += 1 # if increment is not given it will loop with in the same number
     
      
# Exercise -1 To create multiplication table

# get input from user if the gives one number it should retrun the table o/p.add()

number = int(input('Enter the number: '))

i = 1
while i <11:
    print(i * number)
    i += 1
    
# Exericise - 2 to get a exact table format

number = int(input('Enter the number: '))

i = 1
while i <11:
    print(i, '*', number, '=' , i * number)
    i += 1


# while else:

number = int(input('Enter the number: '))

i = 0
while i<11:
    print(i*number)
    i += 1
else:
    print('Program executed')