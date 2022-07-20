from time import sleep


def func(a, b, c):
    return a * b ** c


def delay(func, sleep_time,*args,**kwargs):
    print("Czekamy: ",sleep_time)
    sleep(sleep_time)
    print(func(*args,**kwargs))
    print("The end")


delay(func, 2, 10, 20, 2)

"""def delay_2(func,ms,*args,**kwargs):
    sleep(ms/1000)
    return func2(*args,**kwargs)
def func2(a,b,c):
    return a * b **c

print(delay_2(func2,250,10,20,2))"""