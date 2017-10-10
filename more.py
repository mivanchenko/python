def get_error_details():
    return (2, 'details')
errnum, errstr = get_error_details()
#print(errnum, errstr)


flag = True
#if flag: print('Yes')


points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['x'])
#print(points)


list1 = [2, 3, 4]
#print(list1)
list2 = [ 2*i for i in list1 if i > 2 ]
#print(list2)


def power_sum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

#print( power_sum(2, 3, 4) )
#print( power_sum(2, 10) )


#mylist = ['item']
#assert len(mylist) >= 1
#mylist.pop()
#assert len(mylist) >= 1


from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception(
                    'Attempt {}/{} failed : {}'.format(
                        attempt, MAX_ATTEMPTS, (args, kwargs)
                    )
                )
        log.critical('All {} attempts failed: {}'.format(MAX_ATTEMPTS, (args, kwargs)))
    return wrapper_function

counter = 0

@retry
def save_to_database(arg):
    print('Begin')
    global counter
    counter += 1
    if counter < 3:
        raise ValueError(arg)

#if __name__ == '__main__':
#    save_to_database("Some bad value")


import six
#print(six.PY2)
#print(six.PY3)







