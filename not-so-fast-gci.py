import math

while True:
    o = input('Please input n: ')
    if o:
        n = int(o)
        break
if n > 0 and n <= 1024:
    answer = pow(2,n)
    print(answer)
else:
    print("Please provide a number which is more than 0 and less than oreqqual to 1024")
    exit
