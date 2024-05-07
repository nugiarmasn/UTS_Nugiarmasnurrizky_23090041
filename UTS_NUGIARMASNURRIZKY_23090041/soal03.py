def hitung_total_harga(jumlah_barang):
    total_harga = 0
    for i in range(jumlah_barang):
        harga_barang = float(input("Masukkan harga barang ke-{}: ".format(i+1)))
        total_harga += harga_barang
    return total_harga

def main():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    total_harga = hitung_total_harga(jumlah_barang)
    print("Total harga belanjaan adalah: Rp", total_harga)

if _name_ == "_main_":
    main()