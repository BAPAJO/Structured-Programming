Bindo = 0
IPA = 0
MTK = 0

Bindo = int(input("Input Nilai Bahasa Indonesia     : "))
while not int(Bindo) in range(0,101):
    Bindo = int(input("Input Nilai Bahasa Indonesia hanya 0 sampai 100: "))
    
IPA = int(input("Input Nilai IPA                  : "))
while not int(IPA) in range(0,101):
    IPA = int(input("Input Nilai IPA hanya 0 sampai 100: "))

MTK = int(input("Input Nilai Matematika           : "))
while not int(MTK) in range(0,101):
    MTK = int(input("Input Nilai Matematika hanya 0 sampai 100 : "))
    
if (Bindo > 60 and IPA > 60 and MTK > 70):
    print("Status Kelulusan: LULUS!")
else:
    print("Status Kelulusan: TIDAK LULUS!")
    print("Sebab:")
    if (Bindo < 60):
        print("Nilai Bahasa Indonesia dibawah 60")
    if (IPA < 60):
        print("Nilai IPA dibawah 60")
    if (MTK < 70):
        print("Nilai MTK dibawah 70")