#-*-coding:utf8-*-
from tkinter import *
from tkinter import filedialog
from tkinter import font
import siniflandirma
import zemberekj
import dosya
import vericekme



class Filedialog:


    '''jpype.startJVM("C:/Program Files/Java/jre1.8.0_151/bin/server/jvm.dll",
             "-Djava.class.path=C:/Users/kubra/Desktop/ates/zemberek-tum-2.0.jar", "-ea")'''

    def __init__(self):

        self.spr = 0
        self.tek = 0
        self.anapencere = Tk()
        self.anapencere.title("Metin Sınıflandırma")
        self.anapencere.config(bg="white")
        self.frame1 = Frame(self.anapencere)
        self.frame1.config(bg="white")
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.anapencere)
        self.frame2.config(bg="white")
        self.frame2.pack(side=TOP)
        self.yenikelimeler = []




        # STİLLER
        self.baslikstil = font.Font(family='Helvetica', size=36, weight=font.BOLD, slant="italic", underline=1)
        self.sinifstil = font.Font(family='Helvetica', size=20, weight=font.BOLD, slant="italic")

        self.baslik = Label(self.frame1, text="Metin Sınıflandırma", font=self.baslikstil, bg="white")
        self.baslik.pack()

        self.yazi = Label(self.frame2)
        self.yazi.config(text="Lütfen işlem yapmak için bir txt dosyası seçin.", bg="white")

        self.yazi1 = Label(self.frame2)
        self.yazi1.config(text="Lütfen işlem yapmak için bir haber url si girin", bg="white")

        self.urlgir = Entry(self.frame2)
        self.urlgir.config(bg="gray")

        self.btnurl = Button(self.frame2)
        self.btnurl.config(text="Sınıfını Bul", fg="red", relief=RAISED, cursor="heart")
        self.btnurl.config(command=self.vericek)

        self.dosya = Button(self.frame2)
        self.dosya.config(text="Dosya seçmek için tıklayın", fg="red", relief=RAISED, cursor="heart")
        self.dosya.config(command=self.dosyasec)

        self.yazi2 = Label(self.frame2)
        self.yazi2.config(text="Seçilen Dosya: Henüz dosya seçilmedi", fg="blue", bg="white")


        self.output = Label(self.frame2)
        self.output.config(text="Seçtiğiniz metinin sınıfı:", bg="white")
        self.output1 = Label(self.frame2)
        self.output1.config(text="SINIF", bg="gray")

        self.secilenKelimeler = Label(self.frame2)
        self.secilenKelimeler.config(text="Seçtiğiniz metinin içeriğinde ki ayırt edici sıklıkta geçen kelimeler", bg="white")
        self.secilenKelimeler1 = Message(self.frame2)
        self.secilenKelimeler1.config(text="EŞLEŞEN \n AYIRT \n EDİCİ \n KELİMELER  ", bg="white")

        self.yazi.grid(row=0, column=0)
        self.yazi1.grid(row=0, column=1)
        self.dosya.grid(row=1, column=0)
        self.urlgir.grid(row=1, column=1)
        self.yazi2.grid(row=2, column=0)
        self.btnurl.grid(row=2, column=1)
        self.output.grid(row=3, column=0)
        self.output1.grid(row=4, column=0)
        self.secilenKelimeler.grid(row=3, column=1)
        self.secilenKelimeler1.grid(row=4, column=1)

        self.anapencere.mainloop()

    def dosyasec(self):

        self.spr = 1
        dosyaal=filedialog.askopenfilename()


        if dosyaal:
            self.yazi2.config(text=dosyaal)

            kelimelerial = dosya.Dosya()

            yenikelimeler = kelimelerial.dosyaac(dosyaal)

            baglan = zemberekj.Baglan()

            diziler = baglan.zemberekbaglan(yenikelimeler)

            sinif = siniflandirma.Siniflandirma()

            kssozluk = sinif.hesapla(diziler[0])

            sinif.temizle()

            sonuc= sinif.siniflandir(kssozluk)


            self.output1.config(text=sonuc[0])
            self.secilenKelimeler1.config(text=sonuc[1])


        else:
            self.yazi2.config(text="Seçilen Dosya: Dosya Seçilmedi")

    def vericek(self):
        kubra = self.urlgir.get()
        urlal = kubra
        if urlal:

            veri = vericekme.Vericekme()

            veriler = veri.vericek(urlal)
            print(veriler[0].text)

            for veri in veriler:
                print(veri.text)
                kelimeler = veri.text.split()
                for kelime in kelimeler:
                    self.yenikelimeler.append(kelime)

            baglan = zemberekj.Baglan()

            diziler = baglan.zemberekbaglan(self.yenikelimeler)

            sinif = siniflandirma.Siniflandirma()

            kssozluk = sinif.hesapla(diziler[0])

            sinif.temizle()

            sonuc = sinif.siniflandir(kssozluk)
            self.output1.config(text=sonuc[0])
            self.secilenKelimeler1.config(text=sonuc[1])

        else:
            """Seçili url yok"""