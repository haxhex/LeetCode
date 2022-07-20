j = 1
inp = 15
arr = []
while(j <= inp):
    if j % 3 == 0 and j % 5 == 0:
        arr.append("FizzBuzz")
    elif j % 3 == 0:
        arr.append("Buzz")
    elif j % 5 == 0:
        arr.append("Fizz")
    else:
        arr.append(str(j))
    j = j + 1

print(arr)