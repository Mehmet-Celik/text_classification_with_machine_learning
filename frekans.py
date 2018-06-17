class Frekans:

    def __init__(self):

        self.kelimesayisi = {}

    def hesapla(self, words):

        for kelime in words:

            if kelime in self.kelimesayisi:

                self.kelimesayisi[kelime] += 1

            else:

                self.kelimesayisi[kelime] = 1

        return self.kelimesayisi

    def temizle(self):

        self.kelimesayisi = {}