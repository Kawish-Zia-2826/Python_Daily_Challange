print("this is day three of pyhton programing")
print("print a num to check its prime or not")
num = int(input())
if num == 1 or num < 1 or num == 0:
    print("not a prime number")
elif num % 2 == 0:
        print("not a prime number")
else:
        print("prime number is",num)