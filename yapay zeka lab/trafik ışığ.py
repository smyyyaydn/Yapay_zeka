from random import choice
from experta import *
#ışık sınıfının oluşşturulması 
class Işık(Fact):
   pass
#kurallların belirlenmesi
class KarşıdanKarşıyaGeçme(knowledgeEngine):
    @Rule(Işık(renk="yeşil"))
    def yeşil_ışık(self):
        print("yeşil ışık yandığı için karşıdan karşıya geçebilirsiniz")
    @Rule(Işık(renk="kırmızı"))
    def kırmızı_ışık(self):
        print("kırmızı ışık yandığı için karşıdan karşıya geçemezsiniz.lütfen yeşil ışığın yanmasını bekleyiniz")
    @Rule(Işık(renk="sarı"))
    def sarı_ışık(self):
        print("sarı ışık yanıyor .lütfen dikkatli olunuz")

#kuralların çalıştırılması ve test ediilmesi
uzman=KarşıdanKarşıyaGeçme()
uzman.reset()
uzman.declare(Işık(renk=choice(["yeşil","sarı","kırmızı"])))
uzman.run()
