def q3(num):
    i = 2
    while True:
        Q = num // i
        R = num % i

        if Q == R:
            break
        i += 1
    print(i)


num = int(input("Enter the Number: "))
q3(num)