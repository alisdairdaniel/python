print('The main thread executes the code') 

from threading import Thread
from time import sleep

def threadFunc(argA,argB):
    print('The child thread starts')
    print(f'The thread function parameter is:{argA}, {argB}')
    sleep(5)
    print('Thread end')

thread = Thread(
   
    target=threadFunc, 

    args=('Parameter 1', 'Parameter 2')
)

thread.start()

thread.join()
print('Main thread end')
