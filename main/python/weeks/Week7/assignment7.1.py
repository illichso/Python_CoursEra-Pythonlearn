from pip.backwardcompat import raw_input

__author__ = 'Sergii'
# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
fileName = raw_input("Enter file name: ").strip()
try:
    fileName = open(fileName)
except:
    print("File cannot be opened", fileName)
    exit()
for line in fileName:
    line = line.upper().rstrip()
    print(line)
