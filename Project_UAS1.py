def nama():
    print("=================================================")
    print("|\t     PENJUALAN TIKET BIOSKOP            |") 
    print("|\t         FUTURE CINEMA                  |")
    print("|===============================================|")
    print("|_______________________________________________|")
    print("| No          Nama Film         Harga           |")
    print("|_______________________________________________|")
    print("| 1           Iron Man 2        40000           |")
    print("| 2           Monster Inc 2     35000           |")
    print("| 3           The Avenger       50000           |")
    print("| 4           Star Wars 2       30000           |")
    print("|_______________________________________________|")
nama()

input("Nama Petugas  :")
input("Nama Customer :")
daftar=int(input("Jumlah Pembelian :"))
nomor = []
banyak = []
nama_film = []
harga = []
jumlah = []
i = 0
for i in range(daftar):
    print("Pembelian ke - ", i+1)
    nomor.append(input("No. Film [1/2/3/4/] :"))
    banyak.append(int(input("Banyak Tiket :")))
    if nomor[i] == "1" :
        nama_film.append("Iron Man 2     ")
        harga.append("40000")
        jumlah.append(banyak[i]*int("40000"))
    elif nomor[i] == "2" :
        nama_film.append("Monster Inc 2  ")
        harga.append("35000")
        jumlah.append(banyak[i]*int("35000"))
    elif nomor[i] == "3" :
        nama_film.append("The Avenger    ")
        harga.append("50000")
        jumlah.append(banyak[i]*int("50000"))
    elif nomor[i] == "4" :
        nama_film.append("Star Wars 2    ")
        harga.append("30000")
        jumlah.append(banyak[i]*int("30000"))
    else:
        nama_film.append("Tidak ditemukan")
        harga.append("0")
        jumlah.append(banyak[i]("0"))    


    i = i + 1

print("=========================================================================")
print("\t              PROGRAM TIKET BIOSKOP     ")
print("\t                  FUTURE CINEMA             ")
print("=========================================================================")
print("No.         Nama Film             Harga     Total Tiket       Total Harga")
print("_________________________________________________________________________")
jumlah_bayar = 0
n = 0
for n in range(daftar):
    jumlah_bayar = jumlah_bayar + jumlah[n]
    print("%i           %s       %s        %i                %i" % (n+1,         nama_film[n],       harga[n],      banyak[n],     jumlah[n]))
    n = n + 1

pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("Jumlah Bayar     :", jumlah_bayar)
print("PPN 10%          :", pajak)
print("Total Bayar      :", total_bayar)
pembayaran=int(input("Bayar            : " ))
kembalian=pembayaran-total_bayar
print("Kembali          :", kembalian)



print("                Di susun oleh  :     Kelompok 4")
print("                                 1.Arif Okfiandi")
print("                                 2.Rico Septa Ardinka")
print("                                 3.Fendy Yusuf Darmawan Margono")
print("                                 4.Muhamad Naufal Ar-Rasyid")

def ucapan():
    kata=("========================== TERIMA KASIH =================================")

    return kata
print(ucapan())

