# Molekül 3B Modelle

Sohbet içinde fare veya dokunmayla döndürülebilen, yakınlaştırılabilen **etkileşimli 3B molekül modelleri** hazırlayan beceri. Molekül geometrilerini ve stereomerleri karşılaştırmak için de kullanılabilir.

## Ne işe yarar?

- Molekülün kimliğini, bağ yapısını, hidrojen sayısını, yükünü ve stereokimyasını belirler; belirsizlik varsa güvenilir kaynaklarla araştırır.
- Kimlikle eşleşen 3B veriyi kullanır veya doğrulanmış yapıdan uygun kimya aracıyla koordinat üretir. Basit yapılarda idealize koordinatlar kullanıldığını açıkça belirtir.
- Atom ve bağları sayısal koordinatlardan küre/çubuk modeliyle çizer; kimyasal yapıyı üretken resim aracına çizdirmez.
- Türkçe görünüm, döndürme ve yakınlaştırma düğmeleri sağlar; fare ve dokunma etkileşimini destekler.
- Aynı doğrulanmış modelin yalnız görünümü değiştiriliyorsa veriyi ve çizim motorunu yeniden kullanır.

Çıktı, sohbet içinde etkileşimli model ve gerekli kısa açıklamalardır. Ayrıca istenmedikçe PDF, statik resim, ZIP veya yayımlanmış site üretmez.

## Kullanım örnekleri

> molekul-3b-modelle becerisini kullanarak metanın 3B modelini göster.

> Etin ve eteni yan yana modelle; molekül geometrilerini karşılaştır.

> cis-2-büten ve trans-2-bütenin modellerini oluştur; farklarını kısa açıkla.

> Mevcut molekülün yalnızca kamera açısını ve atom etiketlerini değiştir; yapısını koru.

Molekülün adını veya açık yapısını, varsa yükünü ve stereomerini belirtin. Kapalı formül tek bir izomeri belirlemiyorsa yapı varsayılmaz; kritik belirsizlik açıklığa kavuşturulur. Basit adlandırma soruları için bu beceriye gerek yoktur.

## Model kontrolleri

Her modelde üstte **Başlangıç, Üstten, Yandan**; altta **Sola, Sağa, Yukarı, Aşağı, Büyüt (+), Küçült (−)** düğmeleri bulunur. Sürükleme ve dokunma bu düğmelerin yerine geçmez. Modelin kullanıcıya bakan yüzü sürükleme yönünü tutarlı izlemelidir; mobil ve tablet düzeni de kontrol edilir.

## Kurulum ve gereksinimler

Klasörü tüm destek dosyalarıyla birlikte skill destekleyen aracın kullanıcı dizinine veya projede `.agents/skills/molekul-3b-modelle/` altına kopyalayın. Codex'te `$molekul-3b-modelle` adıyla ya da beceri adını mesajda belirterek çağırabilirsiniz.

Beceri, sohbet görselleştirmesi için `visualize` talimatlarının ve uygun etkileşimli görüntüleme araçlarının bulunduğu bir ortam gerektirir. Yapı doğrulaması gerektiğinde web erişimi; temel model denetleyicisi için Python 3 gerekir. İsteğe bağlı düzlemsellik kontrolü NumPy kullanır. Kullanılacak koordinat üretim aracını molekülün ihtiyacı belirler.

## Dosyalar ve doğrulama

- [SKILL.md](SKILL.md): Esas iş akışı, etkileşim ve teslim kuralları.
- [Kimya ve koordinatlar](references/kimya-ve-koordinatlar.md): Kimlik, stereokimya, koordinatlar ve model JSON şeması.
- [Etkileşim ve çizim](references/etkilesim-ve-cizim.md): Çizim motoru, kontroller ve etkileşim doğrulaması.
- [validate_model.py](scripts/validate_model.py): Temel atom/bağ, yük ve koordinat kontrolleri.
- [agents/openai.yaml](agents/openai.yaml): Arayüzde gösterilen beceri bilgileri.
- [assets/icon.svg](assets/icon.svg): Beceri simgesi.

Hazırlanmış model JSON'unu kontrol etmek için, yer tutucuları gerçek yollarla değiştirin:

```text
python <skill-directory>/scripts/validate_model.py <model.json>
```

JSON biçimi kimya rehberindeki **Denetleyici veri şeması** bölümünde açıklanır. Betik R/S, E/Z, aromatiklik veya molekül kimliğini doğrulamaz; bu kontroller ayrıca kaynak ve geometri incelemesi gerektirir. Hesaplanmış bir konformer deneysel ölçüm ya da molekülün tek olası şekli olarak sunulmaz.

Depo lisansı: [LICENSE](../LICENSE).
