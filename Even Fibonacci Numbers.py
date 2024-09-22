limit = 400000
n1 = 1
n2 = 1
sum = 0
while limit > 0:
    limit = limit - 1
    nth = n1 + n2 
    n1 = n2 
    n2 =nth 
    if nth % 2:
        sum = sum + nth
print(sum)
