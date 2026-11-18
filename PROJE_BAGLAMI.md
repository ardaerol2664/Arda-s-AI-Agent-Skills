# Güncel durum

2026-11-18: `ders-konu-anlatimi` ve `molekul-3b-modelle` için Türkçe README dosyaları eklendi. Amaç, kullanım örnekleri, gereksinimler, dosya haritası ve doğrulama sınırları mevcut SKILL.md içeriklerine göre açıklandı. Beceri talimatları ve uygulama kodları değiştirilmedi.

## Amaç ve dosya haritası

Bu depo yeniden kullanılabilir AI ajan skill'lerini bir arada tutar. Her skill kendi kök klasöründe, `SKILL.md` giriş dosyasıyla bulunur.

- `ders-konu-anlatimi/`: görselli PDF ders notu hazırlama. Kullanım ve gereksinimler: [README](ders-konu-anlatimi/README.md).
- `molekul-3b-modelle/`: etkileşimli 3B molekül modelleri. Kullanım, gereksinimler ve denetleyici sınırları: [README](molekul-3b-modelle/README.md).
- `codex-security/`: Codex yerel alt ajan araçlarıyla güvenlik incelemesi ve patch önerisi akışı. Kullanım, sınırlar ve doğrulama bilgileri `codex-security/README.md` içindedir.
- `codex-playground/`: Kontroller, canlı önizleme ve kopyalanabilir istem içeren tek dosyalı HTML deneme ekranları oluşturur. Kaynak, lisans ve kullanım: kendi README.md dosyasında.
- `codex-pr-review-toolkit/`: Kod/PR değişikliklerini hata, test kapsamı, hata yönetimi, yorum doğruluğu, tip tasarımı ve sadeleştirme açısından inceler. Kaynak, lisans ve kullanım: kendi README.md dosyasında.
- `codex-code-simplifier/`: İstenen kodu davranış ve sözleşmeleri koruyarak daha anlaşılır hâle getirir. Kaynak, lisans ve kullanım: kendi README.md dosyasında.
- `codex-feature-dev/`: Yeni özellikleri keşif, gereksinim, tasarım, uygulama ve inceleme aşamalarıyla geliştirir. Kaynak, lisans ve kullanım: kendi README.md dosyasında.
- `codex-claude-md-management/`: Mevcut proje talimatları ve bağlam dosyalarını denetler; PROJE_BAGLAMI.md ve AGENTS.md görevlerini ayırır. Kaynak, lisans ve kullanım: kendi README.md dosyasında.
- `LICENSE`: mevcut depo kök lisansı; değiştirilmedi. Yeni beş becerinin kendi LICENSE dosyalarında Apache 2.0 metni korunur.

## Kararlar ve doğrulama

Skill'ler depoda kök klasörler olarak paylaşılır; bu deponun `.agents/skills/` dizinine kurulmazlar. Kullanıcı bunları kendi kullanıcı veya proje skill dizinine kopyalayabilir. Kullanıcı `codex-security` açıklamasının yalnız işlev ve kullanıma odaklanmasını istedi. Yeni beş uyarlamada ise kaynak eklentinin Anthropic'ten alındığı açıkça belirtilmesini istedi; bu referans notları codex-security'ye eklenmedi.

Yeni skill'in panel yardımcısı için yerelde 16 hedefli kontrol ve bağımsız inceleme yapıldı; biçim doğrulaması geçti. Gerçek kullanıcı projesinde uçtan uca tarama veya patch üretimi denenmedi. Gelecek değişikliklerde yalnız etkilenen davranışlar doğrulanmalı; mevcut kontroller güncel doğrulama yapılmadan yeni sürüme kanıt sayılmamalıdır.

Yeni beş beceri aynı pinned kaynak sürümden uyarlanmıştır: `e6143c9807a001832badb63e89d58ffe25d542ec`. Kurulu yerel beceri adları bu GitHub yayını için değiştirilmedi; depodaki keşif adları klasörleriyle aynı `codex-` önekini taşır. Değiştirilmemiş frontend-design bu yayına dahil edilmedi. Yerel uyarlamaların önceki doğrulama sınırları geçerlidir; bu yayın yeni bir canlı proje testi anlamına gelmez.

README eklemesinde metinler mevcut beceri talimatlarıyla karşılaştırıldı ve göreli dosya bağlantıları depo ağacına göre kontrol edildi. Bu belge değişikliği için yeni PDF veya molekül üretimi testi yapılmadı.
