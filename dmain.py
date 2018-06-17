
import zemberekj
import dosya
import frekans
import veritabani

kelimelerial = dosya.Dosya()

yenikelimeler = kelimelerial.dosyaac()

baglan = zemberekj.Baglan()

diziler = baglan.zemberekbaglan(yenikelimeler)

frekans = frekans.Frekans()

kssozluk = frekans.hesapla(diziler[0])

frekans.temizle()

print(kssozluk)

"""ksfiil = frekans.hesapla(diziler[1])

frekans.temizle()

ksedat = frekans.hesapla(diziler[2])

frekans.temizle()

kszaman = frekans.hesapla(diziler[3])

frekans.temizle()

kszamir = frekans.hesapla(diziler[4])

frekans.temizle()

kssayi = frekans.hesapla(diziler[5])

frekans.temizle()

ksbaglac = frekans.hesapla(diziler[6])

frekans.temizle()

ksbilinmeyenkelimeler = frekans.hesapla(diziler[7])

frekans.temizle()

ksyenitip = frekans.hesapla(diziler[8])

frekans.temizle()

sqlite = veritabani.Veritabani()

sqlite.baglan(kssozluk)
"""





















