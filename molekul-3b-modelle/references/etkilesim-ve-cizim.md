# Etkileşim ve çizim

## Motor ve veri ayrımı

Önce erişilebilir, uygun bir önceki modelin motorunu kullan; sadece molekül verisi ve gerekli etiketleri değiştir. Motorun yeni elementleri, atom kimliklerini ve bağ mertebelerini gerçekten desteklediğini kontrol et. Şablon dosyası varsa okuyup baştan yazmak yerine kopyala ve parametreleştir. Motor eksikse yalnızca eksik kabiliyeti ekle; özel ray-tracing, aydınlatma veya geometri motorunu her seferinde yeniden geliştirme. Yeniden kullanılacak dosyanın varlığını ve sürümünü doğrula.

Sohbet görselleştirme altyapısının güncel sözleşmesini uygula. Küçük öğretici moleküllerde bağımlılıksız Canvas/SVG ve gerçek 3B koordinatların projeksiyonu yeterlidir. Büyük yapılarda izin verilen CDN'den sürümü sabitlenmiş Three.js veya uygun molekül görüntüleyici seç; resmi API'yi doğrula. İlk ekranda yüklenmeyen motor boş alan bırakmasın; görünür hata veya çalışan uygun yedek sun.

Değişmez kaynak atom-bağ grafiğini kamera dönüşü, zoom ve etiket tercihlerinden ayır. İki boyutlu resme CSS dönüşü uygulamayı 3B model diye adlandırma.

## Kamera

1. Molekülü merkezine ötele; mesafe oranlarını koruyup sınır yarıçapını hesapla.
2. Dönüşü quaternion veya ortonormal matrisle tut; pointer farklarını açıya dönüştür. Her karede kaynak koordinatları kullan; birikimli deformasyonu önle.
3. Öğretici karşılaştırmada ortografik projeksiyon uygundur. Perspektifte yakın düzlem ve örtüşmeyi yönet.
4. Kamera/ölçeği model sınırlarına ve gerçek kapsayıcı boyutuna göre hesapla. `ResizeObserver` kullan; Canvas çözünürlüğünü sınırlanmış `devicePixelRatio` ile eşleştir.
5. Üstten/yandan görünümü öğretici düzleme göre tanımla. Benzende yandan bütün atomların düzlemselliği görülsün; siklohekzanda sandalye kıvrımı korunsun.

## Atomlar ve bağlar

WebGL'de derinlik tamponu ve küre/silindir kullan. Canvas/SVG'de gerekiyorsa çubukları parçalara bölüp atomlarla birlikte derinliğe göre sırala. Bütün bağları ardından bütün atomları çizmenin karmaşık örtüşmelerde yanlış olduğunu dikkate al; basit motor yetersizse WebGL'ye geç.

Çoklu bağ için bağ yönüne en az paralel yardımcı ekseni seç, çapraz çarpımla dik ofset oluştur. Sıfıra yakın vektörde yedek eksen kullan. Ofsetleri model koordinatlarında üret ve modelle döndür; ekran-yatay süs çizgilerini kullanma. Küreler bağı tamamen gizlemesin. Küre/çubuk kalınlığını fiziksel atom/bağ yarıçapı ölçümü gibi sunma.

Aromatik çemberi halka düzleminde oluşturup aynı dönüşe tabi tut. Çemberin matematiksel simge olduğunu; gerçek π elektron yoğunluğunun uzaysal dağılımı olmadığını gerektiğinde açıkla.

## Etkileşim

- `pointerdown/move/up/cancel` ve sürüklemede `setPointerCapture` kullan; bitişte durumu temizle.
- Dokunma davranışını yalnızca model alanında sınırla. Sayfanın tamamında kaydırmayı engelleme. `touch-action` seçimini gereken hareketlere göre yap.
- Zoom'u pozitif alt/üst sınırda tut; modeli kaybetme. Tekerleği yalnızca model üzerinde/odakta işle. Tekerleksiz kullanıcı için erişilebilir zoom kontrolü sun.
- Pinch eklenirse etkin pointer haritasında mesafe oranını kullan; bir parmağa dönüşte başlangıç değerlerini sıfırla. Test edilmemiş pinch'i destekleniyor diye anlatma.
- Görünür yerel düğme/alanları Türkçe etiketle. Gerekirse yön düğmeleriyle sürüklemeye klavye alternatifi sağla.
- `requestAnimationFrame` ile ihtiyaç halinde çiz. Varsayılan sürekli dönüş ve gereksiz döngü ekleme; azaltılmış hareket tercihine uy.
- H gizleme grafiği değiştirmesin; ilgili çubukları da gizle. Etiketleri okunaklı konumlandır; çakışmada isteğe bağlı etiketleri azalt.

## Düzen ve test

Tema kurallarına uy; elementleri sembolle de ayırt et. H'nin zeminde kaybolmasını önle. Model alanını baskın tut; istenmeyen sahte değer panelleri ekleme. Açıklamayı normal yanıta taşı.

1. Denetleyiciyi çalıştır; kaynakla formül/yük/stereo karşılaştır. Düzlemselliği sayısal, tetrahedral ve doğrusal açıları vektörlerle kontrol et.
2. İlk karede atomlar/bağlar görünür ve alan içinde olsun; konsolu incele.
3. Sürükleme sonrası en az bir projeksiyon değişsin, kaynak atomlar arası mesafeler sabit kalsın. Zoom ölçeği değiştirsin; başlangıç görünümü aynı duruma dönsün.
4. Tek parmak akışını ve varsa pinch'i emüle et. Parmak kalkınca kendi kendine dönmesin.
5. 320 px, tablet yatay ve geniş görünümde taşma/çakışmayı denetle. Açık/koyu temada okunabilirliği kontrol et.
6. Benzen yandan düzlemsel, siklohekzan kıvrımlı olsun. Stereomerleri döndürmek ayna dönüşümü yapmasın.

Tarayıcı olanağı varsa gerçek etkileşim veya otomasyon kullan. İncelenmemiş ekran görüntüsüne dayanarak görsel kontrol yapılmış gibi raporlama.
