import datetime

y = int(input("请输入4位数字的年份:"))
m = int(input("请输入月份:"))
d = int(input("请输入是哪一天:"))

targetDay = datetime.date(y, m, d)

daycount = targetDay - datetime.date(targetDay.year - 1, 12, 31)
print(targetDay.year)
print(datetime.date(2020-1, 12, 31))

print("%s 是 %s 年的第%s天"%(targetDay, y, daycount.days))