import time

# build a wrapper for time took for the function to run
# function that returns a function
def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end-start)*1000}ms')
        return result
    return wrapper

@time_it # decorator
def some_op():
    print('Starting op')
    time.sleep(1)
    print('We are done')
    return 123 # random number return

if __name__ == "__main__":
    # some_op()
    # no need for () for some_op, but time_it returns a func, so () required
    # time_it(some_op)() 

    # with decorator
    some_op()