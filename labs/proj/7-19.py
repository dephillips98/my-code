#!/usr/bin/env python3
import random
wordbank= ["indentation", "spaces"] 
tlgstudents= ['Alex', 'Benji', 'Cayla', 'Demetra', 'Derek', 'Deshawn', 'James', 'Maria', 'Marylyn', 'Nor', 'Sal', 'Sammy']
wordbank.append("4")
num = input("Choose a number 0-11\n")
num = int(num)
student_name = tlgstudents[num]
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent ")



