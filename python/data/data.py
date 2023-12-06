import datetime

x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.strftime("%A"))


x2 = datetime.datetime(2020, 5, 17)

print(x2.month)

# formatando a data em strings legiveis

x3 = datetime.datetime(2018, 6, 1)

print(x3.strftime("%B"))