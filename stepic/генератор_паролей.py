import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

amount = input('Введите количество желаемых паролей! ')
length = input('Какова длина одного пароля? ')
digit = input('Включать ли цифры 0123456789? ')
uppercase_letter = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')
lowercase_letter = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')
symbols1 = input('Включать ли символы !#$%&*+-=?@^_? ')
symbols2 = input('Исключать ли неоднозначные символы il1Lo0O? ')

if digit == 'да':
    chars += digits
if uppercase_letter == 'да':
    chars += lowercase_letters
if lowercase_letter == 'да':
    chars += uppercase_letters
if symbols1 == 'да':
    chars += punctuation
for count in range(int(amount)):
    if symbols2 == 'да':
        for count in range(int(length)):
            if chars.count(chars[count]) > 1:
                while chars[count] == random.sample(chars):
                    chars.replace(count, random.sample(chars))
    print(*random.sample(chars, int(length)), sep='')
