import requests
import json
import os

API_KEY = 'ce1d5a7e0fdf1ed4b76a7650207c58cd'
AIRPORT_IATA = 'ADB'

def get_flights():
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&dep_iata={AIRPORT_IATA}"
    
    try:
        response = requests.get(url)
        # Yanıt başarılıysa json olarak kaydet
        if response.status_code == 200:
            data = response.json()
            with open('flights.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("Veriler başarıyla çekildi ve flights.json dosyasına kaydedildi.")
        else:
            print(f"API Hatası: {response.status_code}")
    except Exception as e:
         print(f"Bağlantı hatası: {e}")

if __name__ == "__main__":
    get_flights()
                                 
