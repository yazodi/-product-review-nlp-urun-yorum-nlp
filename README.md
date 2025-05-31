# 🛍️ Ürün Yorumu Analizi (Kategori Tahmini + Anahtar Kelime Çıkarımı)

Bu proje, e-ticaret platformlarına yazılan ürün yorumlarından:

- ✅ Ürünün ait olduğu **kategori**yi tahmin eder  
- ✅ Yorum içerisindeki **anahtar kelimeleri** çıkartır  

---

## 🔍 Örnek Kullanım

Yorum:
> Klavye çok kaliteli, RGB ışıkları mükemmel.

Çıktı:
- **Kategori:** bilgisayar  
- **Anahtar Kelimeler:** "RGB ışıkları", "klavye", "kaliteli"

---

## 📂 Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `app.py` | Streamlit arayüz dosyası |
| `e_ticaret_yorumlari_1000.csv` | Eğitim için kullanılan yorum ve kategori verileri |
| `kategori_tahmin_model.pkl` | Eğitilmiş LogisticRegression model dosyası |
| `tfidf_vectorizer.pkl` | TF-IDF vektörizer nesnesi |
| `README.md` | Proje açıklaması |

---

## 🧠 Kullanılan Teknolojiler

- Python (pandas, sklearn, pickle, yake, streamlit)
- TF-IDF + LogisticRegression
- YAKE anahtar kelime çıkarımı
- Streamlit arayüzü

---

## 🚀 Streamlit ile Çalıştırmak İçin

```bash
pip install -r requirements.txt
streamlit run app.py


🛠️ Geliştirilebilir Alanlar
Daha büyük ve gerçek verilerle yeniden eğitim

Türkçe BERT gibi transformer tabanlı modellerle entegrasyon

Anahtar kelime çıkarımı için KeyBERT gibi gelişmiş yöntemler

Duygu analizi (Sentiment Analysis) eklenmesi

Çok dilli destek


📜 Lisans
MIT License – Açık kaynaklı ve özgürce geliştirilebilir.