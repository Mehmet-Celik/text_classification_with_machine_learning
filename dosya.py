class Dosya:

    def __init__(self):

        self.tumkelimeler = []
        self.yenikelimeler = []
        self.kelimeler = []

    def dosyaac(self, yol):


        dosya = open(yol, "r")

        self.tumkelimeler = dosya.readlines()

        for kelimegruplari in self.tumkelimeler:

            kelimeler = kelimegruplari.split()

            for kelime in kelimeler:

                self.yenikelimeler.append(kelime)

        return self.yenikelimeler