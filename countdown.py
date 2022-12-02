import time

def convert(jam,menit,detik):
    result = 0
    hours = jam*3600
    result+=hours
    minutes = menit*60
    result+=minutes
    result+=detik
    return result

my_time = convert(1,0,10)

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")
    time.sleep(1)

print("TIME'S UP!")