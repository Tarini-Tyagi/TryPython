from datetime import datetime

name=input("Enter your name: ")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

hrs=int(now.strftime("%H"))
min=int(now.strftime("%M"))

if hrs>4 and hrs<12:
    print("Good Morning "+name)
elif hrs==12:
    print("Good Afternoon " + name)
elif hrs>12 and hrs<15:
    print("Good Afternoon " + name)
elif hrs>15 and hrs<22:
    print("Good Evening " + name)
else:
    print("You should sleep. It's "+current_time)
    print("Have a good night")
