#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np

def game_core_v1(number):
    '''Решение реализованно с помощью алгоритма бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0 
    min_value = 1
    max_value = 101
    predict = 50 # наше первое предположение, что число равно половине заданного интервала
    
    while True:
        count += 1
        if number == predict:
            return count # возвращает число попыток
        elif number < predict:
            max_value = predict # обновляем значение для max_value
            predict = int((max_value+min_value) / 2)
        elif number > predict:
            min_value = predict # обновляем значение для min_value
            predict = int((max_value+min_value) / 2)
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core_v1)


# In[ ]:




