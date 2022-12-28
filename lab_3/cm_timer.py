import time
from contextlib import contextmanager

class cm_timer_1:
    
    def __init__(self):
        pass
        
    def __enter__(self):
        # Должен возвращаться значимый объект
        # например, открытый файл
        self.start = time.time()
        return self.start
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            self.end = time.time()
            print('time:', self.end - self.start)

@contextmanager
def cm_timer_2():
    start = time.time()
    yield start
    end = time.time()
    print('time2:',end - start)

def main():
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)

if __name__ == '__main__':
    main()
