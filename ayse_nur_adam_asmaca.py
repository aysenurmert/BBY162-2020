print("Bu bir meyve ismidir.")
iskelet =["""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
   |   |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
   |   |
  / \  |
--------"""]

def kontrol (kelime,harf):
    dizi = []
    sayac = 0
    for i in kelime:
        if i == harf:
            dizi.append (sayac)
        sayac += 1

    if len (dizi) == 0:
        return False
    else:

        return dizi

kelime = "böğürtlen"

for i in range(0,len(kelime)):
    print("-",end="")
print("")
hak = len(iskelet)
hata = 0
tahmin_edilenler = []
while hak > 0:
    tahmin = input("Bir harf tahmin ediniz:")
    cevap = kontrol(kelime,tahmin)
    if cevap == False:
        print (iskelet[hata])
        hata += 1
        hak -= 1
    else:
        for i in cevap:
            tahmin_edilenler.append(i)
        for i in range(0,len(kelime)):
            if i in tahmin_edilenler:
                print(kelime[i]+ " ", end="")
            else:
                print("_", end="")
        print("")
    if len(tahmin_edilenler) == len(kelime):
        hak = -1

if hak == 0:
    print("Üzgünüm, kaybettin..!")
else:
    print("Bravo, kazandın..!")