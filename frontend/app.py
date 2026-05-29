import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="SynthFinance AI", page_icon="🧠", layout="wide")

# Tasarım Sistemi (Design System)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1f77b4; color: white; font-weight: bold; }
    .stSidebar { background-color: #161b22; }
    div[data-testid="stMetricValue"] { color: #00ffcc; }
    .ai-box { background-color: #1e293b; padding: 20px; border-radius: 10px; border-left: 5px solid #38bdf8; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Yan Panel (Parametreler)
st.sidebar.header("🛠️ Simülasyon & AI Ayarları")
start_price = st.sidebar.number_input("Başlangıç Fiyatı ($)", value=100.0, step=10.0)
volatility = st.sidebar.slider("Oynaklık (Volatility %)", 5, 100, 25)
days = st.sidebar.slider("Gün Sayısı", 30, 365, 90)

generate_btn = st.sidebar.button("Uçtan Uca Veri ve AI Analizi Üret")

# Ana Ekran
st.title("🧠 SynthFinance AI - Akıllı Finansal Simülasyon")
st.subheader("FastAPI Backend Bağlantılı & Makine Öğrenmesi Destekli Zaman Serisi Platformu")

if generate_btn:
    with st.spinner('Frontend, Canlı FastAPI Backend servisine bağlanıyor ve AI Modeli eğitiliyor...'):
        try:
            # CANLI BACKEND ENTEGRASYONU (Hugging Face Spaces Canlı Bağlantısı)
            backend_url = "https://silakaymakci-synthfinance-backend.hf.space/generate-data"
            payload = {
                "start_price": start_price,
                "volatility": volatility,
                "days": days
            }
            
            # Canlı Backend'e istek atıyoruz
            response = requests.post(backend_url, json=payload)
            result = response.json()
            
            if result["status"] == "success":
                prices = result["data"]
                ai_data = result["ai_analysis"]
                
                # Tarih indeksleme
                dates = pd.date_range(start="2026-01-01", periods=days)
                df = pd.DataFrame({"Tarih": dates, "Simüle Edilen Fiyat": prices})
                df.set_index("Tarih", inplace=True)
                
                # --- AI İÇGÖRÜ PANELİ ---
                st.markdown(f"""
                <div class="ai-box">
                    <h4>🤖 Yapay Zeka Analist Raporu</h4>
                    <p><b>Trend Durumu:</b> {ai_data['ai_insight']}</p>
                    <p><b>AI Model Güven Skoru (R²):</b> %{ai_data['model_accuracy_score']*100:.2f}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # --- YENİ BAŞLAYANLAR İÇİN DİNAMİK TREND UYARILARI VE SÖZLÜK ---
                # Gelen trend verisinde 'Boğa' veya 'Ayı' (veya İngilizceleri) geçiyorsa kullanıcıyı yakalıyoruz
                trend_text = str(ai_data['ai_insight']).lower()
                
                if "boğa" in trend_text or "bull" in trend_text:
                    st.success(
                        "🐂 **Mevcut Piyasa Yapısı: Boğa Yapısı (Yükseliş Trendi)**",
                        help="Boğa Piyasası: Fiyatların yükselme eğiliminde olduğu, yatırımcıların iyimser olduğu ve alıcıların piyasaya hakim olduğu dönemleri ifade eder."
                    )
                elif "ayı" in trend_text or "bear" in trend_text:
                    st.error(
                        "🐻 **Mevcut Piyasa Yapısı: Ayı Yapısı (Düşüş Trendi)**",
                        help="Ayı Piyasası: Fiyatların düşüş trendinde olduğu, piyasada genel bir karamsarlığın hakim olduğu ve satıcıların baskın geldiği dönemleri ifade eder."
                    )
                else:
                    st.info(
                        "⚖️ **Mevcut Piyasa Yapısı: Yatay / Belirsiz Trend**",
                        help="Piyasa şu an net bir yöne (aşağı veya yukarı) sahip değil. Alıcılar ve satıcılar dengede görünüyor."
                    )
                
                # Metrik Kutuları (Buradaki help parametreleri sağ üstte soru işareti (?) çıkarır)
                col1, col2, col3 = st.columns(3)
                
                col1.metric(
                    label="Mevcut Fiyat (Son Gün)", 
                    value=f"${prices[-1]:.2f}",
                    help="Simülasyonun bittiği son gündeki varlık fiyatıdır."
                )
                
                col2.metric(
                    label="En Yüksek Seviye", 
                    value=f"${max(prices):.2f}",
                    help="Seçilen gün sayısı boyunca simüle edilen fiyatlar arasında ulaşılan en yüksek tepe noktasıdır."
                )
                
                col3.metric(
                    label="AI Gelecek (10. Gün) Tahmini", 
                    value=f"${ai_data['ai_predictions'][-1]:.2f}",
                    help="Makine öğrenmesi modelinin, geçmiş verileri inceleyerek önümüzdeki 10 gün sonrası için tahmin ettiği fiyat değeridir."
                )
                
                # Grafik Alanı
                st.write("### 📊 Finansal Zaman Serisi Grafiği")
                st.line_chart(df)
                
                # Veri İndirme
                csv = df.to_csv().encode('utf-8')
                st.download_button("Sentetik Veri Setini CSV Olarak İndir", csv, "synth_finance_ai_data.csv", "text/csv")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Canlı Backend servisine bağlanılamadı! Lütfen Hugging Face Space sunucunuzun çalışıp çalışmadığını kontrol edin.")
else:
    st.info("Modeli çalıştırmak ve yapay zeka tahmin raporunu oluşturmak için sol taraftaki panelden butonuna basınız.")
