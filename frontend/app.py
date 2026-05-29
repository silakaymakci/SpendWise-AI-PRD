import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Sayfa Genişlik Ayarı
st.set_page_config(page_title="Risk Analyzer AI", layout="wide")

# --- ÜST PANEL (SADE BAŞLIK & RENK REHBERİ) ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("📊 Risk Analyzer AI")
    st.caption("Verilerinizi yükleyin, risk analizini anında görüntüleyin.")

with col2:
    # Renk teorisini kalabalık yapmasın diye expander (açılır kutu) içine aldık
    with st.expander("🎨 Risk Renk Teorisi Kılavuzu"):
        st.markdown("""
        - 🔴 **Kırmızı:** Yüksek Risk (Kritik Müdahale)
        - 🟡 **Sarı:** Orta Risk (Yakın Takip)
        - 🟢 **Yeşil:** Düşük Risk (Güvenli Bölge)
        """)

st.divider()

# --- YAN PANEL (DOSYA YÜKLEME VE PARAMETRELER) ---
st.sidebar.header("📥 Veri Girişi")
uploaded_file = st.sidebar.file_uploader("Analiz edilecek dosyayı seçin (.csv veya .xlsx)", type=["csv", "xlsx"])

# Terim açıklamaları için soru işareti (help) parametresini kullandık
volatility_help = "Fiyatın veya verinin ne kadar dalgalandığının ölçüsü. Risk seviyesini doğrudan etkiler."
topology_help = "Veri hareketlerinin geometrik ve yapısal bağlarını analiz etme yöntemi."

st.sidebar.subheader("⚙️ Analiz Ayarları")
volatility_threshold = st.sidebar.slider(
    "Volatilite Eşiği", 
    min_value=0.0, max_value=1.0, value=0.5, step=0.1,
    help=volatility_help
)

use_topology = st.sidebar.checkbox(
    "Topolojik Yaklaşım Kullan", 
    value=True,
    help=topology_help
)

# --- ANA PANEL (SONUÇLAR VE GRAFİKLER) ---
if uploaded_file is not None:
    # Örnek veri okuma (Kullanıcı dosya yüklediğinde aktif olur)
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.success("Veri başarıyla yüklendi!")
        st.dataframe(df.head(), use_container_width=True)
    except Exception as e:
        st.error(f"Dosya okunurken bir hata oluştu: {e}")
else:
    # Kullanıcı dosya yüklemediyse arayüz boş durmasın diye gösterilecek Simülasyon Verisi
    st.info("💡 Lütfen sol taraftan bir veri dosyası yükleyin. Aşağıda örnek simülasyon çıktısı gösterilmektedir:")
    
    # Rastgele veri üretimi
    np.random.seed(42)
    sample_data = pd.DataFrame({
        "Varlık/Müşteri ID": [f"ID_{i}" for i in range(1, 51)],
        "Volatilite Score": np.random.uniform(0.1, 0.9, 50),
        "Kayıp Potansiyeli": np.random.uniform(10, 100, 50)
    })
    
    # Renk teorisine göre risk durumunu belirleme
    def assign_risk_color(row):
        if row["Volatilite Score"] > 0.65:
            return "🔴 Yüksek Risk"
        elif row["Volatilite Score"] > 0.35:
            return "🟡 Orta Risk"
        else:
            return "🟢 Düşük Risk"
            
    sample_data["Risk Durumu"] = sample_data.apply(assign_risk_color, axis=1)
    
    # Grafik Çizimi (Renk Teorisine Sadık Kalarak)
    fig = px.scatter(
        sample_data, 
        x="Volatilite Score", 
        y="Kayıp Potansiyeli", 
        color="Risk Durumu",
        color_discrete_map={
            "🔴 Yüksek Risk": "#EF553B", 
            "🟡 Orta Risk": "#FECB52", 
            "🟢 Düşük Risk": "#00CC96"
        },
        title="Risk Dağılım Grafiği",
        labels={"Volatilite Score": "Volatilite Skoru", "Kayıp Potansiyeli": "Potansiyel Kayıp ($)"}
    )
    
    st.plotly_chart(fig, use_container_width=True)
