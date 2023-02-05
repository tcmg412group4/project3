
# count the total requests

with open(r"DataSet.txt", 'r') as tlines:
    x = len(tlines.readlines())
    print('Total lines:', x)






# trying to code the 6 months data

from datetime import datetime


date = '[11/Oct/1995:14:14:17 -0600]'
i = 0

count = 0

with open('DataSet.txt','r') as data: # open file and read data
    if data.mode =='r':
    contents = data.readlines() # read each line in the txt file

        # scan for the past 6 months
    for contents in data:
        sixmonths = contents.strftime("%d, %B, %y")
        for i in sixmonths:
            count += 1
        if not date:
            break
        break


print("Total requests made in the last 6 months: ", count)

data.close()
