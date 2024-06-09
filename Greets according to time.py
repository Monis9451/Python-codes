import time
times = time.strftime('%H')
if((int(times))>4 and (int(times))<=12):
    print("Good Morning!")
elif((int(times))>12 and (int(times))<=18):
    print("Good After Noon!")
elif(((int(times))>18 and (int(times))<=24)or(int(times))<=3):
    print("Good Night!")
