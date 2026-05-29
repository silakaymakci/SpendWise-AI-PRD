# 🛡️ Product Requirement Document (PRD) - SynthFinance AI

## 1. Proje Genel Bakışı (Overview)
**SynthFinance AI**, makine öğrenmesi destekli zaman serisi simülasyonları üreten ve finansal piyasalardaki risk/trend durumlarını analiz eden akıllı bir finans platformudur. Platform, karmaşık finansal ve matematiksel verileri işleyerek kullanıcıya sade, anlaşılır ve yönlendirici bir arayüz sunmayı amaçlar.

### 1.1 Çözülen Problem
Geleneksel finansal analiz araçları, genellikle karmaşık grafikler, ham veriler ve teknik terimler üreterek finansal okuryazarlığı düşük veya yeni başlayan kullanıcıları bu verilerin karşısında yalnız bırakır. Kullanıcılar bir trendin veya risk puanının ne anlama geldiğini yorumlamakta zorlanır. `SynthFinance AI`, bu verileri insan diline çevirerek ve uygulama içi anlık terim açıklamaları sunarak finansal analizi herkes için erişilebilir kılar.

### 1.2 Hedef Kullanıcı Kitlesi
* Finansal piyasalara yeni adım atmış, teknik terimlere uzak başlangıç seviyesindeki yatırımcılar.
* Sentetik zaman serisi verilerine ihtiyaç duyan veri bilimciler ve araştırmacılar.
* Yapay zeka destekli karar destek mekanizmalarından yararlanmak isteyen finans meraklıları.

---

## 2. Temel Özellikler (Core Features)

### 2.1 Kullanıcı Ayarlı Parametrik Simülasyon
* Kullanıcılar, sol panel üzerinden simülasyonun **Başlangıç Fiyatı ($)**, piyasanın **Oynaklık (Volatility %)** oranı ve projeksiyonun kapsayacağı **Gün Sayısı** parametrelerini serbestçe optimize edebilirler.

### 2.2 Uçtan Uca Yapay Zeka Analiz Motoru
* Canlı FastAPI backend mimarisi ile entegre çalışarak zaman serisi verileri üzerinden anlık makine öğrenmesi modeli eğitilir.
* Model sonuçlarına göre **Trend Durumu** ve **AI Model Güven Skoru ($R^2$)** hesaplanarak kullanıcıya sunulur.

### 2.3 Uygulama İçi Dinamik Terim Açıklamaları (In-App Guidance)
* Yapay zeka tarafından algılanan piyasa yapısına göre (Boğa, Ayı veya Yatay Trend) dinamik ve renk kodlu uyarı kutuları açılır.
* Bu kutuların içerisinde yer alan **"💡 Nedir?"** alt başlıkları sayesinde, terimlerin finansal tanımları doğrudan kullanıcıya aktarılır.
* Metriklerin sağ üst köşelerinde yer alan yerleşik bilgi kutucukları (tooltips) sayesinde, fareyle üzerine gelindiğinde ("AI Gelecek Tahmini" gibi) teknik açıklamalar anlık olarak görüntülenir.

### 2.4 İnteraktif Görselleştirme ve Veri Aktarımı
* Üretilen sentetik veriler interaktif bir zaman serisi grafiği üzerinde listelenir. Kullanıcılar grafik çizgisi üzerinde fareyi gezdirerek geçmiş ve tahmini fiyat kırılımlarını canlı inceleyebilir.
* Analiz edilen tüm ham veri seti, tek bir tıkla **CSV formatında** bilgisayara indirilebilir.

---

## 3. Teknik Gereksinimler & Kısıtlar
* **Arayüz (Frontend):** Python tabanlı Streamlit kütüphanesi kullanılacaktır.
* **Arka Plan (Backend):** Python FastAPI ile canlı servis sunulacak ve modelleme Hugging Face Spaces üzerinde barındırılacaktır.
* **Güvenlik:** Gerçek API anahtarları ve hassas veritabanı şifreleri kaynak kodda barındırılmayacaktır.
