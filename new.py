# import string
# import random
#
# LETTERS = string.ascii_letters
# # print(LETTERS)
# NUMBERS = string.digits
# # print(NUMBERS)
# punctuation = string.punctuation
# # print(punctuation)
#
# def passWord_Generator(length = 8 , chu = False , so = False , ky_tu = False):
#     chuoi = None
#     if chu and so and ky_tu:
#         chuoi = ''.join([LETTERS, NUMBERS, punctuation])
#     elif (chu == True) and (so == True):
#         chuoi = ''.join([ LETTERS , NUMBERS ])
#
#     elif (chu == True) and (ky_tu == True):
#
#         chuoi = ''.join([ LETTERS , punctuation ])
#
#     elif (so == True) and (ky_tu == True):
#
#         chuoi = ''.join([ NUMBERS , punctuation ])
#
#     elif chu:
#
#         chuoi = ''.join(LETTERS)
#
#     elif so:
#
#         chuoi = ''.join([NUMBERS])
#
#     elif ky_tu:
#
#         chuoi = f'{punctuation}'
#     else:
#         chuoi = ''.join([LETTERS, NUMBERS, punctuation])
#
#     chuoi = list(chuoi)
#     random.shuffle(chuoi)
#
#     random_password = random.choices(chuoi , k= length)
#     random_password = ''.join(random_password)
#
#     return random_password
#
# print(passWord_Generator(20 , chu= False , so= True , ky_tu= True) )