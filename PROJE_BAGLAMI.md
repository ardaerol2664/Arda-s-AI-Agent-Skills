# Güncel durum

2026-11-18: `codex-security` yeniden yazımı taslak PR #1 üzerinden inceleniyor. Kullanıcının talebiyle README, sonuç raporu ve PR açıklaması işlev ve doğrulama bilgilerine odaklandı. Çalışan talimatlar, Python yardımcısı ve karar kuralları bu belge düzenlemesinde değiştirilmedi. Sıradaki adım taslak değişikliği değerlendirmektir.

## Amaç ve kapsam

Depo yeniden kullanılabilir AI ajan skill'lerini kök klasörlerde paylaşır. Bu çalışma `codex-security/` ve ilgili doğrulama kayıtlarını kapsar; diğer skill'ler değiştirilmedi. Yerel teslim paketi yalnız ilgili dosyaları içerir. Kullanıcının temel ölçütü becerinin işlevlerini ve etkinliğini korumaktır; başka bir araçla birebir eşdeğerlik zorunlu değildir. README ve paylaşım belgeleri kullanım, işlev ve doğrulama bilgilerine odaklanmalıdır.

## Dosya haritası

- `codex-security/SKILL.md`: keşif, araçlar ve çalışma sınırları.
- `codex-security/references/workflow.md`: inceleme, snapshot, doğrulama ve patch süreci.
- `codex-security/references/contracts.md`: JSON arayüzü ve karar kuralları.
- `codex-security/scripts/panel.py`: Python 3.8+ ve standart kütüphaneyle çalışan karar yardımcısı.
- `codex-security/README.md`: kullanım ve özellikler.
- `DEGISIKLIK_RAPORU.md`: değişiklik ve doğrulama sonuçları.
- `tests/`: karşılaştırma araçları ve test kanıtları.

## Kararlar ve doğrulama

Karşılaştırma tabanı: `13974317b0d353fcafc9045f447842cb1bc1a297`. Üç ayrı doğrulayıcı, en az iki onay, önem derecesi üst sınırı, eksik işte kısmi durum, snapshot/redaksiyon ve iki bağımsız patch incelemesi korundu. Çağrı adı, helper CLI ve JSON arayüzü uyumludur.

2026-11-18 kontrollerinde bizim eski/yeni sürümlerimiz 4.100 geçerli durumda aynı sonucu verdi; her sürüm 44 bozuk girdiyi reddetti ve 7 CLI kontrolünü geçti. Sınırlı A/B denemesinde iki sürüm de aynı dört adayı ayırdı ve 12 karar senaryosunda gereksinimlerle uyumluydu. Ayrı incelemede doğrulanmış regresyon bulunmadı. Bunlar tüm projelerde başarı garantisi değildir; ayrıntı ve ham kanıtlar sonuç raporundadır.

Standart skill doğrulayıcısı PyYAML eksikliğiyle çalışmadı; ayrı paket/başvuru/sözdizimi kontrolleri geçti. Gerçek projede tam çok ajanlı tarama ve patch üretimi uçtan uca denenmedi. Belge değişikliği için geniş davranış testleri tekrar çalıştırılmamalı; ilgili içerik/bağlantı ve kodun değişmediği kontrolleri yeterlidir.

Skill kullanıcı veya proje skill dizinine kopyalanabilir; bu koleksiyon deposunun `.agents/skills/` dizinine kurulmaz. Yerelde kurulu skill değiştirilmedi. Mevcut LICENSE korundu. PR taslaktır ve birleştirilmedi; bu düzenleme önceki Git commitlerini değiştirmez.
