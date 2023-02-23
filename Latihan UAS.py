menuAnswer = 0
# menu UI
while menuAnswer != 4:
    print(
"""
====================
DATA BARANG
--------------------
Menu:
1. Tambah Data
2. Hapus Data
3. Tampilkan Data
4. Exit

"""
    )

# menu
    menuAnswer = int(input("Pilihan Menu: "))
    if menuAnswer == 1:
        print("--------------------------------------")
        addData = str(input("Masukkan Data: "))
        fo = open("dataBase.txt", "a")
        fo.write("- ", addData + "\n")
        menuAnswer -= 1

    elif menuAnswer == 2:
        print("--------------------------------------")
        delData = str(input("Data yang dihapus: "))
        fo = open("dataBase.txt", "w+")
        if fo in [delData]:
            fo.seek(delData)
            fo.truncate()

    elif menuAnswer == 3:
        print("--------------------------------------")
        fo = open("dataBase.txt", "r")
        while True:
            readLines = fo.read()
            print(readLines)
            print("--------------------------------------")
            break
        menuAnswer -= 3
    elif menuAnswer == 4:
        exit
    else:
        exit
