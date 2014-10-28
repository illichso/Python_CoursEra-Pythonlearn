from pip.backwardcompat import raw_input

__author__ = 'Sergii'
hrs = raw_input("Enter Hours\n")
try:
    h = float(hrs)
except Exception:
    print("You shouda entered numbers!")
    quit()
rateInput = raw_input("Enter Rate\n")
try:
    rate = float(rateInput)
except Exception:
    print("You shouda entered numbers!")
    quit()
try:
    if h <= 40:
        print(h * rate)
    else:
        print(str(40 * rate + (h - 40) * rate * 1.5))
except Exception:
    print("We can not do mathematical operations to words!")
    quit()
