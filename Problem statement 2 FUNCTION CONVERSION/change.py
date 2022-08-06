from ./function_conversion import *
import sys

if __name__ == '__main__':
    input = sys.argv[1]
    old_value = sys.argv[2]
    new_value = sys.argv[3]
    print(change(input,old_value,new_value))