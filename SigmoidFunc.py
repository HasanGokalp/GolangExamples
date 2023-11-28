import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def tahmin_et(alisveris_gecmisi, web_suresi, tiklama_gecmisi, kampanya_tepkisi, mevsim_faktoru):
    aktivasyon = (
        0.1 * alisveris_gecmisi +
        0.2 * web_suresi +
        0.3 * tiklama_gecmisi +
        0.1 * kampanya_tepkisi +
        0.3 * mevsim_faktoru
    )
    
    normalized_aktivasyon = sigmoid(aktivasyon)
    
    if normalized_aktivasyon > 0.7:
        return "Kullanıcı muhtemelen ürünü satın alacak."
    else:
        return "Kullanıcı muhtemelen ürünü satın almayacak."

# Örnek kullanım
alisveris_gecmisi = 10
web_suresi = 30
tiklama_gecmisi = 5
kampanya_tepkisi = 0.8
mevsim_faktoru = 0.6

tahmin = tahmin_et(alisveris_gecmisi, web_suresi, tiklama_gecmisi, kampanya_tepkisi, mevsim_faktoru)
print(tahmin)