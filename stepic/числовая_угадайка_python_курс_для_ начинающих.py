import random

number = random.randrange(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(text):
    return text.isdigit() and 1 <= int(text) <= 100


while True:
    text = input('Введите Ваше число от 1 до 100: ')
    if is_valid(text) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if is_valid(text) == True:
        text = int(text)
        if text < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if text > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        if text == number:
            print('Вы угадали, поздравляем!')
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
