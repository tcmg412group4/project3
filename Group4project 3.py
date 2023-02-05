d = open('DataSet.txt', 'r')

#Opens the DataSet file which contains the log file imported from the URL using the import.py file

counter1 = 0

while True:
    counter1 += 1           

    line = d.readline()         # read each line and save it to a new file named 'line'

    if not line:
        break

# While loop to count all the lines in the text file, as each line represents an individual log. Stores the count in the variable counter1

counter1 -= 1

# The DataSet.txt file has one extra blank line at the end of the file which does not contain a log.     

print("Total requests made in the entire log: ", counter1)


# The last log was made on 11/Oct/1995:14:14:17
# 6 months prior to this would be 11/Apr/1995:14:14:17
# The earliest log file within the last 6 months occured on 11/Apr/1995:14:14:19


date = '[11/Apr/1995:14:14:19 -0600]'
with open(r'DataSet.txt', 'r') as file:
    logs = file.readlines()
    for log in logs:

        if log.find(date) != -1:

            print ('Total requests made in the last 6 months: ', counter1 - logs.index(log) - 1)
            # -1 is to count the log that gets excluded, as we subtract the counter in this for loop from the counter1 value
           






