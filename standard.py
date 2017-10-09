#import sys
#
#print(sys.version_info)
#print(sys.version_info.major == 3)


#import os
#import platform
#import logging
#
##print(os.path)
#if platform.platform().startswith('Windows'):
#    logging_file = os.path.join(
#        os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log'
#    )
#else:
#    logging_file = os.path.join( os.getenv('HOME'), 'test.log' )
#
#print('Logging to', logging_file)
#
#logging.basicConfig(
#    level=logging.DEBUG,
#    format='%(asctime)s : %(levelname)s : %(message)s',
#    filename=logging_file,
#    filemode='w',
#)
#
#logging.debug("Start of the progran")
#logging.info("Doing something")
#logging.warning("Dying now")


#import os
#
#print(os.path.join('1','2'))
#print(''.join( ('1', os.sep, '2') ) )
#
## does not work!
##arr = ['apple', 'banana', 'kiwi']
##print(str.join(arr))


import argparse

parser = argparse.ArgumentParser( description = 'Process some integers.' )
parser.add_argument('integers', metavar='N', type=int, nargs='+',
    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
    const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))








