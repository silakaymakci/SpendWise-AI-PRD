import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Sayfa Konfigürasyonu (Tarayıcı sekmesindeki isim ve ikon)
st.set_page_config(page_title="SynthFinance AI", page_icon="📈", layout="wide")

# 2. Tasarım Sistemi (Design System) - CSS Dokunuşları
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #2e7d32; color: white; border: none; }
    .stButton>button:hover { background-color: #1b5e20; border: none; }
    h1, h2, h3 { color: #ffffff; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sol Panel (Sidebar) - Kullanıcı Girişleri
st.sidebar.title("⚙️ Parametreler")
st.sidebar.info("Modelin sentetik veri üretmesi için değerleri giriniz.")

start_price = st.sidebar.number_input("Başlangıç Fiyatı ($)", min_value=1.0, value=100.0)
volatility = st.sidebar.slider("Oynaklık (Volatilite %)", 1, 100, 20)
days = st.sidebar.slider("Gün Sayısı (Simülasyon Süresi)", 7, 365, 90)

generate_btn = st.sidebar.button("Sentetik Veri Oluştur")

# 4. Mock Veri Fonksiyonu (Haftaya Backend'e bağlanacak kısım)
def create_mock_data(base, vol, period):
    # Basit bir finansal hareket simülasyonu
    change = np.random.normal(0, vol/100, period)
    price_series = base * (1 + change).cumprod()
    dates = pd.date_range(start="2026-01-01", periods=period)
    return pd.DataFrame({"Tarih": dates, "Fiyat": price_series})

# 5. Ana Ekran İçeriği
st.title("📈 SynthFinance AI")
st.write("Finansal modeller için yapay veri üretim arayüzü.")

if generate_btn:
    # Yüklenme efekti (Hocaların sevdiği bir detay)
    with st.spinner('Matematiksel model çalıştırılıyor...'):
        time.sleep(1.5) # Gerçekçi bekleme süresi
        
        # Veriyi oluştur
        df = create_mock_data(start_price, volatility, days)
        
        # Üst Metrikler
        m1, m2, m3 = st.columns(3)
        current_val = df['Fiyat'].iloc[-1]
        m1.metric("Son Değer", f"${current_val:.2f}")
        m2.metric("En Yüksek", f"${df['Fiyat'].max():.2f}")
        m3.metric("Değişim", f"%{((current_val/start_price)-1)*100:.2f}")
        
        # Çizgi Grafik
        st.subheader("Simülasyon Grafiği")
        st.line_chart(df.set_index("Tarih"))
        
        # Veri Tablosu ve İndirme
        with st.expander("Ham Verileri Gör ve İndir"):
            st.dataframe(df, use_container_width=True)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Veriyi CSV Olarak İndir", csv, "data.csv", "text/csv")
else:
    # İlk açılışta görünecek boş ekran mesajı
    st.warning("Lütfen sol taraftan parametreleri seçip butona basarak simülasyonu başlatın.")
