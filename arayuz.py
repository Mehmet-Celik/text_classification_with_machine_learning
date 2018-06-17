import sqlite3
connection = sqlite3.connect("classification.db")
cur = connection.cursor()

spr =0
tek=0
sag=0
siy=0
eko=0
oto=0
spres=[]
ekoes=[]

dizi=[]
sinif="x"
isimler = ["ahmet","hakem","ekonomi","futbol","bono","hisse","tahvil","para","hesap"]


for isim in isimler:
    kontrol= cur.execute("""SELECT kelime,entropi FROM SPOR WHERE kelime=?""",(isim,))
    o = list(cur)
    if len(o) is 0 :
        spr += 0
    else:
        spres.append(o[0][0])
        print(spres)
        spr += o[0][1]

    connection.commit()

print(spr)
dizi.append(spr)
print(dizi)

for isim in isimler:
    cur.execute("""SELECT entropi FROM EKONOMI WHERE kelime=?""",(isim,))
    o=list(cur)
    if len(o) is 0:
        eko+=0

    else:
        eko+=o[0][0]
print(eko)
dizi.append(eko)
print(dizi)

for isim in isimler:
    cur.execute("""SELECT entropi FROM OTOMOBIL WHERE kelime=?""",(isim,))
    o=list(cur)
    if len(o) is 0:
        continue
    else:

        oto+=o[0][0]
print(oto)
dizi.append(oto)
print(dizi)

for isim in isimler:
    cur.execute("""SELECT entropi FROM SIYASI WHERE kelime=?""",(isim,))
    o=list(cur)
    if len(o) is 0:
        continue
    else:

        siy+=o[0][0]
print(siy)
dizi.append(siy)
print(dizi)

for isim in isimler:
    cur.execute("""SELECT entropi FROM TEKNOLOJI WHERE kelime=?""",(isim,))
    o=list(cur)
    if len(o) is 0:
        continue
    else:

        tek+=o[0][0]
dizi.append(tek)
print(dizi)

for isim in isimler:
    cur.execute("""SELECT entropi FROM SAGLIK WHERE kelime=?""",(isim,))
    o=list(cur)
    if len(o) is 0:
        continue
    else:
        sag+=o[0][0]
print(sag)
dizi.append(sag)
print(dizi)


#sıralama
s=0
for d in range(0,5):
    if s<dizi[d]:
        s=dizi[d]
    else:
        continue


if s==spr:
    print("sınıfı spordur")
elif s==eko:
    print("sınıfı ekonomi")
elif s==oto:
    print("sınıfı otomobil")
elif s==sag:
    print("sağlık")
elif s==tek:
    print("teknoloji")
else:
    print("siyaset")

connection.commit()