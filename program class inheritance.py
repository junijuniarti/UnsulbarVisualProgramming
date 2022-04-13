class ojek():
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah= daerah
    def cek_id_abang(self):
        print('\nnama:',self.nama, '\nmotor:',self.transmisi, '\ndaerah:',self.daerah)

class gojek(ojek):
    def cek_id_abang(self):
        print('cek aplikasi gojek')

ojek1= ojek('ayub','manual','makassar')
ojek2= gojek('juni','manual','mamasa')

ojek1.cek_id_abang()
ojek2.cek_id_abang()
