# 年 月 日
# 保质期 
# 保质期+ 月 大于12月 则减12 年加1


print("请输入生产日期")
year = int(input("年"))
month = int(input("月"))
day = int(input("日"))
exp = int(input("请输入有效期"))
if month + exp > 12:
    year+=1
    month = (month + exp)-12
    print("%d-%d-%d" % (year, month, day))
else:
    month= month + exp
    print("有效期为：")
    print("%d-%d-%d" % (year, month, day))