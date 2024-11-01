class kitap:

    def __init__(self,kitap_adı,yazar,yayım_yılı):

        self.kitap_adı = kitap_adı
        self.yazar = yazar
        self.yayım_yılı = yayım_yılı

    def __str__(self):
        return "{} - {} ({})".format(self.kitap_adı, self.yazar, self.yayım_yılı)

class kitap_katalogu:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self,kitap):
        self.kitaplar.append(kitap)

    def kitap_listele(self):
        for kitap in self.kitaplar:
            print(kitap)

kitap1 = kitap("Nutuk", "Mustafa Kemal Atatürk", 1927)
kitap2 = kitap("Kaşağı", "Ömer Seyfettin", 1911)
kitap3 = kitap("Mor Salkımlı Ev", "Halide Edip Adıvar", 1935)

katalog = kitap_katalogu()

katalog.kitap_ekle(kitap1)
katalog.kitap_ekle(kitap2)
katalog.kitap_ekle(kitap3)

print("Kitap Kataloğu:")
katalog.kitap_listele()
