# Codex Security

Yerel kaynak kodunda veya belirli bir Git değişikliğinde güvenlik hataları aramak, aday bulguları bağımsız ajanlarla sınamak ve istenirse ayrı incelenmiş patch önerileri hazırlamak için bir Codex becerisi.

## Kullanım

Klasörü kendi skill dizininize veya projenizde `.agents/skills/codex-security/` konumuna kopyalayın. `$codex-security` ile çağırın. Örneğin: `Bu projenin backend dizinini codex-security ile incele.` Yerel alt ajan araçları ve Python 3.8+ gerekir; yardımcı program ek Python paketi kullanmaz.

`SKILL.md` kapsamı ve çalışma sınırlarını, `references/workflow.md` işlemleri, `references/contracts.md` kayıt biçimleri ile karar kurallarını açıklar. `scripts/panel.py` gerçek inceleyici sonuçlarından karar ve önem derecesi hesaplar; kendi başına kod taramaz veya ajan başlatmaz.

Her aday için araştırmaya katılmamış üç ayrı doğrulayıcı gerekir. Üçü tamamlandığında en az iki onay bulguyu kabul ettirir. Eksik çalışma kısmi sonuç olarak gösterilir. Yardımcı program gerçek ajan kimliğini veya kanıtın doğruluğunu teyit edemez; bunları ana ajan kontrol eder. Patch önerisi hedefe otomatik uygulanmaz.

## Doğrulama

Yeniden yazımın karşılaştırmalı kontrolleri ve sınırları depo kökündeki `DEGISIKLIK_RAPORU.md` dosyasında tutulur. Ajan talimatları ve yardımcı program için yapılan kontroller, bütün projelerde aynı tespit başarısını kanıtlamaz.
