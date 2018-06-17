
import jpype

class Baglan:

    def __init__(self):

        self.yenikelimeler = []
        self.yenitip = []
        self.fiil = []
        self.edat = []
        self.zaman = []
        self.zamir = []
        self.baglac = []
        self.sayi = []
        self.ozel = []
        self.isim = []
        self.sifat = []
        self.bilinmeyenkelimeler = []
        self.sozluk = []

    def zemberekbaglan(self, words):

        self.yenikelimeler = words
        # JVM başlat
        # Aşağıdaki adresleri java sürümünüze ve jar dosyasının bulunduğu klasöre göre değiştirin

        """jpype.startJVM("C:/Program Files/Java/jre1.8.0_151/bin/server/jvm.dll",
                 "-Djava.class.path=C:/Users/kubra/Desktop/ates/zemberek-tum-2.0.jar", "-ea")"""

        jpype.startJVM("C:/Program Files/Java/jre1.8.0_151/bin/server/jvm.dll",
                 "-Djava.class.path=C:/Users/Mehmet/PycharmProjects/classification/zemberek-tum-2.0.jar", "-ea")



        # Türkiye Türkçesine göre çözümlemek için gerekli sınıfı hazırla

        Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")

        # tr nesnesini oluştur

        tr = Tr()

        # Zemberek sınıfını yükle

        Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")

        # zemberek nesnesini oluştur

        zemberek = Zemberek(tr)

        #Çözümlenecek örnek kelimeleri belirle

        for kelime in self.yenikelimeler:

            if kelime.strip() > '':

                yanit = zemberek.kelimeCozumle(kelime)

                if yanit:

                    if str(yanit[0]).split('tip:')[1].split('}')[0] == "OZEL":

                        self.ozel.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "ISIM":

                        self.isim.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "SIFAT":

                        self.sifat.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "FIIL":

                        self.fiil.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "EDAT":

                        self.edat.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "ZAMAN":

                        self.zaman.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "BAGLAC":

                        self.baglac.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "SAYI":

                        self.sayi.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    elif str(yanit[0]).split('tip:')[1].split('}')[0] == "ZAMIR":

                        self.zamir.append(str(yanit[0]).split('Kok: ')[1].split(' ')[0])

                    else:
                        print("*****************bu yeni bir tip**************** ")
                        print(yanit[0].tip)

                        self.yenitip.append(yanit[0].tip)



                else:
                    self.bilinmeyenkelimeler.append(kelime)

        #JVM kapat


        jpype.shutdownJVM()

        self.sozluk = self.ozel + self.isim + self.sifat

        return self.sozluk, self.fiil, self.edat, self.zaman, self.zamir, self.sayi, self.baglac, self.bilinmeyenkelimeler, self.yenitip
