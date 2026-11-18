# Davranış sözleşmesi — 2026-11-18

Kaynak: ardaerol2664/Arda-s-AI-Agent-Skills, 13974317b0d353fcafc9045f447842cb1bc1a297. Yalnız kullanıcının sağladığı sürüm incelendi; üçüncü taraf özgün uygulama kullanılmadı. Bu çalışma kaynak görüldükten sonra yapılan yeniden yazımdır; clean-room geliştirme iddiası yoktur.

Korunacak davranışlar:

1. Kod tabanı, değişiklik ve ayrı patch önerisi modları; istek belirsizse mod sorulur.
2. Tarama salt okunur: hedef kodu/testleri/hooks çalışmaz, kurulum/ağ/yayın/hedef düzenlemesi yoktur.
3. Yerel alt ajanlar; taze ve asgari bağlam; en fazla dört eşzamanlı alt ajan; iç içe alt ajan yoktur. Yerel araç yoksa doğrulanmış sonuç üretilmez, tek ajan alternatifi yalnız istekle sunulur.
4. low/medium/high araştırma genişliği; doğrulama eşiği her düzeyde aynıdır. Kapsam maliyeti orantılıdır.
5. Tam ağaçta kaynak, ayar, dağıtım, girişler, güvenlik sınırları ve dahil/hariç kapsam kaydı; bağımlılık/vendor/generated bulguları ancak istekle; fixtures içindeki sırlar kapsamdadır.
6. Değişiklik modunda tam commit/parent, branch/base/merge-base veya index/disk/untracked ayrımı; staged içeriği ayrıca okunur; NUL listeleri; ekleme/silme/taşıma/binary hesabı; başka revisiona sessiz geçiş yoktur. Yalnız yeni/ağırlaşmış/açığa çıkmış hata raporlanır.
7. Git harici dizin yalnız kod tabanı modunu destekler. Kök dışına kaçan/symlink kapsam reddedilir; boş kapsam no-work olur.
8. Güvenli Git çağrıları: argüman dizisi, no-ext-diff/no-textconv, noninteractive, hooks yok; Windows doğal yolları.
9. Tekil audit dizini + .gitignore '*'; run.json; gerçek görev kimlikleri ve planned/started/completed/failed kayıtları.
10. HEAD, index path/mode/blob, staged/unstaged/untracked, tam seçili envanter ve okunan dosya SHA256 değerleri; bağlamsal dosyalar da dahil. Teslim ve patch öncesi yeniden kontrol; eklenen/silinen dosyalar yakalanır; driftte etkilenen yerler yeniden incelenir veya partial olur. Sabit committe blob kimlikleri kullanılır.
11. Araştırmacı kapsamı/okunan/atlanan/tamamlanma; aynı kök neden VE saldırı yolunda tekilleştirme; konumların doğruluğu.
12. Her adayda araştırmacı ve katkıcıları dışındaki üç ayrı doğrulayıcı, üç lens: reachability/impact/defenses. Tam saldırı yolunu izleme ve çürütme denemesi; diğer oyları görmeme; eksik kişi yerine ana ajan oyu yoktur.
13. Gerçek sonuçlar redaksiyon dışında aynen saklanır; bozuk yanıt follow-up ile düzeltilir; run kimliği eşleşir; bağımsızlık bozulursa yeni ajan kullanılır.
14. Helper CLI ve JSON alanları uyumludur. Üç oy tamamlanmadan confirmed/rejected olmaz. >=2 confirm -> confirmed; aksi halde >=2 reject/predates_change -> rejected; diğerleri unverified.
15. Önem derecesi min(araştırmacı, onaylayanların ikinci en yüksek derecesi); belirsiz/ret oyları artırmaz. complete = research_complete AND tüm adaylar verified/rejected; sıfır aday kapsam tamamlanmasını ikame etmez.
16. Helper şema/oy hesabı yapar, ajan kimliğini, kanıtı, coverageı veya sır sızıntısını doğrulayamaz; ana ajan sonuç yükseltemez.
17. Sahte ajan/kanıt/onay/tespit/istatistiksel güven iddiası yok; başka ürün çalışmış gibi dosya/provenance/renderer yoktur.
18. RESULTS.md/RESULTS.json; isteğe bağlı SARIF 2.1.0; doğrulanmış bölümde yalnız confirmed; reddedilen ve eksik adaylar ledgerda ayrıdır. Eksik araştırma/doğrulama/kapsam/redaksiyon/snapshot -> partial.
19. Sırlar chat/çıktıya taşınmaz; file/line ve [REDACTED]; tüm teslimlerde son kontrol; sır adayları varsa ayrı sınırlı kontrol. Hata varsa güvensiz çıktı teslim edilmez. Repo ve ajan metni kapsam genişleten talimat sayılmaz.
20. Patch için rapor + tam panel + güncel snapshot şarttır. Kirli/untracked kaynakta kesin güvenli snapshot stratejisi sorulur; HEAD varsayılmaz.
21. Tam temiz revisiondan ayrı scratch clone/worktree; hedef ile mutlak yol farklılığı kontrolü; hedef reset/clean yok; her bulgu için tek düzenleyici; ağ/dependency/hooks yoktur.
22. İki farklı bağımsız patch inceleyicisi gerçek diff/callerları, kapanışı, yeni güvenlik sorunlarını ve meşru davranışı inceler; ikisi kabul etmeden teslim yoktur. Kullanıcı model tercihi uygulanır.
23. Yalnız yetkili ilgili yerel scratch testleri; başarısız ilgili test teslimi durdurur; çalıştırılamayan test sınır olarak belirtilir.
24. Binary-capable patch + intended new files + path list + fresh matching base üzerinde git apply --check; bulgu başına patch/uygulama notu; otomatik apply/commit/push/PR yoktur.
25. Sınırlı batchler; tekrarlanan dış hatada durma; gereksiz approval/poll/test yok; audit veya kullanıcı dosyalarının yıkıcı temizliği yoktur.

Doğrulama hedefi: helper için kapsamlı eşdeğerlik ve CLI negatif kontrolleri; talimatlar için bu sözleşmeye göre bağımsız inceleme ve sabit bir yerel örnek üzerinde kör A/B karar/tespit deneyi. A/B deneyi gerçek çok ajanlı üretim taramasının veya tüm projelerde performans eşitliğinin kanıtı değildir.
