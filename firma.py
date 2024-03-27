from personel import Personel

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel_nesnesi):
        self.personel_listesi.append(personel_nesnesi)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(f"Adı: {personel.adı}, Departmanı: {personel.departmanı}, Çalışma Yılı: {personel.çalışma_yılı}, Maaşı: {personel.maaşı}")

    def maaş_zammı(self, personel_nesnesi, zam_oranı):
        personel_nesnesi.maaşı *= (1 + zam_oranı / 100)

    def personel_çıkart(self, personel_nesnesi):
        self.personel_listesi.remove(personel_nesnesi)
