# Fortune Cookie using random.randint to generate a random number between specified integers between () & turning the
# string into and f-string meaning we can put variables in it using {} and the variable between them.

import random



lucky_number = random.randint(3, 6)
meh_number = random.randint(25, 49)
unlucky_number = random.randint(50, 75, )

fortune_number_lucky = 'You will have an excellent day...because you are learning python!'
fortune_number_meh = 'You will have a boring day...but you are alive!'
fortune_number_unlucky = 'You will have a terrible day...sorry for you!'
fortune_text = ''


if fortune_number_lucky == 1:
        fortune_text_l = 'You will have an excellent day...because you are learning python!'

if fortune_number_meh == 2:
        fortune_text_m = 'You will have a boring day...but you are alive!'

if fortune_number_unlucky == 3:
        fortune_text_u = 'You will have a terrible day...sorry for you!'

print(f'{fortune_number_lucky} Your Lucky number is: {lucky_number}! YAY')
print(f'{fortune_number_unlucky} Your Unlucky number is: {meh_number}! WOMP WOMP')
print(f'{fortune_number_meh} Your Meh number is: {unlucky_number}! MEH MEH')


