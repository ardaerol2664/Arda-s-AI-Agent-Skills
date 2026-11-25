# Replica for Codex

[Jake Schincariol’un Replica skill paketi](https://github.com/Jakeschincariol/replica-skill), belgelenmiş davranışları incelemek ve bağımsız bir uygulama geliştirmek için Codex’e uyarlandı. [İncelenen upstream revizyonu](https://github.com/Jakeschincariol/replica-skill/tree/77c9436fb3d18c3d58169efb8caf4fe906b0dc51).

## Uyarlama

26 Kasım 2026’da kaynak keşfi, mimari, özgün tasarım, uygulama, test ve davranış karşılaştırması tek bir `SKILL.md` altında birleştirildi. Upstream’deki 11 ayrı Claude komutu, eklenti bildirimi, Python yardımcıları ve zorunlu yayın zinciri bu pakete taşınmadı. Kaynak ayrıntıları için [keşif](https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/replica-recon/SKILL.md), [tasarım](https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/replica-design/SKILL.md), [test](https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/replica-test/SKILL.md) ve [karşılaştırma](https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/replica-diff/SKILL.md) dosyalarına bakılabilir.

Codex’in beceri seçicisinden çağırmak için `codex-replica` klasörünü ilgili projenin `.agents/skills/` dizinine yerleştir ve yeni bir oturumda `$codex-replica` kullan. Beceri, proje talimatları `SKILL.md` dosyasına yönlendirdiğinde doğrudan da okunabilir. [Codex skill belgeleri](https://learn.chatgpt.com/docs/build-skills).

Örnek kullanım: “`$codex-replica` ile bu iş akışının kamuya açık belgelerini incele ve özgün uygulamamız için doğrulanabilir kabul ölçütleri yaz.”

Upstream telif ve MIT lisans metni [LICENSE](LICENSE) dosyasındadır.
