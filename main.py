from random import randint

def task1():
    words = []

    print('запись слов через пробел')

    while True:
        word = input('Введите слово: ')
        if(word == 'stop'):
            break
        else:
            words.append(word)
    
    print(" ".join(words))

def task2():

    print('Игра в слова')

    while True:
        word = input('Введите слово: ')
        separatedWord = list(word.lower())
        hasFs = 'ф' in separatedWord

        if(word == 'stop'):
            break
        else:
            if hasFs:
                print("Ого! Это редкое слово")
            else:
                print("Эх, это не очень редкое слово")

def task3():

    print('Математика для детей')

    rightАnswer = 0
    wrongAnswer = 0

    while wrongAnswer < 3:
        a = randint(0, 100)
        b = randint(0, 100)
        answer = input(f"{a} + {b} = ")

        if answer.isdigit():
            if a + b == int(answer):
                rightАnswer += 1
                print('Верно!')
            else:
                wrongAnswer += 1
                print('Не верно')
        else:
            print('Не числовое значение')

    print(f'Игра окончена. Количество верных ответов: {rightАnswer}')


task1()
task2()
task3()