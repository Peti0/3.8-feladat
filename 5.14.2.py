def nyaralas():
   
    x = int(input("Mikor indultál el?"))
    y = int(input("Hány napig voltál távol?"))

    x =(x + y) % 7

    if x ==0:
        print("Hétfőn érsz haza")
    if x ==1:
        print("Kedden érsz haza")
    if x ==2:
        print("Szerdán érsz haza")
    if x ==3:
        print("Csütörtökön érsz haza")
    if x ==4:
        print("Pénteken érsz haza")
    if x ==5:
        print("Szombaton érsz haza")
    if x ==6:
        print("Vasárnap érsz haza")

nyaralas()