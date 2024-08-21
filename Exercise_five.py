#  برنامه ای بسازید که مجموع، تفاوت، حاصلضرب و توان دو عدد
# را محاسبه کند


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