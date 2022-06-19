def stock(price):
    min = price[0]
    max = price[0]
    for i in range(1,len(price)):
        if price[i] < min:
            min = price[i]
            minday = i+1
        if price[i] > max:
            max = price[i]
            maxday = i+1
    if minday > maxday:
         maxday = minday
         max = min

    return int(min), int(minday), int(max), int(maxday)



price = [3,5,11,7,3,2]
result = stock(price)

print(f"Buy on day {result[1]} for {result[0]}")
print(f"Sold on day {result[3]} for {result[2]}")
print(f"Total profit: {result[2]-result[0]}")