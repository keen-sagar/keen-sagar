
def sort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                #list[i], list[i+1] = list[i+1], list[i]

                list[i] = list[i] + list[i+1]
                list[i+1] = list[i] - list[i+1]
                list[i] = list[i] - list[i+1]
    print(list)






list = [112,32,65,10,60,45,7,23,34,67,87,90,109,187]
sort(list)