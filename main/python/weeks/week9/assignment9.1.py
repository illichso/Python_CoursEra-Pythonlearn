__author__ = 'Sergii'
# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using
# a maximum loop to find the most prolific committer.
from pip.backwardcompat import raw_input

name = raw_input("Enter file:")
if len(name.strip()) < 1:
    name = 'mbox-short.txt'
fileHandler = open(name)
emailList = list()

for line in fileHandler:
        if not line.startswith("From") or line.startswith("From:"):
            continue
        words = line.split()
        emailList.append(words[1])
emailDict = dict()
for email in emailList:
    emailDict[email] = emailDict.get(email, 0) + 1

popularEmail = None
popularEmailCount = None

for email, count in emailDict.items():
    if popularEmailCount is None or count > popularEmailCount:
        popularEmail = email
        popularEmailCount = count
print(popularEmail, popularEmailCount)


