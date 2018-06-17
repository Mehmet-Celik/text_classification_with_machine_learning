import sqlite3
connection = sqlite3.connect("classification.db")
cur = connection.cursor()

class Siniflandirma:

    def __init__(self):

        self.spr = 0
        self.tek = 0
        self.sag = 0
        self.siy = 0
        self.eko = 0
        self.oto = 0
        self.spres=[]
        self.tekes = []
        self.sages = []
        self.siyes = []
        self.ekoes = []
        self.otoes = []
        self.dizi = []
        self.kelimeler = {}
        self.kelimesayisi = {}
        self.sonuc=""
        self.sonuckelime=[]

    def hesapla(self, words):

        for kelime in words:

            if kelime in self.kelimesayisi:

                self.kelimesayisi[kelime] += 1

            else:

                self.kelimesayisi[kelime] = 1

        return self.kelimesayisi

    def temizle(self):

        self.kelimesayisi = {}

    def siniflandir(self, words):

        connection = sqlite3.connect("classification.db")
        cur = connection.cursor()

        self.kelimeler = words

        for kelime in self.kelimeler:

            cur.execute("""SELECT kelime,entropi FROM SPOR WHERE kelime=?""", (kelime,))
            o = list(cur)
            if len(o) is 0:
                continue
            else:
                self.spres.append(o[0][0])
                self.spr = self.spr + (o[0][1]*self.kelimeler[kelime])
        self.dizi.append(self.spr)

        for kelime in self.kelimeler:

            cur.execute("""SELECT entropi FROM EKONOMI WHERE kelime=?""", (kelime,))
            o = list(cur)
            if len(o) is 0:
                continue
            else:
                self.eko = self.eko + (o[0][0]*self.kelimeler[kelime])
        self.dizi.append(self.eko)

        for kelime in self.kelimeler:
            cur.execute("""SELECT kelime,entropi FROM OTOMOBIL WHERE kelime=?""", (kelime,))
            o = list(cur)
            if len(o) is 0:
                continue
            else:
                self.otoes.append(o[0][0])
                self.oto = self.oto + (o[0][1]*self.kelimeler[kelime])
        self.dizi.append(self.oto)

        for kelime in self.kelimeler:
            cur.execute("""SELECT kelime,entropi FROM SIYASI WHERE kelime=?""", (kelime,))
            o=list(cur)
            if len(o) is 0:
                continue
            else:
                self.siyes.append(o[0][0])
                self.siy = self.siy + (o[0][1]*self.kelimeler[kelime])
        self.dizi.append(self.siy)

        for kelime in self.kelimeler:
            cur.execute("""SELECT kelime,entropi FROM TEKNOLOJI WHERE kelime=?""", (kelime,))
            o=list(cur)
            if len(o) is 0:
                continue
            else:
                self.tekes.append(o[0][0])
                self.tek = self.tek + (o[0][1]*self.kelimeler[kelime])
        self.dizi.append(self.tek)

        for kelime in self.kelimeler:
            cur.execute("""SELECT kelime,entropi FROM SAGLIK WHERE kelime=?""", (kelime,))
            o=list(cur)
            if len(o) is 0:
                continue
            else:
                self.sages.append(o[0][0])
                self.sag = self.sag+ (o[0][1]*self.kelimeler[kelime])
        self.dizi.append(self.sag)
        print(self.dizi)


        #sıralama
        s = 0
        for d in range(0, 6):
            if s < self.dizi[d]:
                s = self.dizi[d]
            else:
                continue

        if s == self.spr:
            self.sonuc="SPOR"
            self.sonuckelime=self.spres
        elif s == self.eko:
            self.sonuc = "EKONOMİ"
            self.sonuckelime = self.ekoes
        elif s == self.oto:
            self.sonuc = "OTOMOBİL"
            self.sonuckelime = self.otoes
        elif s == self.sag:
            self.sonuc = "SAĞLIK"
            self.sonuckelime = self.sages
        elif s == self.tek:
            self.sonuc = "TEKNOLOJİ"
            self.sonuckelime = self.tekes
        else:
            self.sonuc = "SİYASET"
            self.sonuckelime = self.siyes

        connection.commit()
        return self.sonuc, self.sonuckelime
