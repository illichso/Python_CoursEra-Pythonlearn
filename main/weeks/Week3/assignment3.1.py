from pip.backwardcompat import raw_input

__author__ = 'Sergii'
hrs = raw_input("Enter Hours\n")
h = float(hrs)
rateInput = raw_input("Enter Rate\n")
rate = float(rateInput)
if h <= 40:
    print(h * rate)
else:
    print("40 hours = " + str(40 * rate))
    print("extra " + str(h - 40) + " hours = " + str((h - 40) * rate * 1.5))
    print(str(40 * rate + (h - 40) * rate * 1.5))
