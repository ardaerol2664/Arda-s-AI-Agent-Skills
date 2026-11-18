# Bağımsız incelemenin teknik özeti

Bu belge, bağımsız inceleme kaydının teknik bölümlerinden düzenlenmiştir.

Tarih: 2026-11-18. İncelenen kapsam: `requirements.md`, `baseline/codex-security/` altındaki beş dosya ve `outputs/codex-security-revision/codex-security/` altındaki beş yeniden yazılmış dosya. Dosyalar değiştirilmedi; yalnız bu inceleme kaydı oluşturuldu.

## Sonuç

**Doğrulanmış bir davranış/karar regresyonu veya kaybolmuş gereksinim bulunmadı.** Bu sonuç kaynak karşılaştırmasına dayanır; bütün projelerde tespit etkinliğinin eşit olduğuna ilişkin bir onay değildir.

- Üç çalışma modu; salt okunur tarama; yerel, taze bağlamlı ve sınırlı alt ajanlar; araştırma genişliği; tam çalışma ağacı/index ayrımı; snapshot ve drift denetimi; kanıt ve sır koruma; patch için ayrı scratch çalışma alanı, iki bağımsız inceleme ve apply-check sınırları yeni talimatlarda korunuyor (`SKILL.md`, `references/workflow.md`).
- Karar hesabı kaynak düzeyinde eşdeğer: üç ayrı lens ve araştırmacılardan ayrık üç kimlik; üç oy tamamlanmadan karar yok; en az iki confirm ile kabul; bunun dışında en az iki reject/predates_change ile ret; önem derecesi araştırmacı ile ikinci en yüksek onay derecesinin minimumu; araştırma tamamlanmadan genel tamamlanma yok (`scripts/panel.py`: `_review_table`, `_outcome`, `tally`). Alanlar, çıktı sırası, `adapter` değeri, `tally` girdisi/çıktısı ve `--input`/`--output` CLI seçenekleri korunmuş. İç yardımcı işlev isimleri ve hata açıklamaları değişmiş; incelenen uyumluluk sözleşmesi bunları herkese açık arayüz olarak tanımlamıyor.
- CLI'da yinelenen JSON anahtarlarının reddi, aynı girdi/çıktının reddi ve çıktının yalnız yeni dosya olarak oluşturulması korunmuş (`unique_object`, `main`).

## Şüpheler ve sınırlar

Somut bir regresyon şüphesi saptanmadı.

Bu incelemede test çalıştırılmadı. Ana ajanın hazırladığı kapsamlı diferansiyel/CLI kontrolleri ve A/B deneyi tekrarlanmadı, sonuçları görülmedi; bu kayıt onların geçtiğini ileri sürmez. Gerçek çok ajanlı bir kullanıcı projesi taraması, patch üretimi ve performans ölçümü yapılmadı.

## Son dar değişiklik incelemesi — 2026-11-18

`panel.py` içindeki `_outcome` değişikliği ayrıca kaynak üzerinden incelendi. Onayların sayılması korunuyor; önem derecelerinin sıralanması artık yalnız üç oy ve en az iki onay olan dalda yapılıyor. Bu dalın dışındaki sonuçlar zaten `severity: null` olduğundan, `_review_table` doğrulamasından geçen girdiler için karar/önem/oy sayıları ve JSON alanları değişmiyor. Yeni bir bulgu yok. Testler tekrar çalıştırılmadı. Ana ajan son sürümde 4.100 geçerli eşdeğerlik/oracle, 44 bozuk girdi ve 7 CLI kontrolünün geçtiğini bildirdi; bu sayılar bu incelemede bağımsız olarak yeniden doğrulanmadı.
