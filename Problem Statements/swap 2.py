''' Question: swap case of each character, then if a letter is between two numbers, switch the places of the two numbers.
Ex:
input:Hello -5LOL6
output: hELLO -6lol5
input: 2S 6 du5d4e
output: 2s 6 DU4D5E '''
a = input("Enter a String")
str = "ABCf"
def case(str):
    str1 = ""
    for i in str:
        if i.isupper():
            str1 = str1 + i.lower()
        elif i.islower():
            str1 = str1 + i.upper()
        else:
            str1 = str1 + i


    result = swap(str1)
    return result

def swap(str1):
    check = ['1','2','3','4','5','6','7','8','9','0']
    str1 = list(str1)
    count = 0
    j = 0
    swap1 = []
    for i in str1:
        if i in check:
            count += 1
            swap1.append(j)

        elif i == " ":
            count = 0
            swap1 = []

        else:
            pass

        if count == 2:
            str1[swap1[0]], str1[swap1[1]] = str1[swap1[1]], str1[swap1[0]]
            count = 0
            swap1 = []

        j += 1
    str2 = ''
    for ele in str1:
        str2 += ele
    return str2


result = case(a)
print(result)