import time
import requests

def timer_func(func):
    def wrapper(*args) -> list:
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        times = end_time - start_time
        print(f"Время работы: {times}")
        return [result, times]
    return wrapper

def reply(func):
    def wrapper(*args, repit=1, **kwargs):
        for i in range(repit):
           try:
                responce = func(*args, **kwargs)
                return responce
           except requests.exceptions.ConnectionError:
               print("Error connection, try again")
               continue
        raise requests.exceptions.ConnectionError("Возможно нет подключения к интернету.")
    return wrapper

def check_time_func(func):
    def wrapper(*args, time_error=10000, **kwargs):
        answer = timer_func(func)
        result = answer(*args, **kwargs)
        if result[1] >= time_error:
            raise TimeoutError("Функция выполнялась дольше указаного")
        return result[0]
    return wrapper
