def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"

def main():
    print("Program Kalkulator BMI")
    print("-----------------------")
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (m): "))

    bmi = hitung_bmi(berat_badan, tinggi_badan)
    print("BMI Anda adalah:", round(bmi, 2))
    print("Kategori BMI Anda:", kategori_bmi(bmi))

if _name_ == "_main_":
     main()