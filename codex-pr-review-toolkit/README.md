# codex-pr-review-toolkit

Kod/PR değişikliklerini hata, test kapsamı, hata yönetimi, yorum doğruluğu, tip tasarımı ve sadeleştirme açısından inceler.

## Kaynak

Bu beceri, **Anthropic'in `pr-review-toolkit` eklentisinden alınarak Codex için uyarlanmıştır**.

- [Kaynak paket](https://github.com/anthropics/claude-plugins-official/tree/e6143c9807a001832badb63e89d58ffe25d542ec/plugins/pr-review-toolkit)
- Sabit kaynak sürüm: `e6143c9807a001832badb63e89d58ffe25d542ec`
- Lisans: bu klasördeki [Apache 2.0 LICENSE](LICENSE); kaynak ve değişiklik bildirimi [NOTICE.md](NOTICE.md) içinde korunur.

Bu bir Codex uyarlamasıdır; kaynak eklentinin değiştirilmemiş sürümü veya resmî bir ürün değildir. Codex araçlarına göre düzenleme yapıldı; kök skill adına `codex-` eklendi. Rol dosyaları Codex alt ajanlarına aktarılacak referanslara dönüştürüldü; kapsam, yetki ve model seçimi mevcut araçlara uyarlandı.

## Kullanım

Bu klasörü kullanıcı skill dizinine veya projede `.agents/skills/codex-pr-review-toolkit/` altına kopyalayın. `$codex-pr-review-toolkit` adıyla ya da beceriyi mesajda belirterek çağırın. Destek dosyalarını SKILL.md ile birlikte koruyun.

## Doğrulama

18 Kasım 2026: Yerel sürümün biçimi, kaynak bağlantıları ve kurulum dosyalarının hash değerleri kontrol edildi; beş uyarlama birlikte bağımsız incelemeden geçti. Playground'un güvenli metin gösterimi örneği dört hedefli DOM sözleşmesi kontrolünden geçti. Bu yayında yalnız beceri adları ve kullanım/kaynak açıklamaları düzenlendi. Gerçek projelerde her iş akışının uçtan uca doğruluğu henüz denenmedi.
