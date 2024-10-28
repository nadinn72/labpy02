def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Operasi yang tersedia:")
    print("+ : Penjumlahan")
    print("- : Pengurangan")
    print("* : Perkalian")
    print("/ : Pembagian")

    try:
        # Input angka pertama
        angka1 = float(input("\nMasukkan angka pertama: "))
        
        # Input operator
        while True:
            operator = input("Masukkan operator (+, -, *, /): ")
            if operator in ['+', '-', '*', '/']:
                break
            print("Operator tidak valid! Silakan masukkan +, -, *, atau /")
        
        # Input angka kedua
        angka2 = float(input("Masukkan angka kedua: "))
        
        # Proses perhitungan
        if operator == '+':
            hasil = angka1 + angka2
            operasi = "Penjumlahan"
        elif operator == '-':
            hasil = angka1 - angka2
            operasi = "Pengurangan"
        elif operator == '*':
            hasil = angka1 * angka2
            operasi = "Perkalian"
        elif operator == '/':
            if angka2 == 0:
                raise ZeroDivisionError("Tidak dapat melakukan pembagian dengan nol!")
            hasil = angka1 / angka2
            operasi = "Pembagian"
        
        # Tampilkan hasil
        print("\n=== Hasil Perhitungan ===")
        print(f"Operasi: {operasi}")
        print(f"{angka1} {operator} {angka2} = {hasil}")
        
        # Tampilkan hasil dengan format khusus untuk pembagian
        if operator == '/' and hasil.is_integer():
            print(f"Hasil (dalam bilangan bulat): {int(hasil)}")
        
    except ValueError:
        print("\nError: Masukkan angka yang valid!")
    except ZeroDivisionError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")

def main():
    while True:
        kalkulator()
        
        # Tanya user apakah ingin melakukan perhitungan lagi
        lanjut = input("\nIngin melakukan perhitungan lagi? (Y/T): ").upper()
        if lanjut != 'Y':
            print("\nTerima kasih telah menggunakan kalkulator ini!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()