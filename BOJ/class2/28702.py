data = []
result = 0

for i in range(3):
    n = input()
    data.append(n)

for i in data:
    if i.isdigit() == True:
        result += int(i)
        if data.index(i) == 0:
            result += 3
        elif data.index(i) == 1:
            result += 2
        elif data.index(i) == 2:
            result += 1
        break
    else: 
        continue

if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0 and result % 5 != 0:
    print('Fizz')
elif result % 3 != 0 and result % 5 == 0:
    print('Buzz')
elif result % 3 != 0 and result % 5 != 0:
    print(result)
