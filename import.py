import urllib.request

textfile = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
data = open("DataSet.txt", "w+")

for line in textfile:
    strline = str(line)
    data.write(strline + '\n' )

data.close()

# The above portion imports the data from the webserver into a new .txt file called DataSet
# The for loop prints out each new log into a new line to seperate logs
# Once you run this program, will have a copy of the data in a text file on your local computer