def buat_kontak(nama, nomor):
    file = open ("Buku_Telepoon.txt", "a")
    file.write(nama)
    file.write(":")
    file.write(nomor)
    file.write("\n")
    file.close
    
def hapus_kontak(nama):
    file = open("Buku_Telepoon.txt", "r")
    save = {}
    i = 0
    data = file.readline()
    datanama = data.split(":")
    while data:
        if datanama[0] == nama:
            del (data)
        else:
            save[i] = data
            i = i + 1
        data = file.readline()
        datanama = data.split(":")
    file.close
    file = open("Buku_Telepoon.txt", "w")
    for x in save:
        file.write(save[x])
    file.close

def update_kontak(nama, nomor):
    file = open("Buku_Telepoon.txt", "r")
    save = {}
    i = 0
    ketemu = False
    data = file.readline()
    datanama = data.split(":")
    while data and ketemu == False:
        if datanama[0] == nama:
            datanama[1] = nomor
            data = datanama[0] + ":" + datanama[1] + "\n"
            save[i] = data
        else:
            save[i] = data
        i = i + 1
        data = file.readline()
        datanama = data.split(":")
    file.close
    file = open("Buku_Telepoon.txt", "w")
    for x in save:
        file.write(save[x])
    file.close

def cari_kontak(nama):
    print("===== Kontak yang dicari =====")
    file = open("Buku_Telepoon.txt", "r")
    data = file.readline()
    datanama = data.split(":")
    ketemu = False
    while data and ketemu == False:
        if datanama[0] == nama:
            print(data)
            ketemu = True
        else:
            data = file.readline()
            datanama = data.split(":")
    if(ketemu == False):
        print("Tidak ada kontak...")
    file.close

def tampil_kontak():
    print("=====    Daftar Kontak    =====")
    file = open("Buku_Telepoon.txt", "r")
    data = file.readline()
    while data:
        print(data)
        data = file.readline()
    file.close


while True:
    """ Tampilan menu awal  """
    print("=====    Menu    =====")
    print("1. Buat kontak baru")
    print("2. Hapus kontak")
    print("3. Perbarui kontak")
    print("4. Cari kontak")
    print("5. Lihat semua kontak")
    print("6. Keluar")
    
    i = input("Masukkan angka yang dipilih : ")

    if i == '1':
        nama = input("Masukkan nama : ")
        nomor = input("Masukkan nomor :")
        buat_kontak(nama, nomor)

    elif i == '2':
        nama = input("Masukkan nama contact yang mau di hapus : ")
        hapus_kontak(nama)

    elif i == '3':
        nama = input("masukkan nama kontak yang akan diperbarui : ")
        nomor = input("Masukkan nomor yang baru : ")
        update_kontak(nama, nomor)

    elif i == '4':
        nama = input("Masukkan nama kontak yang akan dicari : ")
        cari_kontak(nama)

    elif i == '5':
        tampil_kontak()

    elif i == '6':
        print("Keluar...")
        break