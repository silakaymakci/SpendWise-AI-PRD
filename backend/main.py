from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Veri modeli (Frontend'den gelecek istek yapısı)
class SimulationParams(BaseModel):
    start_price: float
    volatility: float
    days: int

# Matematiksel Motor: Geometrik Brownian Hareketi (GBM)
def generate_gbm(s0, vol, days):
    dt = 1/365  # Günlük zaman adımı
    mu = 0.05   # Yıllık beklenen getiri (varsayılan %5)
    
    # Günlük getirileri hesapla
    returns = np.exp((mu - 0.5 * vol**2) * dt + vol * np.sqrt(dt) * np.random.standard_normal(days))
    
    # Fiyat serisini oluştur (S0 * kumülatif çarpım)
    price_path = s0 * np.cumprod(returns)
    return price_path.tolist()

@app.get("/")
def read_root():
    return {"message": "SynthFinance AI Backend Servisi Çalışıyor!"}

@app.post("/generate-data")
def get_simulation(params: SimulationParams):
    # Frontend'den gelen parametrelerle veriyi üret
    prices = generate_gbm(params.start_price, params.volatility/100, params.days)
    
    return {
        "status": "success",
        "data": prices
    }
