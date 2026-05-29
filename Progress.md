# Progress Log - SynthFinance AI

Geliştirme sürecinde alınan kararlar, karşılaşılan zorluklar ve çözümlerin günlüğüdür.

- **Aşama 1 (Mimari Kurulum):** Proje kurumsal standartlara uygun olarak `/backend` ve `/frontend` servislerine ayrıştırıldı. Boş dizinlerin korunması amacıyla `.gitkeep` yapısı uygulandı.
- **Aşama 2 (Matematik & API):** FastAPI üzerinde Geometrik Brownian Hareketi (GBM) motoru yazıldı. Vektörel hesaplamalar için NumPy entegre edildi.
- **Aşama 3 (AI Entegrasyonu):** Geliştirilen simülasyon çıktılarının analizi için Scikit-Learn kütüphanesi kullanılarak Linear Regression modeli backend katmanına eklendi. Gelecek 10 günün tahmini veri setine entegre edildi.
- **Aşama 4 (Uçtan Uca Bağlantı):** Frontend mock verilerden tamamen temizlenerek `requests` kütüphanesi ile API endpoint'ine bağlandı.
