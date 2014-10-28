from pip.backwardcompat import raw_input

__author__ = 'Sergii'

def computepay(h, rate):
    if h <= 40:
        return h * rate
    else:
        return str(40 * rate + (h - 40) * rate * 1.5)

hrs = raw_input("Enter Hours\n")
h = float(hrs)
rateInput = raw_input("Enter Rate\n")
rate = float(rateInput)
print(computepay(h, rate))



