# کاراکتر های وِیژه
print("mahdi\"yousefi")  # خروجی mahdi"yousefi
# برای اینکه دابل کوتیشین چاپ بشه


# -----------------------------------------------------------


# هر جا بخواهم بک اسلش را چاپ کنم میتوانم یک بک اسلش دیگری بزنم

#وقتی که بک اسلش را در کد درایم و بعد آن تی میاد مثل مثال زیر ما باید یک بک اسلش دیگری را هم بزنیم برا یلغو دستور


print("mahdi\\tyousefi")

# ------------------------------------------------------------------

# هر کارکتر که داریم یک سری کد دارند برای به دست آوردن آنها با استفاده از توابع زیر استفاده میکنیم
# دو نوع کد اسکی وکد یونیکد
# ASCII=تعداد حرف کتری را شمال میشود 127دارد  https://www.asciitable.com/
# UNICODE= همه کاراکتر ها را میگید تعداد آنها از کد های اسکی بیشتر است https://www.utf8-chartable.de/
print(ord('C'))
print(chr(33))


# برای چاپ کارکتر های خاص روی کیبورد نیست میتوانم با دستورات زیر استفاده کنیم

print("char : \u00AB")
print("char : \052	")   #مبنای 8یک یک اسلش میزنم
print("char : \x2a	")   #مبنای 16بک اسلش بعد ان یک xمیزنیم



