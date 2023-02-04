d = open('DataSet.txt', 'r')

#opens the DataSet file which contains the log file imported from the URL using the import.py file

counter1 = 0

while True:
    counter1 += 1

    line = d.readline()

    if not line:
        print(counter1)
        break

# while loop to count all the lines in the text file, as each line represents an individual log. Stores the count in the variable counter1

counter1 = counter1 - 1

# the DataSet.txt file has one extra blank line at the end of the file which does not contain a log.     

print("Total requests made in the entire time period of the log: ", counter1)

print("Total requests made in the last 6 months: ")


