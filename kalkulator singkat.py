def kalkulator():
    print("=== Kalkulator Sederhana ===")
    print("Operator: +, -, *, /")
    
    try:
        a = float(input("Angka pertama: "))
        op = input("Operator: ")
        b = float(input("Angka kedua: "))
        
        if op == '+': hasil = a + b
        elif op == '-': hasil = a - b
        elif op == '*': hasil = a * b
        elif op == '/': hasil = a / b if b != 0 else "Error: Pembagian dengan nol!"
        else: hasil = "Error: Operator tidak valid!"
        
        print(f"\nHasil: {a} {op} {b} = {hasil}")
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")

if __name__ == "__main__":
    kalkulator()