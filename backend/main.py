from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression

app = FastAPI()

class SimulationParams(BaseModel):
    start_price: float
    volatility: float
    days: int

# Matematiksel Motor (GBM)
def generate_gbm(s0, vol, days):
    dt = 1/365
    mu = 0.05
    returns = np.exp((mu - 0.5 * vol**2) * dt + vol * np.sqrt(dt) * np.random.standard_normal(days))
    price_path = s0 * np.cumprod(returns)
    return price_path.tolist()

# Yapay Zeka Motoru: Trend Analizi ve Gelecek Tahmini
def analyze_with_ai(prices):
    days = len(prices)
    X = np.array(range(days)).reshape(-1, 1) # Günler (0, 1, 2...)
    y = np.array(prices) # Fiyatlar

    # AI Modelinin Eğitilmesi (Makine Öğrenmesi Regresyonu)
    model = LinearRegression()
    model.fit(X, y)
    
    # Gelecek 10 gün için tahmin yapay zeka tarafından yapılıyor
    future_days = np.array(range(days, days + 10)).reshape(-1, 1)
    ai_predictions = model.predict(future_days).tolist()
    
    # Modelin eğiminden trend yönünü bulma (AI İçgörüsü)
    slope = model.coef_[0]
    if slope > 0.1:
        ai_insight = "Güçlü Yükseliş Trendi (Boğa Piyasası Yapısı). Risk iştahı yüksek tutulabilir."
    elif slope < -0.1:
        ai_insight = "Düşüş Trendi Sinyali (Ayı Piyasası Yapısı). Risk azaltılmalı, korumacı pozisyon alınmalı."
    else:
        ai_insight = "Yatay ve Kararsız Piyasa Yapısı. Ani volatilite kırılımlarına karşı dikkatli olunmalı."
        
    return {
        "ai_predictions": ai_predictions,
        "ai_insight": ai_insight,
        "model_accuracy_score": float(model.score(X, y)) # R^2 skoru ile yapay zekanın veriye uyumu
    }

@app.get("/")
def read_root():
    return {"message": "SynthFinance AI - Canlı Yapay Zeka Backend Servisi Aktif!"}

@app.post("/generate-data")
def get_simulation(params: SimulationParams):
    # 1. Matematiksel olarak veriyi üret
    prices = generate_gbm(params.start_price, params.volatility/100, params.days)
    
    # 2. Üretilen veriyi Yapay Zeka modeline sokup analiz et
    ai_results = analyze_with_ai(prices)
    
    return {
        "status": "success",
        "data": prices,
        "ai_analysis": ai_results
    }
