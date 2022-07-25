from itertools import count
import numpy as np
def random_predict(number:int=1) -> int:
    """рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        if number == np.random.randint(1, 101):
            break
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(func) -> int:
    """За какое количество времени комп в среднем угадывает числа при зафиксированном сиде

    Args:
        func (_type_) функция угадывания

    Returns:
        int: срднее количество попыток
        Так как у вас случайные числа, без seed, 
        запуская функцию много раз - случайные числа будут 
        меняться. И если 2 человека запустят код, они 
        могут получить разные результат. Для воспроизводимости 
        кода нам нужно зафиксировать начальные условия, 
        чтобы в не зависимости  от запуска, мы получали одно 
        и тоже. За это отвечает seed. Функция random.seed() в
        Python используется для инициализации случайных чисел. 
        По умолчанию генератор случайных чисел использует 
        текущее системное время. Если вы дважды используете 
        одно и то же начальное значение seed, вы получите 
        один и тот же результат, что означает случайное число 
        дважды.
        
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(func(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
if __name__ == '__main__':
    score_game(random_predict)