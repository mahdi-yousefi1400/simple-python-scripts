
# simple-python-scripts

 
 1-دو متغیر x و y را تعریف کنید و به آنها مقادیری اختصاصدهید. سپس، مقادیر x و y را بدون استفاده از متغیر سوم عوض کنید.
x = 15
y = 25
x, y = y, x
print(x)
print(y)

#################################################################################################



2- برنامه ای بنویسید تا مساحت یک مستطیل را با استفاده از متغیرها محاسبه کند. طول و عرض را در متغیرها ذخیره کنید سپس مساحت را محاسبه و چاپ کنید.



length_rectangle = int(input("Enter the length of the rectangle:\t"))
width_rectangle = int(input("Enter the width of the rectangle:\t"))
are_rectangle = length_rectangle * width_rectangle
print(are_rectangle)



########################################################################################################


3- برنامه ای ایجاد کنید که دما را از سانتیگراد به فارنهایت تبدیل کند. دما را بر حسب سانتیگراد در یک متغیر ذخیره کنید، تبدیل را انجام دهید و نتیجه را چاپ کنید.
# برای تبدیل دما از سانتیگراد به فارنهایت=Fahrenheit=32+(9/5*Celsius)
celsius_c = float(input("\t :دمای مورد نظر بر حسب سانتیگراد را وارد کن"))
fahrenheit = (celsius_c * 9 / 5) + 32
print(F" دمای معادل درفارنهایت {fahrenheit}")




@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
4-مساحت و محیط دایره را محاسبه کنید. شعاع را در یک متغیرذخیره کنید و سپس مساحت و محیط را محاسبه و چاپ کنید

radius = float(input("enter the redis of the "))
π = 3.14159

# محیط دایره
circumference = radius * π * 2
print(f"محیط دایره:{circumference}")                                                                                              
                                                       

# مساحت دایره
area_of_circle = radius * π
print(f"{area_of_circle}")

                                                        
########################################

5- برنامه ای بسازید که مجموع، تفاوت، حاصلضرب و توان دو عدد را محاسبه کند


numbers_one = int(input("Enter  number:\t"))
numbers_tow = int(input("Enter  number:\t"))
sum_result = numbers_one + numbers_tow
difference = numbers_one - numbers_tow
product = numbers_one *numbers_tow
power = numbers_one ** numbers_tow
print(f"مجموع {numbers_one} و {numbers_tow}: {sum_result}")
print(f"تفاوت {numbers_one} و {numbers_tow}: {difference}")
print(f"حاصلضرب {numbers_one} و {numbers_tow}: {product}")
print(f"{numbers_one} به توان {numbers_tow}: {power}")




#########################################################
 6-برنامه ای بسازید که میانگین سه عدد را محاسبه کند. سه متغیر x و y و z را تعریف کنید، آنها را در متغیرها ذخیره کنید، میانگین را محاسبه کنید و نتیجه را چاپ کنید


number_1 = 20
number_2 = 20
number_3 = 20
Sum = number_1 + number_2 + number_3
average = Sum / 3
print(f"{average}")

######################################################################################



7- یک برنامه پایتون بنویسید تا مساحت یک مثلث را با توجه به قاعده و ارتفاع آن محاسبه کند.
rule = int(input(":قاعده را وارد کنید\t "))
height = int(input(":ارتفاع را وارد کنید\t"))
Area_triangle = (rule * height) / 2
print(f"مساحت مثلث: {Area_triangle}")



####################################################################################################


8- یک متغیر ایجاد کنید و سن خود را در آن بنویسد. سالی که درآن 100 ساله خواهد شد را محاسبه کنید

 تعریف متغیر و ذخیره سن کنونی
age = int(input("Enter age:\t"))
 
current_year = 1403   #سال کنونی را وارد کنید
years_to_100 = 100 - age
year_turn_100 = current_year + years_to_100  # محاسبه سالی که 100 ساله خواهید شد

print(f"شما در سال {year_turn_100} صد ساله خواهید شد.")


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


                                                           
# 9( نام متغیرها در قطعه کد داده شده را مطابق با قراردادهای نامگذاری 8 PEP تغییر دهید:
num_1 = 42
num_2 = 13
result = num_1, num_2
print(result)
