import numpy as np
from time import time


def random_predict(number:int=np.random.randint(1,101)) ->int:
    """поиск случайного числа

    Args:
        number (int, optional): слуайное число. Стандартное значение из np.random.randint(1,101).
s
    Returns:
        int: количество попыток
    """
    count = 0
    low = 1
    high = 100
    
    while True:
        
        count += 1
        predict = np.random.randint(low,high+1)
        
        if predict > number:
            high = predict - 1
        elif predict < number:
            low = predict + 1
        else:
            break
    return count


def time_runs(n_runs:int=100000):
    """Декоратор для определения среднего числа попыток

    Args:
        n_runs (int, optional): _description_. Defaults to 100000.
    Returns:
        Отдекоррированную функцию и средние число попыток
    """
    def time_decorator(func):  
        def decorated_func(*args, **kwargs):
            start = time()
            count = ()
            np.random.seed(1)
            
            for i in range(n_runs):
                count += (func(*args, **kwargs),)
            end = time()
            delta = end - start
            
            mean_time = delta / n_runs
            
            print("Mean runtime:", mean_time)
            print('full runtime:', delta)
            
            return np.mean(count)
        
        return decorated_func
    
    return time_decorator


#RUN
if __name__=='__main__':
    decorated_random = time_runs()(random_predict)
    print(f'Алгоритм в среднем угадывает за {decorated_random()} попыток')