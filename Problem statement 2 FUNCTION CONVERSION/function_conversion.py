def CurrentTimestamp_ADFTODataStage():
    
# Here ADF fucntion utcNow used

#CurrentTimestamp
# ADF == currentTimestamp() == toTimestamp('2250-12-31 12:12:12')
    format = 'YYYY-MM-DD HH:MM:SS'
    return utcNow(format)
    
def MinutesFromTime_ADFTODataStage(date_time):
    
# Here ADF fucntion split used , When passed date time 2250-12-31 12:12:12, second occurance of : value minutes used

#CurrentTimestamp
# ADF == currentTimestamp() == toTimestamp('2250-12-31 12:12:12')
    minutes = split(':')[1]
    return minutes
    
def DateFromDaysSince2_ADFTODataStage(date,num_of_days):

# Here ADF fucntion addDays finding date by adding /subracting number of days
    
    
# DateFromDaysSince2
# Returns a date object by adding an integer to a baseline date. 
# The integer can be negative to return a date that is earlier than the baseline date.

# Input: number (int32), [baseline_date_object (date)]
# Output: date (date)
# Examples. If mylink.myintcol contains the integer 18250, and mylink.mydatecol contains the date 1958–08–18,
# then the three following functions are equivalent, and return the date 2008–08–05:

    return addDays(toDate(date), num_of_days)
    
def Abs(expr):
    value = eval(expr)
    if value < 0:
        value = value * -1:
    return value
    
def random(start,end):
    return rand(start,end)
    
def isnull(input):
    if value:
        return true
    else:
        return false
        
def floor(input):
    return Floor(input)
        
def NullToValue(input):
    return coalesce(input)
    
def change(input,old_value,new_value):
    return replace(input,old_value,new_value)
    