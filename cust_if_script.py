#!/usr/bin/env python3

message = 'Score: '

myscore = int(input("What is the numeric score? "))

if myscore > 100:
    message = message + 'not a real score'
elif myscore > 90:
    message = message + 'A'
elif myscore > 80:
    message = message + 'B'
elif myscore > 70:
    message = message + 'C'
elif myscore > 60:
    message = message + 'D'
else:
    message = message + 'F'
print(message)
