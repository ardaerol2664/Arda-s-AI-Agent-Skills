---
name: molekul-3b-modelle
description: Sohbet içinde fare/dokunmayla döndürülebilen, yakınlaştırılabilen 3B molekül modelleri ve geometri/stereomer karşılaştırmaları oluştur. Yapıdan emin değilsen önce güvenilir web kaynaklarıyla doğrula. Basit adlandırma sorularında veya ayrıca istenmedikçe PDF/statik resim için kullanma.
---

# Etkileşimli 3B molekül modelleme

## Kaynakları ihtiyaç kadar yükle

Önce bu kısa akışı uygula. Ayrıntıları yalnızca ilgili durumda aç; aynı sürüm aynı bağlamda okunmuşsa tekrar yükleme. Başka bir becerinin zorunlu tam okuma kuralına uy.

| Durum | Açılacak kaynak |
| --- | --- |
| Kimlik, stereo, kaynak veya koordinat yöntemi belirsiz | [Kimya rehberi](references/kimya-ve-koordinatlar.md): ilgili bölüm |
| Yeni model JSON'u hazırlanıyor | Kimya rehberindeki “Denetleyici veri şeması” |
| Çizim motoru ilk kez kuruluyor veya değişiyor | [Çizim rehberi](references/etkilesim-ve-cizim.md) |
| Yalnızca kamera, etiket veya görünüm değişiyor | Mevcut dosyanın değişecek bölümü; veri ve motoru koru |

## Ekonomik çalışma kuralları

- Oturumda erişilebilir doğrulanmış modeli, kaynak kaydını ve uygun çizim kodunu yeniden kullan; aynı motoru her molekül için baştan yazma. Kimlik/yöntem/sürüm uyumunu, atom indislerini, elementleri ve bağ mertebelerini kontrol et. Önceki çalışmanın varlığını doğrulamadan hatırlandığını veya önbelleklendiğini varsayma.
- Yalnızca istenen değişikliği yap. Kamera/renk değişiminde yapıyı yeniden araştırma veya konformer üretme; kimlik, yük, stereo ya da geometri değişiyorsa ilgili veriyi yeniden doğrula.
- Önce hedefli bir arama veya doğrudan doğru bileşik kaydını kullan. Güvenilir kaynak kimliği ve gereken özelliği doğruladığında dur; ikinci kaynağı belirsizlik/çelişki için aç. Bu kural zorunlu araştırmayı azaltmasın.
- Araçlara veriyi dosya olarak ilet. HTML, büyük JSON, SDF veya kodu sırf incelemek için bütünüyle araç çıktısına tekrar bastırma; özet, ilgili satırlar ve hata mesajlarını al. Bağımsız okuma/aramaları tek çağrıda grupla.
- Basit öğretici model için uygun tek konformerle başla. Çoklu konformer taraması, optimizasyon, ek kontrol ve özellikleri bilimsel ihtiyaç veya kullanıcı isteği gerektirirse ekle.
- Aynı hatalı araç/ağ/tarayıcı denemesini koşul değişmeden yineleme. İlk hatayı teşhis et, gerekçeli bir düzeltmeyi dene; aynı engel sürerse uygun yedeğe geç ve test sınırını belirt.
- Kontroller geçtiğinde bitir; yalnızca yeni değişiklik, hata veya belirsizlik ilgili kontrolün tekrarını gerektirsin. Rutin üretimde ek ajan/ikinci tam inceleme başlatma; karmaşık stereo veya çözülmemiş hata varsa değerlendir.
- Son yanıtta modeli ve gerekli birkaç açıklama cümlesini sun. Kod/veri dökümü, uzun işlem günlüğü veya istenmeyen PDF/ZIP/site üretme. Tasarrufu sabit token sayısı/yüzdesiyle garanti etme.

## 1. Kimliği ve yapıyı doğrula

Ad, formül, bağ grafiği, net yük ve stereokimyayı belirle. Kapalı formülü tek izomere eşitleme; okunamayan kritik bağı tahmin etme. Açık kimlikte gereksiz soru sorma.

**Yapı, H sayısı, yük, bağ, stereo, halka geometrisi veya bileşiğin varlığından emin değilsen modellemeden önce internette araştır. Kullanıcı bir bilgiye karşı çıkarsa önce araştır.** PubChem/ChEBI/NIST veya uygun birincil/üniversite kaynağında kimliği eşleştir; URL ve doğrulanan bilgiyi kaydet. MEB kapsamı istenirse terminolojisini de doğrula. Kritik belirsizlikte açıklama iste; erişilemeyen kaynağı okunmuş gibi sunma.

## 2. Koordinatları hazırla

Kaynak kimlikle eşleşen 3B veriyi kullan; yoksa doğrulanmış yapıdan uygun kimya aracıyla üret. Metan/etin/benzen gibi iyi bilinen basit yapılarda doğrulanmış ideal koordinatlar uygundur; “idealize” olarak belirt. Karmaşık halka/stereomerleri göz kararı kurma. Metal, radikal ve alışılmadık bağlanmada uygun uzman yöntem seç.

H dahil sabit atom kimliği, element, formal yük ve Å cinsinden x/y/z; bağ uçları ve mertebeleri tut. Stereo/aromatiklik bilgisini koru. Kaynak veriyi kamera dönüşünden ayır; yansıtma enantiyomeri değiştirmesin. Hesaplanan konformeri deneysel ölçüm veya tek olası şekil; örneklenen minimumu küresel minimum diye sunma.

## 3. Etkileşimli modeli çiz

Sohbet görselleştirmesi için güncel `visualize` talimatlarını oku ve uygula. Kesin atom-bağ yapısını sayısal koordinatlardan çiz; üretken resim aracı kullanma.

Küre/çubuk, doğru derinlik/örtüşme ve çoklu bağ düzeni kullan. Fare/tek parmakla döndürme ve erişilebilir sınırlı zoom sağla. Öğretici ise üstten/yandan/başlangıç görünümü ekle; gereksiz özellik ekleme. İlk kare dolu, etiketler okunaklı ve renk dışında sembolle de anlaşılır olsun. 320 px ve tablet yönlerinde düzen sığsın. Karşılaştırmada ölçek/renk tutarlı; dar ekranda modeller alt alta olsun. Aromatik çemberi elektron düzeninin şematik simgesi olarak açıkla.

## 4. Doğrula ve teslim et

`python <skill-directory>/scripts/validate_model.py <model.json>` ile temel sayım/yük/bağ/koordinat kontrolünü çalıştır; betiğin R/S, E/Z, aromatiklik veya kimlik doğrulamadığını unutma. Kaynakla kimlik/stereo ve modele özgü geometriyi ayrıca karşılaştır: metan tetrahedral, etin doğrusal, benzen düzlemsel/eşdeğer C–C; siklohekzan uygun sandalye geometrisinde olsun. π bağını serbest döndürme.

Yeni/değişmiş motor için sözdizimi, ilk kare, sürükleme, zoom/görünüm kontrolleri, dokunma ve dar/geniş düzeni test et. Aynı motorla yalnız veri değiştiyse yeni molekülün geometri, sığma ve temel etkileşimine odaklan; değişmeyen özellikleri baştan kapsamlı test etme. Kullanılabilir tarayıcıyı dene; ekran görüntüsünü etkileşim kanıtı sayma. Test edilmeyeni test edilmiş gibi raporlama.

Modeli sohbet içinde sun; gerekli görünüm açıklaması, kaynak atfı ve idealizasyon/konformer sınırlamasını kısa belirt.
