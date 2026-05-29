import streamlit as st
import pandas as pd
import requests

# Sayfa yapılandırması ve geniş mod
st.set_page_config(page_title="SynthFinance AI Terminal", page_icon="🧠", layout="wide")

# Kurumsal Finansal Terminal CSS Tasarımı
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 6px; height: 3.2em; background-color: #1f77b4; color: white; font-weight: bold; border: none; transition: 0.3s; }
    .stButton>button:hover { background-color: #145a8d; box-shadow: 0px 0px 10px rgba(31,119,180,0.5); }
    .stSidebar { background-color: #161b22; }
    div[data-testid="stMetricValue"] { color: #00ffcc; font-family: 'Courier New', monospace; font-weight: bold; }
    .ai-box { background-color: #1e293b; padding: 22px; border-radius: 8px; border-left: 6px solid #38bdf8; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .info-title { color: #58a6ff; font-weight: bold; font-size: 1.1em; margin-bottom: 8px; }
    .badge { background-color: #21262d; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; border: 1px solid #30363d; color: #c9d1d9; }
    </style>
    """, unsafe_allow_html=True)

# --- YAN PANEL (PARAMETRELER VE KILAVUZ) ---
st.sidebar.markdown("### 🧠 SynthFinance AI")
st.sidebar.markdown("<span class='badge'>Sürüm: v1.0.0 (Canlı)</span>", unsafe_allow_html=True)
st.sidebar.write("---")

st.sidebar.header("🛠️ Simülasyon & AI Ayarları")
start_price = st.sidebar.number_input("Başlangıç Fiyatı ($)", value=100.0, step=10.0, help="Simülasyonun başlayacağı baz fiyat seviyesi.")
volatility = st.sidebar.slider("Oynaklık (Volatility %)", 5, 100, 25, help="Piyasadaki risk ve ani dalgalanma katsayısı.")
days = st.sidebar.slider("Gün Sayısı (Zaman Serisi)", 30, 365, 90, help="Üretilecek ve analiz edilecek toplam gün sayısı.")

st.sidebar.write("---")
generate_btn = st.sidebar.button("Uçtan Uca Veri ve AI Analizi Üret")

st.sidebar.write("")
st.sidebar.markdown("""
**💡 Hızlı İpucu:** Oynaklığı **%60'ın üzerine** çıkararak yapay zekanın yüksek riskli (ayı piyasası/volatil) piyasa koşullarına nasıl tepki verdiğini ve analiz raporunu nasıl güncellediğini videonuzda gösterebilirsiniz!
""")

# --- ANA EKRAN ÜST BAŞLIK ---
st.title("🧠 SynthFinance AI - Akıllı Finansal Simülasyon Terminali")
st.markdown("#### **FastAPI Dağıtık Mimari Bağlantılı & Makine Öğrenmesi Destekli Zaman Serisi Platformu**")
st.write("---")

# --- PROJE ÖZETİ VE REHBER (SADELİĞİ KIRAN İLK BÖLÜM) ---
col_info1, col_info2 = st.columns([2, 1])

with col_info1:
    st.markdown("""
    ### 📋 Platform Hakkında
    SynthFinance AI; gerçek kullanıcı verilerini ve finansal gizliliği riske atmadan, makine öğrenmesi modellerini test etmek ve eğitmek amacıyla kurumsal standartlarda **sentetik finansal zaman serisi verileri** üretir. 
    Platform, mikroservis mimarisine uygun olarak **Frontend (Streamlit)** ve **Backend (FastAPI)** olmak üzere iki bağımsız katmandan oluşur.
    """)

with col_info2:
    st.markdown("""
    ### 🔬 Kullanılan Yapay Zeka Metodu
    Üretilen stokastik veriler, backend sunucusunda anlık olarak **Scikit-Learn Linear Regression** modeline beslenir. Yapay zeka, zaman serisinin matematiksel eğilimini (Trend Skoru) hesaplayarak geleceğe dönük projeksiyonlar sunar.
    """)

st.write("")

# --- ANA AKIŞ VE TETİKLEME ---
if generate_btn:
    with st.spinner('Frontend bulut sunucusu, Hugging Face üzerindeki canlı FastAPI Backend servisine bağlanıyor...'):
        try:
            # Canlı Backend Endpoint Adresi
            backend_url = "https://silakaymakci-synthfinance-backend.hf.space/generate-data"
            payload = {
                "start_price": start_price,
                "volatility": volatility,
                "days": days
            }
            
            # API İsteği
            response = requests.post(backend_url, json=payload)
            result = response.json()
            
            if result["status"] == "success":
                prices = result["data"]
                ai_data = result["ai_analysis"]
                
                # Veriyi Pandas DataFrame yapısına dönüştürme ve tarih indeksleme
                dates = pd.date_range(start="2026-01-01", periods=days)
                df = pd.DataFrame({"Tarih": dates, "Simüle Edilen Fiyat ($)": prices})
                df.set_index("Tarih", inplace=True)
                
                # --- AI İÇGÖRÜ VE ANALİZ PANELİ ---
                st.markdown("""<div class='ai-box'>
                    <h3 style='margin-top:0; color:#38bdf8;'>🤖 Yapay Zeka Analist Raporu & Risk Analizi</h3>
                    <p style='font-size:1.15em;'><b>Trend Durumu ve Yatırım Sinyali:</b> {}</p>
                    <p style='font-size:1em; color:#a1a1aa;'>Bu analiz, üretilen zaman serisi matrisinin makine öğrenmesi regresyon katsayıları (eğim parametreleri) taranarak otomatik olarak oluşturulmuştur.</p>
                </div>""".format(ai_data['ai_insight']), unsafe_allow_html=True)
                
                # Metrik Kutuları (Zenginleştirilmiş Finansal Göstergeler)
                st.markdown("### 📈 Gerçek Zamanlı Finansal Metrikler")
                col1, col2, col3, col4 = st.columns(4)
                
                col1.metric("Son Kapanış Fiyatı", f"${prices[-1]:.2f}")
                col2.metric("Maksimum Tepe Seviyesi", f"${max(prices):.2f}")
                col3.metric("Minimum Dip Seviyesi", f"${min(prices):.2f}")
                
                # Model Güven Skoru Renklendirmesi Bilgisi
                r2_score = ai_data['model_accuracy_score'] * 100
                col4.metric("AI Model Güven Skoru (R²)", f"%{r2_score:.2f}")
                
                st.write("")
                
                # Grafik Alanı ve Açıklaması
                st.write("### 📊 Finansal Zaman Serisi ve Trend Grafiği")
                st.markdown("*Aşağıdaki grafik Geometrik Brownian Hareketi ile backend'de üretilen adımların frontend üzerinde dinamik görselleştirilmiş halidir.*")
                st.line_chart(df, height=400)
                
                # İndirme ve Ek Bilgiler Bölümü
                col_down1, col_down2 = st.columns([3, 1])
                with col_down1:
                    st.write("")
                    csv = df.to_csv().encode('utf-8')
                    st.download_button("📊 Üretilen Yapay Zeka Destekli Sentetik Veri Setini CSV Olarak İndir", csv, "synth_finance_ai_data.csv", "text/csv")
                with col_down2:
                    st.write("")
                    if volatility > 50:
                        st.warning("⚠️ Yüksek Volatilite Uyarısı: Girdiğiniz oynaklık değeri standart sapmanın çok üzerindedir. AI tahmin modellerinin sapma payı artabilir.")
                    else:
                        st.success("✅ Kararlı Piyasa Koşulu: Seçilen oynaklık düzeyi, doğrusal trend tahminleri için optimize edilmiştir.")
                
                st.write("---")
                
                # --- INTERAKTİF DÖKÜMANTASYON SEKME YAPISI (SADELİĞİ TAMAMEN YOK EDEN KISIM) ---
                st.write("### 📚 Proje Teknik Referans Modülleri")
                tab1, tab2, tab3 = st.tabs(["🔬 Matematiksel Model (GBM)", "🧠 Regresyon & AI Tahmini", "💻 Dağıtık Sistem Mimarisi"])
                
                with tab1:
                    st.markdown("""
                    #### Geometrik Brownian Hareketi (GBM) Nedir?
                    Finans matematiğinde, hisse senedi fiyatları ve döviz kurları gibi finansal zaman serilerinin rastgele yürüyüş (random walk) hareketlerini modellemek için kullanılan en yaygın **stokastik süreçtir**.
                    
                    Formül temelde iki ana bileşenden oluşur:
                    1. **Drift (Trend/Eğilim):** Verinin zamanla belirli bir yöne (örneğin yıllık %5 büyüme) doğru gitme eğilimi.
                    2. **Diffusion (Rastgele Şoklar):** Piyasadaki anlık haberler ve belirsizlikleri temsil eden, normal dağılıma sahip rastgele Wiener süreci ($dW_t$).
                    
                    Bu sayede platform, tamamen yapay ama finans dünyasının kurallarına harika uyum sağlayan veri setleri türetir.
                    """)
                    
                with tab2:
                    st.markdown("""
                    #### Lineer Regresyon Analizi Nasıl Çalışıyor?
                    Backend servisimiz veriyi ürettikten hemen sonra veri setini **Linear Regression (Doğrusal Regresyon)** makine öğrenmesi algoritmasına teslim eder.
                    * **Girdi (X):** Gün indeksleri (0, 1, 2, ... N)
                    * **Çıktı (Y):** Simülasyondan çıkan fiyat matrisi.
                    
                    Model eğitildikten sonra doğrunun eğim katsayısına bakılır. Eğer eğim pozitif yönlüyse yapay zeka **Boğa Piyasası**, negatif yönlüyse **Ayı Piyasası** içgörüsü üretir. Sağ üstte gördüğünüz **R² Skoru** ise yapay zekanın bu çizgiye ne kadar güvendiğini (verinin doğrusal hatta ne kadar yakın olduğunu) matematiksel olarak kanıtlar.
                    """)
                    
                with tab3:
                    st.markdown("""
                    #### Tech Stack ve Servis Ayrıştırması
                    Bu uygulama kurumsal mimari standartlarına tam uyumlu geliştirilmiştir:
                    * **Arkayüz (Backend):** FastAPI (Python) kullanılarak Hugging Face Spaces üzerinde Docker mimarisiyle canlıya alınmıştır.
                    * **Önyüz (Frontend):** Streamlit (Python) kullanılarak Streamlit Community Cloud üzerinde deploy edilmiştir.
                    
                    İki katman birbiriyle tamamen bağımsız olup, internet üzerinden **HTTP POST istekleri ve JSON veri paketleri** aracılığıyla haberleşmektedir. Bu sayede yarın bir gün bu uygulamaya bir mobil uygulama yazılmak istense, backend koduna hiç dokunmadan sadece yeni bir arayüz bağlanması yeterli olacaktır.
                    """)

        except requests.exceptions.ConnectionError:
            st.error("❌ Canlı Backend servisine bağlanılamadı! Lütfen Hugging Face Space sunucunuzun aktif olup olmadığını kontrol edin.")
            st.info("💡 Çözüm: Arka planda sunucunun uyku moduna geçip geçmediğini doğrulamak için Hugging Face paneline göz atabilirsiniz.")
else:
    # İlk açılışta ekranı dolduracak şık bilgilendirme panelleri
    st.info("💡 Modeli çalıştırmak, grafik analizini çizdirmek ve yapay zeka tahmin raporunu oluşturmak için sol taraftaki panelden 'Uçtan Uca Veri ve AI Analizi Üret' butonuna basınız.")
    
    # Kullanıcı ilk kez girdiğinde boş kalmasın diye alt tarafa yerleştirilen rehber adımları
    st.write("")
    st.markdown("### 🛠️ Teslimat Öncesi Adım Adım Sunum Kılavuzu")
    col_step1, col_step2, col_step3 = st.columns(3)
    col_step1.metric("1. Adım", "Parametreleri Seçin")
    col_step1.write("Sol panelden projenize özel başlangıç fiyatı, oynaklık ve simüle edilecek gün sayısını kendi isteğinize göre özelleştirin.")
    
    col_step2.metric("2. Adım", "AI Motorunu Tetikleyin")
    col_step2.write("Mavi butona basarak arayüzün canlı FastAPI sunucusuna bağlanmasını sağlayın ve otomatik AI raporunun gelmesini bekleyin.")
    
    col_step3.metric("3. Adım", "Dökümanları İnceleyin")
    col_step3.write("Grafiğin hemen altında belirecek olan interaktif sekmelerden (Tabs) projenin matematiksel ve teknik detaylarını hocalarınıza sunun.")
