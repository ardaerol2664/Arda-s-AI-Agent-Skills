# Codex Security

Codex yerel alt ajan araçlarıyla kod tabanını veya Git değişikliklerini güvenlik açısından inceleyen skill. Kullanıcı istediğinde ayrı bir çalışma kopyasında incelenmiş patch dosyaları önermek için de talimatlar içerir.

## Kullanım

`codex-security` klasörünü kullanıcı genelindeki skill dizinine veya projede `.agents/skills/codex-security/` altına kopyalayın. Skill'i `@codex-security` adıyla çağırın; native alt ajan araçları ve Python 3.8+ gerekir. Python yardımcısı üçüncü taraf paket gerektirmez.

Örnek: `codex-security skill'ini kullanarak bu projenin backend klasörünü güvenlik açısından tara.`

## Yapı ve sınırlar

- `SKILL.md`: keşif açıklaması, araçlar ve temel sınırlar.
- `references/workflow.md`: tarama, bağımsız doğrulama ve patch önerisi akışı.
- `references/contracts.md`: araştırmacı/doğrulayıcı veri sözleşmeleri.
- `scripts/panel.py`: oyları ve önem düzeyi sınırını deterministik hesaplayan yardımcı.

Bu, tek komutla bağımsız çalışan bir güvenlik tarama motoru değildir: iş akışını ana ajan yürütür. Üç farklı doğrulayıcı tamamlanmadan bulgu onaylanmaz; en az iki onay gerekir. Script gerçek ajan kimliğini veya kanıtın doğruluğunu doğrulamaz; gerçek araç dönüşleri ve kaynak incelemesi gereklidir. Eksik araştırma veya doğrulama açıkça kısmi sonuç olarak raporlanır. Patch'ler otomatik uygulanmaz.

## Doğrulama

2026-11-18: Yerel geliştirmede panel için 16 hedefli algoritma/CLI kontrolü ve bağımsız inceleme yapıldı; skill biçim doğrulaması geçti. Gerçek kullanıcı projesinde uçtan uca tarama veya patch üretimi henüz doğrulanmadı. Bu kontroller güvenlik doğruluğu garantisi değildir.
