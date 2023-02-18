import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''


def generate_password(length, chars):
    password = ''.join(random.sample(chars, length))
    print(password)


amount = int(input('Какое количество паролей необходимо?'))
length = int(input('Какая длина пароля необходима?'))
if input('Нужны ли цифры? (0123456789)').lower() in ['да', 'yes', 'lf', 'нуы', 'д', 'y']:
    digit = True
else:
    digit = False

if input('Нужны ли прописные буквы? (ABCDEFGHIJKLMNOPQRSTUVWXYZ)').lower() in ['да', 'yes', 'lf', 'нуы', 'д', 'y']:
    uppercase = True
else:
    uppercase = False

if input('Нужны ли строчные буквы? (abcdefghijklmnopqrstuvwxyz)').lower() in ['да', 'yes', 'lf', 'нуы', 'д', 'y']:
    lowercase = True
else:
    lowercase = False

if input('Нужны ли символы? (!#$%&*+-=?@^_)').lower() in ['да', 'yes', 'lf', 'нуы', 'д', 'y']:
    symbols = True
else:
    symbols = False

if input('Исключить неоднозначные символы?').lower() in ['да', 'yes', 'lf', 'нуы', 'д', 'y']:
    similar_symbols = True
else:
    similar_symbols = False

chars = digit * digits + uppercase * uppercase_letters + lowercase * lowercase_letters + symbols * punctuation
if similar_symbols:
    for char in 'il1Lo0O':
        chars = chars.replace(char, '')

for _ in range(amount):
    generate_password(length, chars)


