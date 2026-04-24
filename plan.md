# Proje Geliştirme Planı: SynthFinance AI

## Backend (Servis 1)
- **Kurulum:** Python/FastAPI ortamının kurulumu.
- **İşlev:** Geometrik Brownian Hareketi (GBM) simülasyon motorunun yazılması.
- **API:** Üretilen veriyi JSON formatında sunacak endpoint'in (`/generate-data`) geliştirilmesi.

## Frontend (Servis 2)
- **Kurulum:** Streamlit arayüzünün `/frontend` dizinine yapılandırılması.
- **İşlev:** Kullanıcıdan parametreleri alma (volatilite, zaman, başlangıç fiyatı).
- **Entegrasyon:** Backend'e istek atıp dönen veriyi grafik olarak çizdirme.

## Adımlar
1. Backend ve Frontend klasörlerinin ayrıştırılması.
2. Backend tarafında veri üretim mantığının tamamlanması.
3. Frontend tarafında kullanıcı arayüzü ve API bağlantısının kurulması.
4. Test ve dokümantasyon.
