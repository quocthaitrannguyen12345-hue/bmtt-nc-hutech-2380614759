#Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(n):
    # Chuyển đổi chuỗi nhị phân thành số nguyên
    so_thap_phan = int(so_thap_phan, 2)
    # Kiểm tra nếu số nguyên chia hết cho 5
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
# Nhập chuỗi nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy) ")
# Tách chuỗi thành các số nhị phân và kiểm tra có chia hết cho 5 
so_nhi_phan_list = chuoi_so_nhi_phan.split(",")
so_chia_het_cho_5 = [so for so_nhi_phan in so_nhi_phan_list if chia_het_cho_5(so)]
# In ra các số nhị phân chia hết cho 5
if len(so_chia_het_cho_5) > 0:
    ket_qua = ", ".join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")