import datetime
#1
data = datetime.datetime.now()-datetime.timedelta(days=5)
print(data)

#2
data = datetime.datetime.now()
yes = datetime.datetime.now() - datetime.timedelta(days=1)
tod = datetime.datetime.now()
tom = datetime.datetime.now() + datetime.timedelta(days=1)
print(yes,tod,tom)

#3
print(now.strftime("%f"))

#4
def diff(sum_date):
    now = datetime.now()  
    days_diff = now.day - sum_date
    return days_diff * 86400  
difference_seconds = diff(10)  
print(difference_seconds)