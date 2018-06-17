
import sqlite3

class Veritabani:

    def __init__(self):

        self.dizi = []

    def baglan(self, words):

        baglanti = sqlite3.connect("classification.db")
        con = baglanti.cursor()

        for veri in words:
            dbeleman = con.execute("SELECT frekans FROM TEKNOLOJI WHERE kelime=?", (veri,))
            entry = con.fetchone()

            if entry is None:
                con.execute("""INSERT INTO TEKNOLOJI (kelime,frekans) VALUES(?,?)""", (veri, words[veri]))
            else:
                con.execute("""UPDATE TEKNOLOJI SET frekans=? WHERE kelime =? """, ((entry[0]+int(words[veri])), veri))

        baglanti.commit()







