# Kimyasal doğrulama ve koordinat üretimi

## Kimlik ve kaynak

Ad, formül, net yük, izomerik tanım, kaynak URL'si, koordinat yöntemi ve konformer açıklaması kaydet. Belirtilmemiş stereokimyayı sessizce tek izomere dönüştürme. Racemik karışımı tek molekül sayma; nötr tür/iyon, tautomer ve protonlanma durumlarını ayır.

Yöntem için resmi başvurular:

- https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
- https://www.rdkit.org/docs/GettingStartedInPython.html
- https://www.rdkit.org/docs/RDKit_Book.html
- https://www.rdkit.org/docs/Cookbook.html

Bunları belirli bir molekülün doğrulandığına kanıt sayma; kullanımda ilgili bileşik kaydını aç. API/paket sürümü için güncel dokümantasyonu kontrol et.

PubChem'de önce doğru CID'yi eşleştir. Uygun kayıt için şu biçimi kullan:

```text
https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/<CID>/record/SDF?record_type=3d
```

404, 3B kaydı olmaması veya stereo farkında başka kayda sessizce geçme. Bileşik koordinatlarının deneysel olduğunu varsayma. İndirmeyi hazırlık aşamasında yap; sohbet görselleştirmesinin çalışma anında API erişimi gerektirmesini önle.

## RDKit ile konformer

Önce paketin mevcut olduğunu denetle. Yoksa ortamın kurallarına uygun yükle veya başka güvenilir koordinat kaynağı bul. Çalıştırmadığın kodun başarılı olduğunu varsayma.

```python
from rdkit import Chem
from rdkit.Chem import AllChem

mol = Chem.MolFromSmiles(verified_isomeric_smiles)
if mol is None:
    raise ValueError('SMILES okunamadı')
mol = Chem.AddHs(mol)
params = AllChem.ETKDGv3()
params.randomSeed = 2026
params.enforceChirality = True
ids = list(AllChem.EmbedMultipleConfs(mol, numConfs=1, params=params))
if not ids:
    raise ValueError('3B koordinatlar üretilemedi')
```

Bu örneği doğrulanmış molekül ve sürüme uyarlayıp çalıştır. Tek konformeri öğretici başlangıç olarak kullan; geometri sorunu, halka biçimi, esneklik veya enerji karşılaştırması gerektirirse örneklemeyi artır. Belirli bir örnek sayısını kapsamlı tarama diye sunma. Mevcut doğrulanmış koordinatlar ihtiyacı karşılıyorsa yeniden üretme; kullanılan yöntem/sürüm ve stereokimyayı kontrol et.

`AllChem.MMFFHasAllMoleculeParams(mol)` ile parametreleri kontrol et. Optimizasyon gerekirse `MMFFOptimizeMoleculeConfs` sonuçlarındaki yakınsama ve enerjiyi denetle. UFF'ye yalnızca parametreleri uygunsa geç. Başarısız yakınsamayı yok sayma. Uygun kuvvet alanı yoksa ETKDG sonucunun sınırını belirt veya uygun uzman yöntem bul. Enerjiyi ancak aynı kimlik ve yöntemle üretilmiş uygun konformerler arasında karşılaştır.

Kaynak stereokimyasını seçilen konformer ve dışa aktarılan bağ grafiğiyle karşılaştır. MOL/SDF stereo bilgisini koru. Veriye yalnızca öteleme, pozitif tekdüze ölçekleme ve determinantı +1 olan dönüş uygula; tek ekseni ters çevirmek kiral molekülü aynalar. Kamera projeksiyonu kimyasal veriyi değiştirmesin.

Konformasyon ile konfigürasyonu ayır. Konformer düğmesi, cis/trans veya enantiyomer dönüşümünü sıradan kamera hareketi gibi göstermesin. Geçiş animasyonu eklenirse doğrulanmamış doğrusal koordinat interpolasyonunu gerçek moleküler hareket veya reaksiyon mekanizması diye sunma.

## Denetleyici veri şeması

H dahil bütün atomları açık kaydet. `charge` formal yük, koordinatlar Å olsun. Bağlarda `a` ve `b` atom kimliği; `order` 1, 2, 3 veya aromatik gösterim için 1.5 olsun. Alışılmadık bağlanma için şemayı gerekirse genişlet; denetleyiciye uysun diye bağ değiştirme.

```json
{
  "name": "Metan",
  "formula": "CH4",
  "charge": 0,
  "coordinate_method": "idealized",
  "sources": [],
  "atoms": [
    {"id": 0, "element": "C", "charge": 0, "x": 0, "y": 0, "z": 0},
    {"id": 1, "element": "H", "charge": 0, "x": 0.6293, "y": 0.6293, "z": 0.6293},
    {"id": 2, "element": "H", "charge": 0, "x": 0.6293, "y": -0.6293, "z": -0.6293},
    {"id": 3, "element": "H", "charge": 0, "x": -0.6293, "y": 0.6293, "z": -0.6293},
    {"id": 4, "element": "H", "charge": 0, "x": -0.6293, "y": -0.6293, "z": 0.6293}
  ],
  "bonds": [
    {"a": 0, "b": 1, "order": 1},
    {"a": 0, "b": 2, "order": 1},
    {"a": 0, "b": 3, "order": 1},
    {"a": 0, "b": 4, "order": 1}
  ]
}
```

```bash
python <skill-directory>/scripts/validate_model.py <model.json>
```

`--planar-ids 0,1,2,3,4,5 --planarity-tol 0.03` ile seçili atomların en iyi düzlemden maksimum sapmasını Å cinsinden denetle; bu seçenek NumPy gerektirir. Formülde Hill yazımını, yük için ayrı `charge` alanını kullan. Betiğin izotop, radikal, bağlantı izomerliği veya stereo eşleştirmesi yapmadığını dikkate al.

## Yaygın örnekler

| Örnek | Doğru özellik | Kaçınılacak hata |
| --- | --- | --- |
| Metan | C çevresinde yaklaşık 109,5° tetrahedral düzen | Düz artı biçiminde dört H |
| Etin | C–C–H iskeletinde doğrusal düzen | Üçlü bağın uçlarını bükmek |
| Benzen | C/H aynı düzlemde, eşdeğer C–C uzaklıkları | Sabit üç kısa/üç uzun fiziksel bağ |
| Siklohekzan | C₆H₁₂, sandalye konformasyonu | Benzenin bağlarını teke çevirip düz bırakmak |
| Etan | İki C'nin çevresinde tetrahedral düzen | Bütün H'leri tek düzleme koymak |
| 2-büten | C=C çevresinde E/Z geometrisi | Çift bağı serbestçe döndürmek |
| Enantiyomer çifti | Kaynakla eşleşen stereo, aynada farklılık | Sıradan döndürmeyle birbirine dönüşüm |

Kesin açı/uzunluk istenirse tür, konformer ve yönteme bağlı ölçümü kaynaklandır. Okul için idealize değeri deneysel veri diye sunma. Hückel kuralını tüm aromatik sistemlerin istisnasız tek ölçütü sayma; benzen gibi uygun basit örneklerde kullan.
