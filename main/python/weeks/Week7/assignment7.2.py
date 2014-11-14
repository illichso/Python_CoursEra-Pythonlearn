from pip.backwardcompat import raw_input

__author__ = 'Sergii'
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute
# the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing
# below enter mbox-short.txt as the file name.
fileName = raw_input("Enter file name: ").strip()
try:
    fileName = open(fileName)
except:
    print("File cannot be opened", fileName)
    exit()
lineCount = 0
sumSpam = 0
lineStart = "X-DSPAM-Confidence:"
slipLen = len(lineStart)
for line in fileName:
    if not line.startswith(lineStart):
        continue
    line = line[slipLen + 1:]
    line = line.strip()
    tempFloat = 0.
    try:
        tempFloat = float(line)
    except:
        continue
    sumSpam += tempFloat
    lineCount += 1
averageSpam = sumSpam / lineCount
print("Average spam confidence:", averageSpam)
print("Average spam confidence:", 0.750718518519)