# Proje Geliştirme Planı: SynthFinance AI

## Backend (Servis 1) - [TAMAMLANDI]
- **Kurulum:** Python/FastAPI ortamı yapılandırıldı.
- **İşlev:** Geometrik Brownian Hareketi (GBM) simülasyon motoru yazıldı.
- **AI Entegrasyonu:** `scikit-learn` Linear Regression modeli eklenerek trend analizi, gelecek 10 gün tahmini ve R² güven skoru hesaplama özellikleri tamamlandı.
- **API:** `/generate-data` (POST) endpoint'i hem simülasyonu hem de AI sonuçlarını dönecek şekilde aktifleştirildi.

## Frontend (Servis 2) - [TAMAMLANDI]
- **Kurulum:** Streamlit arayüzü `/frontend` dizinine kuruldu.
- **Tasarım:** Custom CSS ile finansal temaya uygun Dark Mode "Design System" uygulandı.
- **Entegrasyon:** `requests` kütüphanesi eklenerek mock veri tamamen kaldırıldı; artık FastAPI backend'ine bağlanarak canlı veri ve AI raporu sunuyor.

## Tamamlanan Aşamalar
1. [x] Backend ve Frontend klasörlerinin mimari olarak ayrıştırılması (2. Hafta).
2. [x] Streamlit arayüz tasarımı ve Mock veri prototipi (4. Hafta).
3. [x] FastAPI ile GBM matematiksel motorunun yazılması.
4. [x] Scikit-Learn ile Yapay Zeka (Trend & Risk Analizi) katmanının backend'e eklenmesi.
5. [x] Frontend ve Backend servislerinin uçtan uca (End-to-End) birbirine bağlanması.
