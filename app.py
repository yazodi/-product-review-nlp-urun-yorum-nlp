import streamlit as st
import pandas as pd
import pickle
import yake
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 🔃 Eğitimli model ve TF-IDF yükleme (senin eğittiğin modeli kaydettiysen kullanabilirsin)
# Bu örnek içinde yeniden eğitiyoruz (demo amaçlı)
df = pd.read_csv("e_ticaret_yorumlari_1000.csv")

# TF-IDF ve model
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['review'])
y = df['category']
model = LogisticRegression()
model.fit(X, y)

# Anahtar kelime çıkarım fonksiyonu
def extract_keywords(text, max_keywords=3):
    kw_extractor = yake.KeywordExtractor(lan="tr", top=max_keywords)
    keywords = kw_extractor.extract_keywords(text)
    return [kw for kw, _ in keywords]

# Kategori tahmini fonksiyonu
def predict_category_and_keywords(text):
    tfidf_vector = tfidf.transform([text])
    category = model.predict(tfidf_vector)[0]
    keywords = extract_keywords(text)
    return category, keywords

# 🎨 Streamlit Arayüzü
st.title("🛍️ Ürün Yorumu Analizi")
st.write("Bu uygulama, bir ürün yorumundan anahtar kelimeleri çıkarır ve hangi kategoriye ait olduğunu tahmin eder.")

yorum = st.text_area("Yorumunuzu yazın:", "Klavye çok kaliteli, RGB ışıkları mükemmel.")

if st.button("Analiz Et"):
    kategori, anahtar_kelimeler = predict_category_and_keywords(yorum)
    st.success(f"Tahmin Edilen Kategori: {kategori}")
    st.info(f"Anahtar Kelimeler: {', '.join(anahtar_kelimeler)}")
