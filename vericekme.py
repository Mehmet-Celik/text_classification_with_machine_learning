import requests

from bs4 import BeautifulSoup

class Vericekme:

    def __init__(self):

        self.url = ""
        self.sinif = ""


    def vericek(self, url):

        self.url = url

        r =requests.get(self.url)

        soup = BeautifulSoup(r.content, "html.parser")
        veriler = soup.find_all("p")

        return veriler