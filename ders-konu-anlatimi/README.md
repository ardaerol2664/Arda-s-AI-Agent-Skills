# Ders Konu Anlatımı

Bir ders konusunu, seviyeye ve kapsama uygun **görselli PDF ders notu** hâline getiren beceri.

## Ne işe yarar?

- Konunun ilgili güncel müfredatını ve kapsamını araştırır. Türkiye lise konularında MEB öğretim programları, ders kitapları ve OGM materyallerini önceliklendirir; kullanıcının kaynak kısıtlarını gözetir.
- Kavramları temelden başlayarak adım adım açıklar; gerekli ön bilgileri, çözümlü örnekleri ve uygun alıştırmaları ekler.
- Konuya uygun şema, etiketli çizim, grafik veya tablolarla anlatımı destekler.
- İddiaları, çözümleri ve görselleri kaynaklarla karşılaştırır; PDF'in okunabilirliğini ve sayfa düzenini kontrol eder.
- Kaynak atıflarını PDF içinde sunar; doğrulanamayan noktaları açıkça belirtir.

Varsayılan çıktı dikey sayfa düzeninde PDF'tir. İstenirse yatay hazırlanır. Kullanıcı ayrıca istemedikçe tüm anlatımı önce sohbete dökmek veya ara sürümleri göndermek yerine son, düzeltilmiş PDF sunulur.

## Ne zaman kullanılır?

Açıkça bir ders konusu anlatımı, eğitim veya kapsamlı ders notu istendiğinde kullanılır. Tek bir sorunun cevabı ya da kısa bir açıklama için tasarlanmamıştır.

## Kullanım örnekleri

> ders-konu-anlatimi becerisini kullanarak 10. sınıf kimyada mol kavramını temelden anlatan, çözümlü örnekleri olan görselli bir PDF hazırla.

> 11. sınıf fizikte elektrik alan konusunu anlat. Yatay PDF düzeni kullan; alan çizgilerini açıklayıcı çizimlerle göster.

> Bu konu için yalnızca paylaştığım ders kitabını kaynak alarak görselli PDF ders notu hazırla.

İstemde ders ve sınıf/seviyeyi, konu sınırını, varsa kaynak kısıtını ve sayfa yönünü belirtmek çıktıyı netleştirir. Sınıf belirtilmezse beceri bağlamdan çıkarır; belirsizse varsayımını açıklar.

## Kurulum ve gereksinimler

Klasörü destek dosyalarıyla birlikte skill destekleyen aracın kullanıcı dizinine veya projede `.agents/skills/ders-konu-anlatimi/` altına kopyalayın. Codex'te `$ders-konu-anlatimi` adıyla ya da beceri adını mesajda belirterek çağırabilirsiniz.

Çalıştığı ortamın gerekli kaynaklara erişebilmesi, PDF oluşturabilmesi ve son PDF'i görüntüleyerek kontrol edebilmesi gerekir. Bu klasör tek başına bir PDF dönüştürme programı içermez; ilgili araçları yönlendiren talimatları barındırır.

## Dosyalar

- [SKILL.md](SKILL.md): Esas iş akışı ve çıktı kuralları.
- [agents/openai.yaml](agents/openai.yaml): Arayüzde gösterilen beceri bilgileri.
- [assets/icon.svg](assets/icon.svg): Beceri simgesi.

Bilimsel çizimlerde idealizasyon, temsil ve ölçek sınırları belirtilir; beceri kullanılması içeriğin otomatik olarak hatasız olduğunu garanti etmez.

Depo lisansı: [LICENSE](../LICENSE).
