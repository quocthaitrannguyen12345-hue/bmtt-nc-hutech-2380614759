#Nhập số từ người dùng
so = input("Nhập một số nguyên: ")
#Kiểm tra nếu số là chẵn hay không
if int(so) % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải là số chẵn.")