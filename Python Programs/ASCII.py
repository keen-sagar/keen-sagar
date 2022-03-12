#convert CHAR to ASCII and viceversa
#ord will convert char to ascii
#chr will convert ascii to char

code = "hello"
code =list(code)
length = len(code)
for i in code:
    x = (ord(i)+4)
    y = chr(x)
    print(y)



