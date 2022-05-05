'''
Question: find the basic roman Numerals(str)
example:
input: 'iv'
output: 4
input: 'xlvi'
output: 46
input: 'xxiv'
output: 24
'''

#a= input("Enter the Roman Number String")
a = ['xlvi','xx','iv','xix','xxiv']
def roman(str1):
    rs = []
    for k in range(0,len(str1)):
        str = str1[k].upper()
        value_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        temp = []
        for i in str:
            x = value_dict[i]
            temp.append(x)

        l = len(temp)+1
        for j in range(-1,-l,-1):
            if j < -1:
                if temp[j] >= temp[j+1]:
                    result = result + temp[j]
                else:
                    result = result - temp[j]
            else:
                result = temp[j]
        rs.append(result)
    return rs




result = roman(a)
print(result)