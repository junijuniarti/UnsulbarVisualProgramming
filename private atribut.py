# class

#juniarti_D0219008
class mahasiswa():

    __nilai = 0 # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama, 'lulus')

# main programnya

juni = mahasiswa("juniarti (D0219008) dinyatakan:", 219008)
ayub = mahasiswa("ayub fetmen (D02190011)dinyatakan:", 13317002)

juni.uts(10)
juni.uas(50)
juni.check_status()
ayub.uts(5)
ayub.uas(25)
ayub.__nilai = 60
ayub.check_status()
