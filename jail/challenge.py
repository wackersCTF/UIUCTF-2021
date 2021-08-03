
#baby_python_fixed from uiuctf jail category

'''
whoops, I made a typo on the other chal. it's probably impossible, right? Python version is 3.8.10 and flag is at /flag

nc baby-python-fixed.chal.uiuc.tf 1337

author: tow_nater
'''
import re
bad = bool(re.search(r'[a-z\s]', (input := input())))
#bad = False
x = input
print(x)
exec(input) if not bad else print('Input contained bad characters')
exit(bad)
