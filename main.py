# %%
class Lop:
    def __init__(self,ma,ten):
        self.ma = ma
        self.ten = ten
    def __eq__(self, other):
        if isinstance(other,Lop):
            if other.ma == self.ma:
                 return True
        return False


# %%
class Sinh_vien:
    def __init__(self,ma,ten,ma_lop):
        self.ma = ma
        self.ten = ten
        self.ma_lop = ma_lop
    def __eq__(self, other):
        if isinstance(other,Sinh_vien):
            if other.ma == self.ma:
                 return True
        return False

# %%
class Danh_sach_lop:
    def __init__(self):
        self.danh_sach = []
    def them(self,lop):
        if lop in self.danh_sach:
            return False
        self.danh_sach.append(lop)
        return True
    def xem_danh_sach(self):
        print("Danh sach lop")
        print("STT - Ma lop - Ten lop")
        stt = 1
        for lop in self.danh_sach:
            print(f"{stt} - {lop.ma} - {lop.ten} ")
            stt+=1
        
    

# %%
class Danh_sach_sinh_vien:
    def __init__(self):
        self.danh_sach = []
    def kiem_tra_lop_ton_tai(self,sinh_vien,danh_sach_lop):
        
        for lop in danh_sach_lop.danh_sach:
            if sinh_vien.ma_lop == lop.ma:
                 return True
        return False
    def them(self,sinh_vien,danh_sach_lop):
        if not self.kiem_tra_lop_ton_tai(sinh_vien,danh_sach_lop): 
            return -1
        if sinh_vien in self.danh_sach:
            return 0
        self.danh_sach.append(sinh_vien)
        return 1
    def xem_danh_sach(self):
        print("Danh sach sinh vien")
        print("STT - Ma sinh vien - Ten sinh vien - Ma lop")
        stt = 1
        for sinh_vien in self.danh_sach:
            print(f"{stt} - {sinh_vien.ma} - {sinh_vien.ten} - {sinh_vien.ma_lop} ")
            stt+=1

# %%
danh_sach_lop = Danh_sach_lop()
danh_sach_sinh_vien = Danh_sach_sinh_vien()

# %%
selection = "start"
while True:
    print("Ban muon lam gi?")
    print("Chon \"1\" : Nhap danh sach lop")
    print("Chon \"2\" : Nhap danh sach sinh vien ")
    print("Chon \"3\" : Xem danh sach lop")
    print("Chon \"4\" : Xem danh sach sinh vien ")
    print("Nhap phim khac de dung chuong trinh.")
    selection = input("Lua chon cua ban la: ")
    if not selection == "1" and not selection == "2" and not selection == "3" and not selection == "4" :
        print("Chuong trinh ket thuc.")
        break
    elif selection == "1":
        while True:
            print("Nhap \"ESC\" de tro ve xem cac lua chon chuong trinh.")
            ma_lop = input("Vui long nhap ma lop:")
            if ma_lop == "ESC": 
                break
            ten_lop = input("Vui long nhap ten lop:")
            if ten_lop == "ESC": 
                break
            if danh_sach_lop.them(Lop(ma_lop,ten_lop)) == True:
                print("Them lop thanh cong!")
                print("Tiep tuc them lop...")
            else :
                print("Lop da ton tai!, moi ban thu lai.")
    elif selection == "2":
        while True:
            print("Nhap \"ESC\" de tro ve xem cac lua chon chuong trinh.")
            mssv = input("Vui long nhap mssv:")
            if mssv == "ESC": 
                break
            ten_sinh_vien = input("Vui long nhap ten sinh vien:")
            if ten_sinh_vien == "ESC": 
                break
            ma_lop = input("Vui long nhap ma lop:")
            if ma_lop == "ESC": 
                break
            ket_qua_them = danh_sach_sinh_vien.them(Sinh_vien(mssv,ten_sinh_vien,ma_lop),danh_sach_lop)
            if ket_qua_them == -1:
                print("Lop da nhap khong ton tai! Moi ban thu lai.")
            elif ket_qua_them == 0:
                print("Sinh vien da ton tai! Moi ban nhap sinh vien khac.")
            else:
                 print("Them sinh vien thanh cong! Tiep tuc them sinh vien...")
    elif selection == "3":
        danh_sach_lop.xem_danh_sach()
    elif selection == "4":
        danh_sach_sinh_vien.xem_danh_sach()
    


            




