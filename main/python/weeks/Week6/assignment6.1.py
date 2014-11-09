__author__ = 'Serg'
text = "X-DSPAM-Confidence:    0.8475"
column = text.find(":")
number = text[column+1:]
number = number.strip()
number = float(number)
print(number)