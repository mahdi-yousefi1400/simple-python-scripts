# مساحت و محیط دایره را محاسبه کنید. شعاع را در یک متغیر
# ذخیره کنید و سپس مساحت و محیط را محاسبه و چاپ کنید

radius = float(input("enter the redis of the "))
π = 3.14159

# محیط دایره
circumference = radius * π * 2
print(f"محیط دایره:{circumference}")

# مساحت دایره
area_of_circle = radius * π
print(f"{area_of_circle}")


# 9( نام متغیرها در قطعه کد داده شده را مطابق با قراردادهای
# نامگذاری 8 PEP تغییر دهید:
num_1 = 42
num_2 = 13
result = num_1, num_2
print(result)