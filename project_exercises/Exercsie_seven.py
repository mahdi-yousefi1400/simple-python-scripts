#  یک برنامه پایتون بنویسید تا مساحت یک مثلث را با توجه به
# قاعده و ارتفاع آن محاسبه کند.

rule = int(input(":قاعده را وارد کنید\t "))
height = int(input(":ارتفاع را وارد کنید\t"))
Area_triangle = (rule * height) / 2

print(f"مساحت مثلث: {Area_triangle}")

