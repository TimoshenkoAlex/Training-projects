rus_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_upper = rus_lower.upper()
eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = eng_lower.upper()

def ask_input_question():
    # Шифровать - True, Дешифровать - False
    do: bool
    answer = input('Что требуется сделать? Шифровать или дешифровать')
    while answer not in ['шифровать', 'ibdhjdfnm', 'i', 'ш',
                         'дешифровать', 'ltibdhjdfnm', 'l', 'д']:
        print('Введите корректный ответ: шифровать/дешифровать')
        answer = input('Что требуется сделать? Шифровать или дешифровать')
    if answer.lower() in ['шифровать', 'ibdhjdfnm', 'i', 'ш']:
        do = True
    elif answer.lower() in ['дешифровать', 'ltibdhjdfnm', 'l', 'д']:
        do = False

    # Русский - True, Английский - False
    language: bool
    answer = input('Какой язык используется?')
    while answer not in ['russian', 'rus', 'русский', 'рус',
                         'english', 'eng', 'английский', 'англ']:
        print('Введите корректный ответ: rus/eng')
        answer = input('Какой язык используется?')
    if answer.lower() in ['russian', 'rus', 'русский', 'рус']:
        language = True
    elif answer.lower() in ['english', 'eng', 'английский', 'англ']:
        language = False

    answer = input('Какой шаг сдвига (вправо)? Пожалуйста, введите только число')
    while not answer.isdigit():
        print('Введите корректный ответ: число')
        answer = input('Какой шаг сдвига (вправо)? Пожалуйста, введите только число')
    shift = int(answer)

    message = input('Введите текст')


    return do, language, shift, message


def code(language, shift, message):
    decoded = ''
    if language:
        l_upper = rus_upper
        l_lower = rus_lower
    else:
        l_upper = eng_upper
        l_lower = eng_lower
    for char in message:
        if char in l_lower:
            decoded = decoded + l_lower[(l_lower.find(char) + shift) % len(l_lower)]
        elif char in l_upper:
            decoded = decoded + l_upper[(l_upper.find(char) + shift) % len(l_upper)]
        else:
            decoded += char
    return decoded


def decode(language_d, shift_d, message_d):
    if language_d:
        length = 32
    else:
        length = 26
    return code(language_d, length - shift_d, message_d)