import random

word_list = ['привет', 'пока', 'электромонтер']                      # Words used in the game


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(stages[tries])


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в виселицу')

    while tries > 0:
        display_hangman(tries)
        tries -= 1
        if word_completion == word:
            print('Поздравляем! Вы победили!')
            break
        print(word_completion)
        char = input('Введите букву').upper()
        if not char.isalpha():
            print('Нужно ввести букву. Попробуйте снова')
            continue
        if len(char) > 1:
            print('Вы ввели слово? Ну, ладно сейчас проверим...')
            if char == word:
                print('Поздравляем! Вы победили')
                break
            elif char in guessed_words:
                print('Вы уже вводили это слово. Попробуйте снова')
                continue
            else:
                print('Увы, это неправильный ответ')
                guessed_words.append(char)
                continue
        elif len(char) == 1:
            if char in guessed_letters:
                print('Вы уже называли эту букву. Попробуйте снова')
                continue
            else:
                guessed_letters.append(char)
                word_copy = word
                while char in word_copy:
                    word_completion = word_completion[:word_copy.find(char)] + char + \
                                      word_completion[word_copy.find(char) + 1:]
                    word_copy = word_copy.replace(char, '_', 1)
        if word_completion == word:
            print('Поздравляем! Вы победили!')
            break
    if tries == 0 and word_completion != word:
        display_hangman(0)
        print("Вы проиграли(((")
        print(f'Загаданное слово - {word}')


while True:
    play(get_word())
    if input('Хотите сыграть снова?').lower() in ['нет', 'н', 'тщ', 'no', 'n', 'ytn']:
        print('Спасибо за игру! До свидания!')
        break







