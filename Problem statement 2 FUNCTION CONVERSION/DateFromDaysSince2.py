from ./function_conversion import *
import sys

if __name__ == '__main__':
    date = sys.argv[1]
    num_of_days = sys.argv[2]
    print(DateFromDaysSince2_ADFTODataStage(date,num_of_days))