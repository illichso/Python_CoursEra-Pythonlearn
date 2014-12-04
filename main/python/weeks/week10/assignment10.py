from pip.backwardcompat import raw_input
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
# messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that
# the autograder does not have support for the sorted() function.
__author__ = 'Sergii'

name = raw_input("Enter file:")
if len(name.strip()) < 1:
    name = 'mbox-short.txt'
fileHandler = open(name)
hoursList = list()

for line in fileHandler:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    hoursList.append(words[5][:2])

hourDict = dict()

for hour in hoursList:
    hourDict[hour] = hourDict.get(hour, 0) + 1

sortedHourList = sorted([(k, v) for k, v in hourDict.items()])

for k, v in sortedHourList:
    print(k, v)