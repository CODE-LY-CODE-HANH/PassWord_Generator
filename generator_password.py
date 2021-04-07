import string
import random

LETTERS = string.ascii_letters

NUMBERS = string.digits

punctuation = string.punctuation

def password_generator(length = 8 , chu = False , so = False , ky_tu = False):
    chuoi = None

    if (chu == True) and (so == True):

        chuoi = ''.join([ LETTERS , NUMBERS ])

    elif (chu == True) and (ky_tu == True):

        chuoi = ''.join([ LETTERS , punctuation ])

    elif (so == True) and (ky_tu == True):

        chuoi = ''.join([ NUMBERS , punctuation ])

    elif chu:

        chuoi = f'{LETTERS}'

    elif so:

        chuoi = f'{NUMBERS}'

    elif ky_tu:

        chuoi = f'{punctuation}'

    else:
        chuoi = f'{LETTERS}{NUMBERS}{punctuation}'


    # chuyen sang []
    chuoi = list(chuoi)
    random.shuffle(chuoi)

    random_password = random.choices(chuoi , k= length)
    random_password = ''.join(random_password)
    print(random_password)
    return str(random_password)

password_generator(10 , chu= True , so= True , ky_tu= False)