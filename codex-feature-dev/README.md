# codex-feature-dev

Yeni özellikleri keşif, gereksinim, tasarım, uygulama ve inceleme aşamalarıyla geliştirir.

## Kaynak

Bu beceri, **Anthropic'in `feature-dev` eklentisinden alınarak Codex için uyarlanmıştır**.

- [Kaynak paket](https://github.com/anthropics/claude-plugins-official/tree/e6143c9807a001832badb63e89d58ffe25d542ec/plugins/feature-dev)
- Sabit kaynak sürüm: `e6143c9807a001832badb63e89d58ffe25d542ec`
- Lisans: bu klasördeki [Apache 2.0 LICENSE](LICENSE); kaynak ve değişiklik bildirimi [NOTICE.md](NOTICE.md) içinde korunur.

Bu bir Codex uyarlamasıdır; kaynak eklentinin değiştirilmemiş sürümü veya resmî bir ürün değildir. Codex araçlarına göre düzenleme yapıldı; kök skill adına `codex-` eklendi. Rol dosyaları Codex alt ajanlarına aktarılacak referanslara dönüştürüldü; kapsam, yetki ve model seçimi mevcut araçlara uyarlandı.

## Kullanım

Bu klasörü kullanıcı skill dizinine veya projede `.agents/skills/codex-feature-dev/` altına kopyalayın. `$codex-feature-dev` adıyla ya da beceriyi mesajda belirterek çağırın. Destek dosyalarını SKILL.md ile birlikte koruyun.

## Doğrulama

18 Kasım 2026: Yerel sürümün biçimi, kaynak bağlantıları ve kurulum dosyalarının hash değerleri kontrol edildi; beş uyarlama birlikte bağımsız incelemeden geçti. Playground'un güvenli metin gösterimi örneği dört hedefli DOM sözleşmesi kontrolünden geçti. Bu yayında yalnız beceri adları ve kullanım/kaynak açıklamaları düzenlendi. Gerçek projelerde her iş akışının uçtan uca doğruluğu henüz denenmedi.
