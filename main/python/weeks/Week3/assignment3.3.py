__author__ = 'Serg'
from pip.backwardcompat import raw_input

scoreText = raw_input("Enter score\n")
score = float(scoreText)
if score > 1. or score < 0.:
    print("The value is wrong")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
