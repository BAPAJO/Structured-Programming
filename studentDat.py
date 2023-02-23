# open file

fo = open("students.dat", "r")

male = 0
female = 0

# header
print("======================================================================")
print("ID        NAME       ADDRESS     BIRTH DATE     BIRTH PLACE     GENDER") 
print("----------------------------------------------------------------------")

# data

list1 = fo.readlines()
for data in list1:
    data = data.strip()
    splittedData = data.split("#")
    print(splittedData[0].ljust(9), splittedData[1].ljust(10), splittedData[2].ljust(11), splittedData[3].ljust(14), splittedData[4].ljust(17), splittedData[5])

    if (splittedData[5] == "M"):
        male += 1
    elif (splittedData[5] == "F"):
        female += 1
print("----------------------------------------------------------------------")
print("Male Students    : ", male)
print("Female Students  : ", female)
print("----------------------------------------------------------------------")
print("Total Students   : ", male + female)
print("======================================================================")

fo.close()
