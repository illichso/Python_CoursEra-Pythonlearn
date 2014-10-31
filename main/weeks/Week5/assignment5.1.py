from pip.backwardcompat import raw_input

__author__ = 'Sergii'

largest = None
smallest = None
intNum = None


def checkForMinNumber(intNum, largest):
    if largest is None:
        largest = intNum
    elif intNum > largest:
        largest = intNum

def checkForMaxNumber(intNum, smallest):
    if smallest is None:
        smallest = intNum
    elif intNum < smallest:
        smallest = intNum


def printResults():
    # print "Maximum", largest
    print("Maximum is ", largest)
    print("Minimum is ", smallest)


while True:
    rawNum = raw_input("Enter a number: ")
    if rawNum == "done":
        break
    try:
        intNum = int(rawNum)
    except Exception:
        print("Invalid input")
        continue

    if largest is None:
        largest = intNum
    elif intNum > largest:
        largest = intNum

    if smallest is None:
        smallest = intNum
    elif intNum < smallest:
        smallest = intNum

    # checkForMaxNumber(intNum, largest)
    # checkForMinNumber(intNum, smallest)

printResults()




