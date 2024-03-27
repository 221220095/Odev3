from personel import Personel
from firma import Firma

# Personel nesneleri oluşturma
personel1 = Personel("Ahmet", "Satış", 3, 5000)
personel2 = Personel("Ayşe", "Muhasebe", 5, 6000)

# Firma nesnesi oluşturma
firma = Firma()

# Personelleri ekleme
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

# Personel listesini görüntüleme
print("----- Personel Listesi -----")
firma.personel_listele()

# Maaş zammı uygulama
firma.maaş_zammı(personel1, 10)
print(f"{personel1.adı}'nın yeni maaşı: {personel1.maaşı}")

# Personel çıkarma
firma.personel_çıkart(personel2)

# Güncellenmiş personel listesini görüntüleme
print("----- Güncellenmiş Personel Listesi -----")
firma.personel_listele()
