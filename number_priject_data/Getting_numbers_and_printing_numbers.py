
# یک برنامه بنویسید که اعاد سه رقمی را بگیرد و ارقام انها را جدا جدا چاپ کند

y = int(input("enter number:\t"))
temp = y % 10
print(temp)
y = y // 10
temp = y % 10
print(temp)
y = y // 10
temp = y % 10
print(y)
