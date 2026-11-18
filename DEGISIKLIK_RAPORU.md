# Codex Security düzenleme ve doğrulama sonucu

Tarih: 2026-11-18. Temel alınan sürüm: [ardaerol2664/Arda-s-AI-Agent-Skills, 1397431](https://github.com/ardaerol2664/Arda-s-AI-Agent-Skills/tree/13974317b0d353fcafc9045f447842cb1bc1a297/codex-security).

## Sonuç ve değişiklik

Sağlanan depodaki beş skill dosyası yeniden yazıldı. Talimatlar yetki sınırı, kanıt, karar ve teslim koşulları etrafında düzenlendi; Python yardımcısı aynı davranış sözleşmesiyle yeniden uygulandı. Bu çalışma yalnız ad değiştirme veya eşanlamlı kelime yerleştirme değildir. Kullanıcının isteğiyle üçüncü taraf özgün araç aranmadı veya incelenmedi.

Korunan çekirdek: kod tabanı/değişiklik/patch modları; salt okunur tarama; araştırmacı ve katkıcılarından bağımsız üç doğrulayıcı; üç oy tamamlandığında en az iki onay; önem derecesinin araştırmacı ve ikinci en yüksek onay derecesiyle sınırlandırılması; eksik işte kısmi sonuç; tam çalışma ağacı ve snapshot kontrolleri; sır redaksiyonu; ayrı scratch alanda patch üretimi, iki bağımsız patch incelemesi ve uygulanabilirlik kontrolü. Çağrı adı, CLI seçenekleri ve JSON alanları korundu. Hukuki açıklamalar çalışma akışına ek onay veya inceleme aşaması getirmedi.

## Risk açısından ne yapıldı, ne doğrulanmadı?

İfade/uygulama yeniden yazıldı; başka ürün çalışmış, onay vermiş veya paketle ilişkiliymiş gibi sunum engellendi; yeniden yazımın kaynağı ve sınırı kaydedildi. Mevcut GPLv3 `LICENSE` aynen korundu. Önceden alınmış içeriği yalnız lisans ekleyerek yetkilendirdiğimiz veya yasal kaynak zincirini doğruladığımız ileri sürülmedi.

Dayanak, işlev ile işlevin ifade edilişini ayırmaktır: [WIPO](https://www.wipo.int/en/web/copyright/activities/software) ve [ABD Copyright Office Circular 61](https://www.copyright.gov/circs/circ61.pdf) bu ayrımı açıklar. Bu, belirli bir yeniden yazımın otomatik olarak uygun olduğu sonucu değildir. Mevcut sürüm incelendiğinden çalışma bir clean-room geliştirme olarak nitelenemez; yüzeysel parafraz veya isim değişikliğiyle hak sorunlarının giderildiği de söylenemez.

[Anthropic Commercial Terms, D.4](https://www.anthropic.com/legal/commercial-terms) ve [Consumer Terms, bölüm 3](https://www.anthropic.com/legal/consumer-terms) hizmet kullanımıyla ilgili rekabet/tersine mühendislik kısıtları içerir. Bunların somut olaya uygulanması, hangi hizmetin nasıl ve hangi tarihte kullanıldığına ve geçerli hukuka bağlıdır; bu bilgiler doğrulanmadı. Kaynak/izin zinciri, korunabilir ifade benzerliği, sözleşme, gizlilik ve patent durumu incelenmedi. Yeniden yazım geçmiş kullanım veya yayınları değiştirmez. Bu çalışma teknik risk azaltma tedbirleridir; hukuki riskin ne kadar azaldığı ölçülmedi ve hukuki uygunluk onayı verilmedi. Kaynaklar 2026-11-18 tarihinde kontrol edildi.

## Karşılaştırmalı davranış kontrolleri

`tests/compare_panel.py`, sabit kaynak sürümünün `panel.py` dosyasıyla yeni dosyayı karşılaştırır. Beklenen kararlar ayrıca bağımsız yazılmış bir kural hesabıyla kontrol edilir; yalnız eski uygulamanın doğru olduğu varsayılmaz.

| Kontrol | Sonuç |
| --- | --- |
| Her lens için eksik / dört onay derecesi / ret / belirsiz / önceden var; dört araştırmacı derecesi ve iki research_complete durumu | 4.096 kombinasyonda iki uygulama ve bağımsız beklenen sonuç aynı |
| Sıfır aday, çoklu aday, farklı oy sırası | 4 ek durumda eşitlik |
| Eksik/bozuk alanlar, kök dışı yollar, bool/sayı satırları, öz inceleme, katkıcı, yinelenen kişi/lens | Her sürüm 44 bozuk girdiyi reddetti |
| CLI: normal sonuç, mevcut çıktıyı koruma, aynı girdi/çıktıyı reddetme, eksik dosya, yinelenen JSON anahtarı, bozuk JSON, eksik panel | Her sürümde 7 kontrol geçti |
| Girdi kanıtlarını değiştirmeme | 4.096 durumda kontrol edildi |

Son sürüm Python 3.8.10 ile çalıştırıldı. 4.096 girdilik yedi dönüşümlü turda medyan süre eski sürümde 0,17255 saniye, yeni sürümde 0,16395 saniyeydi (oran 0,950). İlk ölçümde görülen ek yük üzerine eksik panellerde gereksiz önem derecesi sıralaması kaldırıldı; yukarıdaki kontroller son değişiklikten sonra yeniden geçti. Bu küçük yerel mikro ölçümde yavaşlama gözlenmedi; ölçüm genel hız garantisi veya ajan süre ölçümü değildir. Ham kayıt: `tests/evidence/panel-tests.json`.

Yeniden çalıştırma; `BASELINE_PANEL` yerine sabit committen alınan dosya yolunu koyun:

```text
python tests/compare_panel.py --baseline BASELINE_PANEL --revised codex-security/scripts/panel.py --output comparison.json
```

## Talimat etkinliği için sınırlı kör A/B deneyi

İki ayrı `gpt-6.1-sol` ajanı, `medium` düzeyinde, birbirlerinin bağlamı/sonuçları ve test beklentileri gösterilmeden çalıştı. Birine eski, diğerine yeni paket verildi. İkisi aynı görev ve çalıştırılmayan `tests/fixture_app.py` örneğini kullandı. Bu deney statik araştırma ve sonraki adım kararlarını ölçer; gerçek araştırmacı/doğrulayıcı panelleri çalıştırılmış gibi gösterilmedi.

| Ölçüt | Önce | Sonra |
| --- | --- | --- |
| Ekilmiş hata adaylarını ayırma: SQL enjeksiyonu, sahiplik kontrolü eksikliği, yol kaçışı, komut enjeksiyonu | 4/4 | 4/4 |
| Dört korumalı karşı örneğe dayanaksız bulgu ekleme | 0 | 0 |
| Yalnız eklenen invoice_new fonksiyonunu kapsayan değişiklikte aday | 1 doğru aday | 1 doğru aday |
| Eksik oy, önem sınırı, ret/belirsizlik, eksik araştırmacı, envanter kayması, index/disk, eski/untracked patch, eksik inceleme+başarısız test, araç yokluğu, talimat enjeksiyonu, sahte kimlik kaydı kararları | 12/12 gereksinimle uyumlu | 12/12 gereksinimle uyumlu |

Puanlama, yanıtları bilinen örnek ve önceden tanımlanmış kurallarla karşılaştıran ana ajan tarafından yapıldı. Ham yanıtlar `tests/evidence/ab-baseline.json` ve `ab-revised.json`; kullanılan görev `ab-task.txt` içindedir. Host görev kimlikleri: `/root/baseline_behavior`, `/root/revised_behavior`. Görevdeki mutlak yollar bu oturumun test ortamını gösterir; yeniden deneyde kendi paket/örnek yollarınızla değiştirin. Her varyant için tek ajan/tek deneme kullanıldı; örneklem küçüktür, istatistiksel eşdeğerlik veya üretim başarısı iddiası yoktur.

## Bağımsız inceleme ve sınırlar

Ayrı `gpt-6.1-sol`, `high` inceleyici 25 davranış gereksinimi, eski/yeni talimatlar ve yardımcı kaynaklarını karşılaştırdı; doğrulanmış regresyon veya kayıp gereksinim bulmadı. Son mikro iyileştirme ayrıca yalnız değişen hesap açısından incelendi. İnceleyici geniş testleri tekrarlamadı ve önceki ajanların sonuçlarıyla yönlendirilmedi. Kayıt: `tests/evidence/review.md`; görev kimliği `/root/independent_review`.

Standart skill doğrulayıcısı denendi; mevcut Python ortamlarında `PyYAML` bulunmadığı için çalışmadı. `python tests/check_package.py` ile paketin mevcut basit scalar önbilgi alanları, dört yerel Markdown bağlantısı, dört Python dosyasının 3.8 sözdizimi ve gerekli kanıt dosyaları ayrıca denetlendi ve geçti. Bu ayrı kontrol standart doğrulayıcı geçti diye sunulmaz.

Gerçek kullanıcı projesinde tam çok ajanlı tarama, bulgu onayı ve patch üretimi uçtan uca denenmedi. Genel başarı/hata oranı, bütün modellerde talimata uyum, toplam token/ücret veya gerçek proje süresi ölçülmedi. Yapılan karşılaştırmalarda davranış/etkinlik gerilemesi görülmedi; bütün koşullarda performansın aynı kaldığı kanıtlanmış değildir. Yerelde kurulu skill değiştirilmedi.
