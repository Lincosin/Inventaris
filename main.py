from datetime import datetime

inventaris = {}

def barang_masuk ():
    barang = input("Masukkan nama barang (x untuk keluar): ")
    if not barang:
        print("Nama barang harus diisi.")
        return
    elif barang == "x":
        return
    elif barang in inventaris:
        print("Barang sudah ada dalam inventaris, silahkan pilih menu 3 untuk menambah stok.")
    else:
        try:
            jumlah = int(input("Masukkan jumlah barang: "))
            if not jumlah:
                print("Jumlah barang tidak boleh kosong.")
                return
            elif jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                return
        except ValueError:
            print("Jumlah harus berupa angka yang valid.")
            return
            
        tanggal = input("Masukkan tanggal barang masuk (yyyy-mm-dd): ").strip()
        if not tanggal:
                print("Tanggal barang masuk harus diisi.")
        else:
            try:
                tglobj = datetime.strptime(tanggal, "%Y-%m-%d")
                
                if tglobj > datetime.now():
                    print("Tanggal barang masuk tidak boleh di masa depan.")
                else:
                    inventaris[barang] = {'jumlah': jumlah, 'tanggal': tanggal}
                    print(f"\n{barang} sejumlah {jumlah} unit berhasil ditambahkan pada {tanggal}.")
                    
            except ValueError:
                print("Format tanggal salah. Gunakan format yyyy-mm-dd")    

def barang_keluar ():
    barang = input("Masukkan nama barang (x untuk keluar): ")
    if barang == "x":
        return
    elif barang not in inventaris:
        print("Barang tidak ditemukan.")
        return
    else:
        jumlah = int(input("Jumlah barang yang keluar: "))
        if jumlah > inventaris[barang]['jumlah']:
            print("Jumlah barang yang keluar melebihi jumlah yang ada.")
            return
        elif jumlah <= 0 :
            print("Tidak ada barang yang keluar")
            return
        else:
            inventaris[barang]['jumlah'] -= jumlah
            print(f"{barang} sebanyak {jumlah} dihapus dari inventaris.")
            
            

def tambah_stok ():
    barang = input("Masukkan nama barang (x untuk keluar): ")
    if barang in inventaris:
            try:
                jumlah = int(input(f"Tambahkan jumlah unit untuk {barang} : "))
                if jumlah > 0:
                    inventaris[barang]['jumlah'] += jumlah
                    print(f"({jumlah} unit untuk {barang} berhasil ditambahkan ke gudang.")
                else:
                    print("Jumlah barang harus lebih dari 0.")
            except ValueError:
                print("Input gagal, silahkan masukkan angka untuk jumlah.")
    elif barang == "x":
        return
    elif barang not in inventaris:
        pilih= input("Barang tidak ditemukan di inventaris. Ingin menambahkan barang baru? (y/n) ")
        if pilih == "y":
            barang_masuk()
        else:
            return
    else:
        print("Barang tidak tersedia.")
    
def laporan_barang ():
    print("\nLaporan Barang:")
    if not inventaris:
        print("Inventaris kosong.")
        return
    else:
        print("-" * 60)
        print(f"{'Nama Barang':<30} {'Jumlah':<15} {'Tanggal Masuk':<25}")
        print("-" * 60)
        
        # Isi tabel
        for barang, info in inventaris.items():
            print(f"{barang:<30} {str(info['jumlah']) + ' unit':<15} {info['tanggal']:<25}")
        print("-" * 60)


while True:
        print("\n===== Sistem Pencatatan Barang =====")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tambah Stok")
        print("4. Laporan Barang")
        print("5. Exit")

        choice = input("Pilih Menu (1/2/3/4/5): ")

        if choice == "1":
            barang_masuk()
        elif choice == "2":
            barang_keluar()
        elif choice == "3":
            tambah_stok()
        elif choice == "4":
            laporan_barang()
        elif choice == "5":
            print("Program Selesai. Terima kasih!")
            break
        else:
            print("Pilih dengan Benar!.")