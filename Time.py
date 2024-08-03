import time
timestamp=int(time.strftime('%H'))
print(timestamp)
if 1 <= timestamp <= 5:
   print("Good Night")
elif 5>timestamp<=12:
   print("Good Morning");
elif 17<timestamp<21:
    print("Good Evening");
else:
   print("Good Afternoon")
