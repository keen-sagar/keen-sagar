n = 127
def time(n):
    h = 0
    m = 0
    if n > 3599:
        h = n//3600
        n = n-(3600*h)
    if n > 59:
        m = n//60
        n = n-(60*m)

    print(f"Hours:{h} Minutes:{m} Seconds:{n}")

time(n)