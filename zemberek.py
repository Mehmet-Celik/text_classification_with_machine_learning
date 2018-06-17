
import jpype
# JVM başlat
# Aşağıdaki adresleri java sürümünüze ve jar dosyasının bulunduğu klasöre göre değiştirin
jpype.startJVM("C:/Program Files/Java/jre1.8.0_151/bin/server/jvm.dll",
         "-Djava.class.path=C:/Users/kubra/Desktop/ates/zemberek-tum-2.0.jar", "-ea")

'''jpype.startJVM("C:/Program Files/Java/jre1.8.0_151/bin/server/jvm.dll",
         "-Djava.class.path=C:/Users/Mehmet/PycharmProjects/classification/zemberek-tum-2.0.jar", "-ea")'''

dosya = open("haberler/spor haberleri/spor2.txt", "r")


tumkelimeler = dosya.readlines()

yenikelimeler = []


for kelimegruplari in tumkelimeler:

    kelimeler = kelimegruplari.lower().split()

    for kelime in kelimeler:
        yenikelimeler.append(kelime)

print(tumkelimeler)


# Türkiye Türkçesine göre çözümlemek için gerekli sınıfı hazırla
Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
# tr nesnesini oluştur
tr = Tr()
# Zemberek sınıfını yükle
Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")
# zemberek nesnesini oluştur
zemberek = Zemberek(tr)
#Çözümlenecek örnek kelimeleri belirle

for kelime in yenikelimeler:
    if kelime.strip()>'':
        yanit = zemberek.kelimeCozumle(kelime)
        if yanit:
            print("{}".format(yanit[0]))
        else:
            print("{} ÇÖZÜMLENEMEDİ".format(kelime))
#JVM kapat
jpype.shutdownJVM()

