data = list(str(input()))

weight = 0
total = 0

for i in range (len(data)):
    if data[i] == '*':
        if i % 2 == 0:
            weight += 1
        else:
            weight += 3
            
for i in range(13):
        if i % 2 == 0 and data[i] != '*':
            total += 1 * int(data[i])
        elif i % 2 != 0 and data[i] != '*':
            total += 3 * int(data[i])
        else: 
             continue

for i in range(10):       
    total += weight * i

    if total % 10 == 0:
         print(i)
    else:
         total = total - (weight * i)
         continue
    
         
