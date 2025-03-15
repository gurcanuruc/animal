
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Adım: Verileri Hazırlama (Örnek veri seti)
data = {
    'Metrekare': [100, 150, 200, 80, 120, 180, 140],
    'Oda Sayısı': [3, 4, 5, 2, 3, 4, 3],
    'Bina Yaşı': [10, 5, 2, 20, 15, 7, 12],  # Bina yaşı
    'Konum': ['Merkez', 'Merkez', 'Banliyö', 'Banliyö', 'Kırsal', 'Merkez', 'Kırsal'],  # Konum
    'Fiyat': [300000, 450000, 600000, 250000, 350000, 540000, 400000]
}

# Veri çerçevesi oluşturma
df = pd.DataFrame(data)

# 2. Adım: Kategorik veriyi sayısal veriye dönüştürme (Konum)
le = LabelEncoder()
df['Konum'] = le.fit_transform(df['Konum'])

# 3. Adım: Özellikler ve hedef değişkeni ayırma
X = df[['Metrekare', 'Oda Sayısı', 'Bina Yaşı', 'Konum']]  # Giriş değişkenleri
y = df['Fiyat']  # Hedef değişken (Fiyat)

# 4. Adım: Eğitim ve test verilerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Adım: Doğrusal Regresyon Modeli Oluşturma
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Adım: Test verisi ile tahmin yapma
y_pred = model.predict(X_test)

# 7. Adım: Modelin başarı değerlendirmesini yapma
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Sonuçları yazdırma
print(f"Ortalama Kare Hatası (MSE): {mse}")
print(f"R-Kare Skoru (R²): {r2}")

# 8. Adım: Kullanıcıdan veri alarak tahmin yapma
metrekare = float(input("Evin metrekare bilgisini girin: "))
oda_sayisi = int(input("Evin oda sayısını girin: "))
bina_yasi = int(input("Evin bina yaşını girin: "))
konum = input("Evin konumunu girin (Merkez, Banliyö, Kırsal): ")

# Konumu sayısal hale getirme
konum_sayisal = le.transform([konum])[0]

# Kullanıcıdan alınan veriyi DataFrame formatında hazırlayalım
tahmin_verisi = pd.DataFrame([[metrekare, oda_sayisi, bina_yasi, konum_sayisal]],
                              columns=['Metrekare', 'Oda Sayısı', 'Bina Yaşı', 'Konum'])

# Kullanıcıdan alınan veriyi modele verip tahmin yapma
tahmin_fiyat = model.predict(tahmin_verisi)

# Sonuç
print(f"Ev için tahmin edilen fiyat: {tahmin_fiyat[0]:,.2f} TL")