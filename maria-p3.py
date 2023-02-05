
# count the total requests

with open(r"DataSet.txt", 'r') as tlines:
    x = len(tlines.readlines())
    print('Total lines:', x)


#-----------------------------------------------------------------------------------


# trying to code the 6 months data

from datetime import datetime
from datetime import date


date_ = '[11/Oct/1995:14:14:17 -0600]'

count = 0

format = '%d/%b/%Y'
start_date = datetime.strptime('11/Oct/1995', format)
end_date = datetime.strptime('11/Apr/1995', format)

with open('DataSet.txt','r') as data: # open file
    contents = data.readlines() # read each line

    # scan for the past 6 months
    for i in f:
        count += 1

print("Total requests made in the last 6 months: ", count)

data.close()
