# Inputting Variables
X = int(input('Insert a number: '))
Y = int(input('Insert another number: '))
A = input('Insert operation (+,-,*,/): ')

# Computing the numbers
if A == '+':
    result = X + Y
elif A == '/':
    if Y == 0:
        result = 'Error: division by zero'
    else:
        result = X / Y
elif A == '-':
   result = X - Y
elif A == '*':
	    result = X * Y
else:
	  result = 'error: Wrong Operation selected'

print('The answer is:', result)