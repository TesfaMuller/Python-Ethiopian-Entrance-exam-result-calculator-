# Inputting Variables
X = int(input('Insert English: '))
Y = int(input('Insert Maths: '))
A = int(input('Insert Aptitude: '))
B = int(input('Insert Physics: '))
C = int(input('Insert Chemistry: '))
D = int(input('Insert Biology: '))
S = input('Insert Sex (M/F): ').upper()

# Computing the result
result = X + Y + A + B + C + D

# Giving Comment
if result >= 500:
    comment = 'Promoted! የትምህርት ጀግና!!'

elif result >= 450:
    comment = 'Promoted! በጣም ጥሩ!!'

elif result >= 400:
    comment = 'Promoted! ጥሩ ነዉ!'

elif result >= 300:
    comment = 'Promoted'

else:
    if S == 'M':
        if result >= 210:
            comment = 'Failed. Eligible for remedial'
        else:
            comment = 'Failed'
    else:  # Female
        if result >= 200:
            comment = 'Failed. Eligible for remedial'
        else:
            comment = 'Failed'

print('Your Score is:', result)
print('Comment:', comment)