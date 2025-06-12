# НАЧАЛО ПРОГРАММЫ, ОПРЕДЕЛЕНИЯ
# создание списков вопросов и ответов
question = ['My name __ Vova', 'I __ a coder', 'I live __ Moscow']
answers = ['is', 'am', 'in']

# определение переменных
len_question = len(question) # длина списка вопросов
right_answ = 0               # количество правильных ответов
percent_answ = int(right_answ / len_question * 100) # переменная для процентов правильных ответов

# определяю новую функцию для правильного падежного окончания после числительного
def numm_end(numm): # аргументом передаем число, возвращаем правильное окончание
    if numm % 10 == 1:
        return ''
    elif numm % 10 == 2 or 3 or 4:
        return 'а'
    else:
        return 'ов'
# ---------------------------------------------------------------------------------------------
# ОПЕРАЦИОННАЯ ЧАСТЬ
# приглашение поиграть
import sys
print('Привет!', 'Предлагаю проверить свои знания английского!', 'Наберите "ready", чтоб начать!', sep='\n')
user_input = input()
if user_input != 'ready':
    print('Кажется, вы не хотите играть')
    sys.exit()

# вопросы и ответы
for i in range(len_question):
    print(question[i])
    ques = input()
    if ques == answers[i]:
        print('Ответ верный!')
        right_answ +=1
    else:
        print(f'Неправильно. Правильный ответ {answers[i]}')

# ОКОНЧАНИЕ ПРОГРАММЫ, ВЫВОД РЕЗУЛЬТАТОВ
print(f'''Вот и всё!
Вы ответили на {right_answ} вопрос{numm_end(right_answ)} из {len_question} верно.
Это {percent_answ} процент{numm_end(percent_answ)}.''')
#-----------------------------------------