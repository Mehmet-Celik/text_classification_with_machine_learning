import sqlite3
connection = sqlite3.connect("classification.db")
cur = connection.cursor()

#ekonomi
cur.execute("""SELECT COUNT(id) FROM EKONOMI""")
countkayit = list(cur)
print(countkayit[0][0])
x=countkayit[0][0]

cur.execute("""SELECT SUM(frekans) from EKONOMI""")
sumfrekans = list(cur)
print(sumfrekans[0][0])
y=sumfrekans[0][0]

print(x*y)
geneltoplam=x*y
z=geneltoplam

cur.execute("""select * from EKONOMI""")
rows = cur.fetchall()
print(rows[0])
print(rows[0][0])

for row in rows:
    """"print(row[3])
    print(row[0])"""
    a=int(row[0])
    """print(a)"""
    cur.execute("SELECT frekans FROM EKONOMI WHERE id=?",(a,))
    frekans = list(cur)
    print(frekans[0][0]/z)
#entropi 2 yi ekledim çünkü entropi yi z ye bölerek yaptığım için değerler çok küçük çıktı.
    cur.execute("""UPDATE EKONOMI SET entropi=? WHERE id =? """, ((frekans[0][0]/y), a))
    cur.execute("""UPDATE EKONOMI SET entropi1=? WHERE id =? """, ((frekans[0][0] / z), a))

#spor
cur.execute("""SELECT COUNT(id) FROM SPOR""")
countkayit = list(cur)
print(countkayit[0][0])
x=countkayit[0][0]

cur.execute("""SELECT SUM(frekans) from SPOR""")
sumfrekans = list(cur)
print(sumfrekans[0][0])
y=sumfrekans[0][0]

print(x*y)
geneltoplam=x*y
z=geneltoplam

cur.execute("""select * from SPOR""")
rows = cur.fetchall()
print(rows[0])
print(rows[0][0])

for row in rows:
    """"print(row[3])
    print(row[0])"""
    a=int(row[0])
    """print(a)"""
    cur.execute("SELECT frekans FROM SPOR WHERE id=?",(a,))
    frekans = list(cur)
    print(frekans[0][0]/z)
#entropi 2 yi ekledim çünkü entropi yi z ye bölerek yaptığım için değerler çok küçük çıktı.
    cur.execute("""UPDATE SPOR SET entropi=? WHERE id =? """, ((frekans[0][0]/y), a))
    cur.execute("""UPDATE SPOR SET entropi1=? WHERE id =? """, ((frekans[0][0] / z), a))

#TEKNOLOJİ
cur.execute("""SELECT COUNT(id) FROM TEKNOLOJI""")
countkayit = list(cur)
print(countkayit[0][0])
x=countkayit[0][0]

cur.execute("""SELECT SUM(frekans) from TEKNOLOJI""")
sumfrekans = list(cur)
print(sumfrekans[0][0])
y=sumfrekans[0][0]

print(x*y)
geneltoplam=x*y
z=geneltoplam

cur.execute("""select * from TEKNOLOJI""")
rows = cur.fetchall()
print(rows[0])
print(rows[0][0])

for row in rows:
    """"print(row[3])
    print(row[0])"""
    a=int(row[0])
    """print(a)"""
    cur.execute("SELECT frekans FROM TEKNOLOJI WHERE id=?",(a,))
    frekans = list(cur)
    print(frekans[0][0]/z)
#entropi 2 yi ekledim çünkü entropi yi z ye bölerek yaptığım için değerler çok küçük çıktı.
    cur.execute("   ""UPDATE TEKNOLOJI SET entropi=? WHERE id =? """, ((frekans[0][0]/y), a))
    cur.execute("""UPDATE TEKNOLOJI SET entropi1=? WHERE id =? """, ((frekans[0][0] / z), a))

#SİYASİ
cur.execute("""SELECT COUNT(id) FROM SIYASI""")
countkayit = list(cur)
print(countkayit[0][0])
x=countkayit[0][0]

cur.execute("""SELECT SUM(frekans) from SIYASI""")
sumfrekans = list(cur)
print(sumfrekans[0][0])
y=sumfrekans[0][0]

print(x*y)
geneltoplam=x*y
z=geneltoplam

cur.execute("""select * from SIYASI""")
rows = cur.fetchall()
print(rows[0])
print(rows[0][0])

for row in rows:
    """"print(row[3])
    print(row[0])"""
    a=int(row[0])
    """print(a)"""
    cur.execute("SELECT frekans FROM SIYASI WHERE id=?",(a,))
    frekans = list(cur)
    print(frekans[0][0]/z)
#entropi 2 yi ekledim çünkü entropi yi z ye bölerek yaptığım için değerler çok küçük çıktı.
    cur.execute("""UPDATE SIYASI SET entropi=? WHERE id =? """, ((frekans[0][0]/y), a))
    cur.execute("""UPDATE SIYASI SET entropi1=? WHERE id =? """, ((frekans[0][0] / z), a))

#OTOMOBİL
cur.execute("""SELECT COUNT(id) FROM OTOMOBIL""")
countkayit = list(cur)
print(countkayit[0][0])
x=countkayit[0][0]

cur.execute("""SELECT SUM(frekans) from OTOMOBIL""")
sumfrekans = list(cur)
print(sumfrekans[0][0])
y=sumfrekans[0][0]

print(x*y)
geneltoplam=x*y
z=geneltoplam

cur.execute("""select * from OTOMOBIL""")
rows = cur.fetchall()
print(rows[0])
print(rows[0][0])

for row in rows:
    """"print(row[3])
    print(row[0])"""
    a=int(row[0])
    """print(a)"""
    cur.execute("SELECT frekans FROM OTOMOBIL WHERE id=?",(a,))
    frekans = list(cur)
    print(frekans[0][0]/z)
#entropi 2 yi ekledim çünkü entropi yi z ye bölerek yaptığım için değerler çok küçük çıktı.
    cur.execute("""UPDATE OTOMOBIL SET entropi=? WHERE id =? """, ((frekans[0][0]/y), a))
    cur.execute("""UPDATE OTOMOBIL SET entropi1=? WHERE id =? """, ((frekans[0][0] / z), a))

#sağlık
cur.execute("""SELECT COUNT(id) FROM SAGLIK""")
countkayit = list(cur)
print(countkayit[0][0])
x=countkayit[0][0]

cur.execute("""SELECT SUM(frekans) from SAGLIK""")
sumfrekans = list(cur)
print(sumfrekans[0][0])
y=sumfrekans[0][0]

print(x*y)
geneltoplam=x*y
z=geneltoplam

cur.execute("""select * from SAGLIK""")
rows = cur.fetchall()
print(rows[0])
print(rows[0][0])

for row in rows:
    """"print(row[3])
    print(row[0])"""
    a=int(row[0])
    """print(a)"""
    cur.execute("SELECT frekans FROM SAGLIK WHERE id=?",(a,))
    frekans = list(cur)
    print(frekans[0][0]/z)
#entropi 2 yi ekledim çünkü entropi yi z ye bölerek yaptığım için değerler çok küçük çıktı.
    cur.execute("""UPDATE SAGLIK SET entropi=? WHERE id =? """, ((frekans[0][0]/y), a))
    cur.execute("""UPDATE SAGLIK SET entropi1=? WHERE id =? """, ((frekans[0][0] / z), a))

connection.commit()
connection.close()