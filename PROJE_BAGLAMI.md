# Güncel durum

2026-11-18: `codex-security` için işlevleri koruyan yeniden yazım hazırlandı. Karar yardımcısının 4.100 geçerli girdide eski sürümle çıktıları aynı; 44 bozuk girdi ve her sürümde 7 CLI kontrolü geçti. Sınırlı kör A/B denemesinde iki sürüm de dört hata adayını ayırdı ve 12 karar senaryosunda gereksinimleri korudu. Kaynak incelemesinde kayıp gereksinim bulunmadı. Bu sonuçlar üretim başarısı veya hukuki uygunluk garantisi değildir. Değişiklik seti `codex-security/rewrite-2026-11-18` dalında taslak PR üzerinden incelenmek içindir; main'e birleştirme yapılmadı. Sıradaki adım somut farkı ve test sınırlarını değerlendirmektir.

## Amaç ve kapsam

Asıl depo, yeniden kullanılabilir AI ajan skill'lerini kök klasörlerde paylaşır: `ardaerol2664/Arda-s-AI-Agent-Skills`. Bu çalışma yalnız `codex-security/` ve ilgili bağlam/doğrulama kayıtlarını kapsar. `ders-konu-anlatimi/` ve `molekul-3b-modelle/` değiştirilmedi; bu yerel teslim paketine kopyalanmadı. Asıl deponun mevcut GPLv3 `LICENSE` dosyası aynen korundu.

Kullanıcının temel kabul ölçütü güvenlik incelemesi/bağımsız doğrulama/patch işlevlerini ve etkinliği anlamlı ölçüde azaltmadan hukuki riski azaltacak düzenlemeler yapmaktır. Kullanıcı özgün üçüncü taraf aracın incelenmesini istemedi; yalnız sağladığı depodaki sürüm esas alındı.

## Dosya haritası

- `codex-security/SKILL.md`: keşif, yerel araçlar, yetki ve kanıt sınırları.
- `codex-security/references/workflow.md`: araştırma, snapshot, doğrulama ve patch adımları.
- `codex-security/references/contracts.md`: aynı kalan JSON arayüzü ve karar kuralları.
- `codex-security/scripts/panel.py`: yeniden uygulanan standart kütüphane yardımcısı; Python 3.8+.
- `codex-security/README.md`: kullanım ve kaynak/paylaşım sınırları.
- `DEGISIKLIK_RAPORU.md`: tek sonuç kaydı; kaynaklar, değişiklikler, doğrulama ve sınırlar.
- `tests/`: karşılaştırma aracı ve sınırlı davranış deneyinin kanıtları.

## Kararlar ve güvenle devam etme

Temel alınan commit: `13974317b0d353fcafc9045f447842cb1bc1a297`. Üç ayrı doğrulayıcı, en az iki onay, önem derecesi üst sınırı, eksik işte kısmi durum, snapshot/redaksiyon şartları ve iki bağımsız patch incelemesi korunmuştur. Skill çağrısı, helper CLI ve JSON alanları uyumludur. Çalışma talimatları ve yardımcı uygulaması yeniden yazıldı; runtime akışına hukuki kontrol veya ek onay eklenmedi.

Önceki sürüm görüldüğünden clean-room iddiası yoktur. Özgün kaynakla benzerlik, önceki materyalin izin zinciri, uygulanacak hukuk, sözleşme ve patent durumu doğrulanmadı. Yalnız parafrazın veya depodaki GPLv3 metninin bu konuları çözdüğü ileri sürülmemelidir. Önceki sürümün 16 kontrolü tarihsel kayıttır; yeni sürümün kanıtları rapordaki ayrı kontrollerdir.

Skill'ler bu deponun `.agents/skills/` konumuna kurulmaz; kullanıcı kendi kullanıcı/proje skill dizinine kopyalar. Yerelde kurulu `codex-security` bu çalışmada değiştirilmedi. Tam çok ajanlı gerçek proje taraması ve patch üretimi yeni sürümle uçtan uca çalıştırılmadı. Gereksiz yeniden test yerine yalnız yeni değişikliklerin etkilediği kontrolleri çalıştırın.
