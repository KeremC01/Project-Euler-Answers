number = 1000
sum = 0
 
while number >0:
    number = number - 1
    multiple_of_3 = number / 3
    multiple_of_5 = number / 5
    if multiple_of_3.is_integer() or multiple_of_5.is_integer():
        sum = sum + number
print(sum)
