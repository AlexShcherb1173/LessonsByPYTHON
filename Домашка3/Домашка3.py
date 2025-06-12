#-----------------------------------------------------------------------------------------------------
# инициализация словарей трех уровней сложности
words_easy = {
    "family":"семья",
    "hand":"рука",
    "people":"люди",
    "evening":"вечер",
    "minute":"минута"}

words_medium = {
    "believe":"верить",
    "feel":"чувствовать",
    "make":"делать",
    "open":"открывать",
    "think":"думать" }

words_hard   = {
    "rural":"деревенский",
    "fortune":"удача",
    "exercise":"упражнение",
    "suggest":"предлагать",
    "except":"кроме"}
#------------------------------------------------------------------------------------------------------
# инициализация словаря рангов
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично"}

#---------------------------------------------------------------------------------------------------------
def choose_difficulty():
    """
    функция выбора уровня сложности
    без аргумента, возврат словарь слов уровня сложности
    """
    words = {}
    print('Выберите уровень сложности. Легкий, средний, сложный.')
    level = input()
    print()
    level_l = level.lower()

    if level_l == 'легкий':
       words = words_easy
    elif level_l == 'средний':
       words = words_medium
    elif level_l == 'сложный':
       words = words_hard
    else:
       level_l = 'средний'
       print(f'Уровень по выбору программы')
       print()
       words = words_medium

    print(f'Выбран уровень сложности {level_l}. Мы предложим 5 слов, подберите перевод.')
    print()
    return words
#---------------------------------------------------------------------------------------------

def play_game(words):
    """
    функция тела игры
    аргумент словарь слов - вопросов, возврат словарь ответов
    """
    answers = {}
    for key, value in words.items():
        print(f'{key}, {len(value)} букв, начинается на {value[0]}...')
        word = input()
        word_l = word.lower()
        if word_l == value:
           print(f'Верно. {key.title()} — это {value}.')
           answers[key] = True
        else:
            print(f'Неверно. {key.title()} — это {value}.')
            answers[key] = False
    return answers
#--------------------------------------------------------------------------------------------------

def display_results(answers):
    """
    функция вывода ответов
    аргумент словарь ответов, возврата нет, печать в консоль
    """
    print()
    print('Правильно отвечены слова:')
    for key, value in answers.items():
        if value:
           print(key)
    print()
    print('Неправильно отвечены слова:')
    for key, value in answers.items():
        if not value:
           print(key)
#-------------------------------------------------------------------------------------------------

def calculate_rank(answers):
    """
    функция подсчета ранга ответов
    аргумент словарь ответов, возврат ранг(балл) ответа
    """
    rank = 0
    for value in answers.values():
        if value:
           rank += 1
    return rank
#------------------------------------------------------------------------------------------------

# основная программа
words_dict = choose_difficulty()
play_answers = play_game(words_dict)
display_results(play_answers)
rank = calculate_rank(play_answers)
print()
print(f'Ваш ранг: {levels[rank]}')

