from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    # Sinh ID tự động
    def generateID(self):
        maxID = 1

        if(self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id

            for sv in self.listSinhVien:
                if(maxID < sv._id):
                    maxID = sv._id

            maxID += 1

        return maxID

    # Số lượng sinh viên
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    # Nhập sinh viên
    def nhapSinhVien(self):
        svId = self.generateID()

        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))

        sv = SinhVien(svId, name, sex, major, diemTB)

        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    # Hiển thị danh sách sinh viên
    def showSinhVien(self, listSV):

        print("{:<8} {:<18} {:<10} {:<15} {:<10} {:<12}".format(
            "ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"
        ))

        if(listSV.__len__() > 0):

            for sv in listSV:
                print("{:<8} {:<18} {:<10} {:<15} {:<10} {:<12}".format(
                    sv._id,
                    sv._name,
                    sv._sex,
                    sv._major,
                    sv._diemTB,
                    sv._hocLuc
                ))

    # Xếp loại học lực
    def xepLoaiHocLuc(self, sv: SinhVien):

        if(sv._diemTB >= 8):
            sv._hocLuc = "Gioi"

        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"

        elif(sv._diemTB >= 5):
            sv._hocLuc = "Trung Binh"

        else:
            sv._hocLuc = "Yeu"

    # Lấy danh sách sinh viên
    def getListSinhVien(self):
        return self.listSinhVien


# ===== CHƯƠNG TRÌNH CHÍNH =====

if __name__ == "__main__":

    qlsv = QuanLySinhVien()

    qlsv.nhapSinhVien()
    qlsv.nhapSinhVien()

    print("\nDANH SACH SINH VIEN:\n")

    qlsv.showSinhVien(qlsv.getListSinhVien())