# برنامه ای بنویسید که یک عدد از کاربر گرفته و مربع)توان دوم
# و مکعب توان سوم( آن را چاپ کند


#  مکعب=به توان 3 میرسانیم3^8
#  مربع =به توان 2 میرسانیم 2^6

number_one = int(input("Enter Number = "))
number = number_one ** 3
number_2 = number_one ** 2
print(number_one, "^", " 3", "="f"{number}")
print(number_one, "^", "2", "=", number_2)
