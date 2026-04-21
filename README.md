# SynthFinance AI - Sentetik Finansal Veri Üreticisi (PRD)

## 1. Proje Özeti
SynthFinance AI, gerçek kullanıcı verilerini riske atmadan, makine öğrenmesi modellerini eğitmek ve test etmek için gerçekçi ancak tamamen yapay (sentetik) finansal zaman serisi verileri üreten bir sistemdir.

## 2. Hedef Kitle
- Finansal modelleme üzerinde çalışan veri bilimciler.
- Veri gizliliği (GDPR/KVKK) endişesi olan FinTech geliştiricileri.
- Algoritmik ticaret stratejilerini test etmek isteyen araştırmacılar.

## 3. MVP (Minimum Uygulanabilir Ürün) Kapsamı
- **Veri Modelleme:** Rastgele yürüyüş (random walk) ve Monte Carlo simülasyonu kullanarak sentetik borsa/fiyat verisi oluşturma.
- **Parametrik Ayarlar:** Kullanıcının volatilite (oynaklık) ve trend gibi değişkenleri belirleyebilmesi.
- **Export Özelliği:** Üretilen veriyi CSV formatında dışa aktarma (model eğitimi için hazır formatta).

## 4. Teknik Gereksinimler
- **Dil:** Python
- **Matematiksel Modeller:** Olasılık dağılımları (Normal Dağılım), Stokastik Süreçler.
- **Kütüphaneler:** NumPy, Pandas, Matplotlib/Seaborn (görselleştirme için).
- **Arayüz:** Streamlit (Kullanıcı parametreleri ayarlayıp "Generate" butonuna basacak).

## 5. Başarı Metrikleri
- Üretilen verilerin istatistiksel özelliklerinin (mean, variance) gerçek borsa verileriyle benzerlik göstermesi.
- Kullanıcı dostu arayüz üzerinden verinin 3 saniye içinde üretilmesi.

---
*Bu belge #2-upschool-question ödevi kapsamında hazırlanmıştır.*

