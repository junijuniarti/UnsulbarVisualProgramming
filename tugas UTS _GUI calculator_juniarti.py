from tkinter import *

window = Tk()
window.title("TKINTER KALKULATOR GUI")
window.geometry('350x200')

label = Label(window, text="==PILIH OPERATOR DIBAWAH_by.juniarti==")
label.grid()


label1 = Label(window, text="Nilai Pertama : ",anchor="e",width=20)
label1.grid(column=0, row=1)

nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=1)



label2 = Label(window, text="Nilai Kedua : ",anchor="e",width=20)
label2.grid(column=0, row=2)

nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=2)

label3 = Label(window, text="Hasil : ",anchor="e",width=20)
label3.grid(column=0, row=3)

hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=3)

def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))

def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))

def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))

def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))


tombol = Button(window, text="Tambah", command=tambah)
tombol.grid(column=0, row=4)

tombol = Button(window, text="Kurang", command=kurang)
tombol.grid(column=0, row=5)

tombol = Button(window, text="Kali", command=kali)
tombol.grid(column=1, row=4)

tombol = Button(window, text="Bagi", command=bagi)
tombol.grid(column=1, row=5)




window.mainloop() 
