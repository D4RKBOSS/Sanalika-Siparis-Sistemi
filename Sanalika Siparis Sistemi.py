import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "menu.json"

default_menu = {
    "Americano": ["Kahve"],
    "Ayran": ["Su", "Yoğurt"],
    "Balık ekmek": ["Balık", "Ekmek", "Soğan"],
    "Balıklı Salata": ["Balık", "Domates", "Marul", "Zeytin-Yağı"],
    "Cheese Burger": ["Peynir", "Burger-Ekmek", "Burger-Köfte"],
    "Cacıklı Arap Köftesi": ["Yoğurt", "Kıyma", "Bulgur", "Zeytin-Yağı", "Un"],
    "Cappucino": ["Cappucino"],
    "Çay": ["Çay"],
    "Çikolatalı Donut": ["Hamur", "Yumurta", "Çikolata"],
    "Çilekli Dondurma": ["Çilek", "Sade-Dondurma"],
    "Çikolatalı Milkshake": ["Buz", "Buz", "Buz", "Buz", "Süt", "Çikolata", "Krema"],
    "Falafel": ["Zeytin-Yağı", "Hamur", "Soğan", "Soğan", "Maydanoz", "Nohut"],
    "Gözleme": ["Hamur", "Peynir", "Maydanoz"],
    "Humus": ["Nohut", "Limon", "Su", "Tahin"],
    "Hamburger": ["Domates", "Burger-Ekmek", "Burger-Köfte"],
    "Izgara Balık": ["Balık", "Soğan", "Zeytin-Yağı"],
    "Izgara Biftek": ["Biftek", "Patates", "Zeytin-Yağı"],
    "İtalyan Pizza": ["Hamur", "Peynir", "Biber"],
    "Karpuz Peynir": ["Beyaz-Peynir", "Karpuz"],
    "Kase Pilav": ["Pirinç", "Su", "Zeytin-Yağı"],
    "Kavurmalı Pilav": ["Pirinç", "Biftek", "Su"],
    "Karışık Pizza": ["Hamur", "Peynir", "Sucuk"],
    "Kaşarlı Pide": ["Peynir", "Hamur"],
    "Kapta Dondurma": ["Süt", "Krema", "Krema", "Şeker", "Çikolata", "Çilek"],
    "Kavunda Dondurma": ["Karadut", "Sade-Dondurma", "Şeftali", "Kavun"],
    "Kremalı Filtre Kahve": ["Kahve-Kreması", "Filtre-Kahve"],
    "Lokma": ["Un", "Şeker", "Su", "Maya"],
    "Limonata": ["Buz", "Buz", "Şeker", "Nane", "Nane", "Limon"],
    "Menemen": ["Yumurta", "Zeytin-Yağı", "Domates", "Biber"],
    "Midye": ["Kabuklu Midye", "Kabuklu Midye", "Zeytin-Yağı", "Limon", "Pirinç", "Su"],
    "Meyve Suyu": ["Su", "Karadut", "Buz", "Çilek"],
    "Meyve Suyu Kokteyli": ["Su", "Karadut", "Buz", "Çilek"],
    "Patates Kızartması": ["Patates"],
    "Patlamış Mısır": ["Mısır", "Zeytin-Yağı"],
    "Peynirli Pizza": ["Hamur", "Peynir", "Domates"],
    "Piskevit Arası Marshmellow": ["Şeker", "Süt", "Krema", "Çikolata"],
    "Sucuk Ekmek": ["Sucuk", "Sucuk", "Ekmek"],
    "Sucuklu Pide": ["Sucuk", "Hamur"],
    "Sushi": ["Pirinç", "Su", "Balık"],
    "Sütlaç": ["Pirinç", "Şeker", "Süt"],
    "Sütlü Kahve": ["Süt", "Kahve"],
    "Şam Tatlısı": ["Yoğurt", "Şeker", "Fıstık", "İrmik"],
    "Tavuk Şiş": ["Tavuk-Eti", "Pirinç", "Biber", "Zeytin-Yağı"],
    "Tavuklu Salata": ["Tavuk-Eti", "Domates", "Marul", "Maydanoz"]
}

def menu_yukle():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return default_menu.copy()

def menu_kaydet():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(menu, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("Kaydedildi", "Menü başarıyla kaydedildi.")

menu = menu_yukle()
siparis = []
urun_sayaci = {}

def siparise_ekle(urun):
    siparis.extend(menu[urun])
    urun_sayaci[urun] = urun_sayaci.get(urun, 0) + 1
    guncelle_malzeme_listesi()
    guncelle_urun_listesi()

def siparisi_temizle():
    siparis.clear()
    urun_sayaci.clear()
    text_malzemeler.delete("1.0", tk.END)
    text_urunler.delete("1.0", tk.END)
    messagebox.showinfo("Temizlendi", "Sipariş listesi temizlendi.")

def guncelle_malzeme_listesi():
    text_malzemeler.delete("1.0", tk.END)
    malzeme_sayaci = {}
    for m in siparis:
        malzeme_sayaci[m] = malzeme_sayaci.get(m, 0) + 1
    for m, adet in malzeme_sayaci.items():
        text_malzemeler.insert(tk.END, f"{adet} adet {m}\n")

def guncelle_urun_listesi():
    text_urunler.delete("1.0", tk.END)
    for urun, adet in urun_sayaci.items():
        text_urunler.insert(tk.END, f"{adet}x {urun} → {', '.join(menu[urun])}\n")

def urun_ekle():
    urun_adi = entry_urun.get().strip()
    malzemeler = entry_malzeme.get().strip()
    if urun_adi and malzemeler:
        if urun_adi in menu:
            messagebox.showwarning("Uyarı", f"{urun_adi} zaten mevcut.")
            return
        malzeme_listesi = [m.strip() for m in malzemeler.split(",")]
        menu[urun_adi] = malzeme_listesi
        entry_urun.delete(0, tk.END)
        entry_malzeme.delete(0, tk.END)
        guncelle_siparis_butonu()
        messagebox.showinfo("Eklendi", f"{urun_adi} eklendi.")
    else:
        messagebox.showwarning("Eksik", "Ürün adı ve malzeme giriniz.")

def urun_sil():
    urun_adi = entry_urun.get().strip()
    if urun_adi in menu:
        del menu[urun_adi]
        entry_urun.delete(0, tk.END)
        guncelle_siparis_butonu()
        messagebox.showinfo("Silindi", f"{urun_adi} silindi.")
    else:
        messagebox.showwarning("Bulunamadı", f"{urun_adi} bulunamadı.")

def guncelle_siparis_butonu():
    for widget in urun_button_frame.winfo_children():
        widget.destroy()
    sutun_sayisi = 8
    for i, urun in enumerate(menu.keys()):
        satir = i // sutun_sayisi
        sutun = i % sutun_sayisi
        tk.Button(
            urun_button_frame, text=urun, width=21,
            command=lambda u=urun: siparise_ekle(u)
        ).grid(row=satir, column=sutun, padx=3, pady=3)

    for i in range((len(menu) // sutun_sayisi) + 1):
        urun_button_frame.grid_rowconfigure(i, weight=1)
    for j in range(sutun_sayisi):
        urun_button_frame.grid_columnconfigure(j, weight=1)

root = tk.Tk()
root.title("Sanalika Sipariş Sistemi")
root.geometry("1200x700")
root.iconbitmap("siparis.ico")


root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

urun_button_frame = tk.Frame(root)
urun_button_frame.grid(row=0, column=0, columnspan=2, pady=10)

center_frame = tk.Frame(root)
center_frame.grid(row=1, column=0, sticky="n", pady=20)

icerik_wrapper = tk.Frame(center_frame)
icerik_wrapper.pack()

urun_ozet_frame = tk.Frame(icerik_wrapper)
urun_ozet_frame.pack(side=tk.LEFT, padx=(0, 5))

tk.Label(urun_ozet_frame, text="Seçilen Ürünler", font=("Arial", 12, "bold")).pack()
text_urunler = tk.Text(urun_ozet_frame, width=60, height=30, bg="#f8f8f8", font=("Arial", 10, "bold"))
text_urunler.pack()

malzeme_frame = tk.Frame(icerik_wrapper)
malzeme_frame.pack(side=tk.LEFT, padx=(5, 0))

tk.Label(malzeme_frame, text="Toplam Malzemeler", font=("Arial", 12, "bold")).pack()
text_malzemeler = tk.Text(malzeme_frame, width=60, height=30, bg="#f4f4f4", font=("Arial", 10, "bold"))
text_malzemeler.pack()

admin_frame = tk.Frame(root, bd=2, relief="ridge", width=200, height=550)
admin_frame.grid(row=1, column=1, rowspan=2, sticky="ne", padx=10, pady=20)
admin_frame.pack_propagate(False)
tk.Label(admin_frame, text="Admin Paneli", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(admin_frame, text="Ürün Adı:").pack()
entry_urun = tk.Entry(admin_frame, width=30)
entry_urun.pack(pady=2)

tk.Label(admin_frame, text="Malzemeler (virgülle ayır):").pack()
tk.Label(admin_frame, text="Örnek: Domates, Peynir, Zeytin").pack()
entry_malzeme = tk.Entry(admin_frame, width=30)
entry_malzeme.pack(pady=2)

tk.Button(admin_frame, text="Ürün Ekle", command=urun_ekle, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold")).pack(pady=5)
tk.Button(admin_frame, text="Ürün Sil", command=urun_sil, bg="#F44336", fg="#FFFFFF", font=("Arial", 10, "bold")).pack(pady=5)
tk.Button(admin_frame, text="Kaydet", command=menu_kaydet, bg="#2196F3", fg="#FFFFFF", font=("Arial", 10, "bold")).pack(pady=5)
tk.Button(admin_frame, text="Siparişi Temizle", command=siparisi_temizle, bg="#FF9800", fg="#FFFFFF", font=("Arial", 10, "bold")).pack(pady=5)

guncelle_siparis_butonu()
root.mainloop()
