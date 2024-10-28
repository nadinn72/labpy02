def hitung_harga_tiket(tipe_tiket, is_member):
    # Harga dasar tiket
    HARGA_REGULER = 50000
    HARGA_VIP = 100000
    DISKON_MEMBER = 0.2  # 20%

    # Menentukan harga dasar berdasarkan tipe tiket
    harga_dasar = HARGA_VIP if tipe_tiket.upper() == 'VIP' else HARGA_REGULER
    
    # Menghitung diskon jika member
    diskon = harga_dasar * DISKON_MEMBER if is_member else 0
    
    # Menghitung harga akhir
    harga_akhir = harga_dasar - diskon
    
    return harga_dasar, diskon, harga_akhir

def main():
    print("=== Program Pemesanan Tiket Bioskop ===")
    print("Tipe tiket yang tersedia:")
    print("1. Reguler (Rp50.000)")
    print("2. VIP (Rp100.000)")
    
    # Input tipe tiket
    while True:
        tipe_tiket = input("\nMasukkan tipe tiket (REGULER/VIP): ").upper()
        if tipe_tiket in ['REGULER', 'VIP']:
            break
        print("Tipe tiket tidak valid! Silakan masukkan REGULER atau VIP.")
    
    # Input status member
    while True:
        member = input("Apakah Anda memiliki kartu member? (Y/T): ").upper()
        if member in ['Y', 'T']:
            break
        print("Input tidak valid! Silakan masukkan Y atau T.")
    
    is_member = member == 'Y'
    
    # Hitung harga
    harga_dasar, diskon, harga_akhir = hitung_harga_tiket(tipe_tiket, is_member)
    
    # Tampilkan hasil
    print("\n=== Detail Pembayaran ===")
    print(f"Tipe Tiket: {tipe_tiket}")
    print(f"Status Member: {'Ya' if is_member else 'Tidak'}")
    print(f"Harga Dasar: Rp{harga_dasar:,}")
    print(f"Diskon Member: Rp{diskon:,}")
    print(f"Total Pembayaran: Rp{harga_akhir:,}")

if __name__ == "__main__":
    main()