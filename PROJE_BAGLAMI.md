# Güncel durum

2026-11-18: Skill koleksiyonuna `codex-security` eklendi. Yayındaki beş dosya GitHub üzerinden geri okunarak yüklenen içerikle eşleşti. Bekleyen değişiklik veya engel yok.

## Amaç ve dosya haritası

Bu depo yeniden kullanılabilir AI ajan skill'lerini bir arada tutar. Her skill kendi kök klasöründe, `SKILL.md` giriş dosyasıyla bulunur.

- `ders-konu-anlatimi/`: mevcut skill.
- `molekul-3b-modelle/`: mevcut skill; kendi references, scripts ve assets dosyalarını içerir.
- `codex-security/`: Codex yerel alt ajan araçlarıyla güvenlik incelemesi ve patch önerisi akışı. Kullanım, sınırlar ve doğrulama bilgileri `codex-security/README.md` içindedir.
- `LICENSE`: mevcut depo lisansı; bu çalışmada değiştirilmedi.

## Kararlar ve doğrulama

Skill'ler depoda kök klasörler olarak paylaşılır; bu deponun `.agents/skills/` dizinine kurulmazlar. Kullanıcı bunları kendi kullanıcı veya proje skill dizinine kopyalayabilir. Kullanıcı `codex-security` açıklamasının yalnız işlev ve kullanıma odaklanmasını istedi.

Yeni skill'in panel yardımcısı için yerelde 16 hedefli kontrol ve bağımsız inceleme yapıldı; biçim doğrulaması geçti. Gerçek kullanıcı projesinde uçtan uca tarama veya patch üretimi denenmedi. Gelecek değişikliklerde yalnız etkilenen davranışlar doğrulanmalı; mevcut kontroller güncel doğrulama yapılmadan yeni sürüme kanıt sayılmamalıdır.
