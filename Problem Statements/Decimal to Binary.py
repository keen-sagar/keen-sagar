# Decimal to Binary
decimal = int(input("Enter Decimal Value: "))
# logic implementation
"""def dtb(decimal):
    binary = ""
    count = 0
    if decimal == 0:
        binary = 0
    while decimal > 0:
        quotient = int(decimal/2)
        rem = str(decimal % 2)
        decimal = quotient
        binary = rem + binary

    for i in binary:
        if i == "1":
            count = count + 1
    return binary, count

binary, count = dtb(decimal)
print(f"Binary Value of {decimal} is: ",binary)
print(f"Number of Ones in {binary}: ",count)"""

# one line implimentation
print(bin(decimal).replace("0b","").count("1"))


