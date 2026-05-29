# SynthFinance AI - Akıllı Sentetik Finansal Veri Üreticisi

## 1. Proje Özeti
SynthFinance AI, gerçek kullanıcı verilerini riske atmadan, makine öğrenmesi modellerini eğitmek ve test etmek için gerçekçi finansal zaman serisi verileri üreten ve bu verileri yerleşik bir Yapay Zeka modeliyle analiz eden uçtan uca bir platformdur.

## 2. Teknik Mimari & Servis Yapısı
Proje, kurumsal standartlara uygun olarak iki ayrı servis (Separation of Concerns) mimarisinde geliştirilmiştir:
- **Backend (Port: 8000):** Python, FastAPI, NumPy, Scikit-Learn. Matematiksel simülasyonu yapar ve AI regresyon modellerini çalıştırır.
- **Frontend (Port: 8501):** Streamlit, Pandas, Requests. Kullanıcı parametrelerini toplar, backend API'si ile konuşur ve grafiksel arayüzü sunar.

## 3. Yapay Zeka ve Matematiksel Modeller
- **Veri Üretimi:** Finansal piyasaların standart stokastik süreci olan **Geometrik Brownian Hareketi (GBM)** kullanılmıştır.
- **AI Tahminleme & Analiz:** Üretilen veriler anlık olarak **Linear Regression (Makine Öğrenmesi)** modeline beslenir. Model, trendin yönünü (Boğa/Ayı) tespit eder, geleceğe yönelik 10 günlük fiyat tahmini yapar ve modelin güven skorunu ($R^2$) hesaplar.

---
*Bu proje Up School bünyesinde uçtan uca (End-to-End) AI ürünü olarak geliştirilmiştir.*
