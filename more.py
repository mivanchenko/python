#def get_error_details():
##    return (2, 'details')
##    return (42)
#    return (42, 'details')
#errnum, errstr = get_error_details()
##errnum = get_error_details()
##print(errnum, errstr)
#print(errnum)
#print(errstr)


#flag = True
##if flag: print('Yes')


#points = [{'x': 2, 'y': 3},
#          {'x': 4, 'y': 1}]
#points.sort( key = lambda elem: elem['y'] )
#print(points)


#list1 = [2, 3, 4]
##print(list1)
##list2 = [ 2*i for i in list1 if i > 2 ]
#list2 = [ 2*i for i in list1 ]
#print(list2)


#def power_sum(power, *args):
#    '''Return the sum of each argument raised to the specified power.'''
#    total = 0
#    for i in args:
#        total += pow(i, power)
#    return total
#
##print( power_sum(2, 3, 4) )
##print( power_sum(2, 10) )
#
#
#mylist = ['item']
#assert len(mylist) >= 1
#mylist.pop()
##assert len(mylist) >= 1
#
#
#from time import sleep
#from functools import wraps
#import logging
#logging.basicConfig()
#log = logging.getLogger("retry")
#
#def retry(f):
#    @wraps(f)
#    def wrapper_function(*args, **kwargs):
#        print('.')
#        MAX_ATTEMPTS = 5
#        for attempt in range(1, MAX_ATTEMPTS + 1):
##            try:
#                return f(*args, **kwargs)
##            except:
##                log.exception(
##                    'Attempt {}/{} failed : {}'.format(
##                        attempt, MAX_ATTEMPTS, (args, kwargs)
##                    )
##                )
##                sleep(10 * attempt)
##        log.critical('All {} attempts failed: {}'.format(MAX_ATTEMPTS, (args, kwargs)))
#    return wrapper_function
#
#counter = 0
#
#@retry
#def save_to_database(arg):
#    print('Begin')
#    global counter
#    counter += 1
#    if counter < 3:
#        raise ValueError(arg)

#if __name__ == '__main__':
#    save_to_database("Some bad value")


##import six
##print(six.PY2)
##print(six.PY3)
#


from functools import wraps

def add_one(f):
    '''Adds one.'''
    @wraps(f)
    def wrapped(*args, **kwargs):
        result = f(*args, **kwargs)
        return result + 1
    return wrapped

def double(f):
    '''Doubles the value.'''
    @wraps(f)
    def wrapped(*args, **kwargs):
        result = f(*args, **kwargs)
        return result * 2
    return wrapped

@double
@add_one
def calc(arg):
    '''Calculates something.'''
    return arg

print(calc(1))
