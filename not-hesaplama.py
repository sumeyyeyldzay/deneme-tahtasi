# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:56:33 2026

@author: user
"""

import tkinter as tk
from tkinter import messagebox


def hesapla():
  try:
    vize = float(vize_entry.get())
    final = float(final_entry.get())

    # Ortalama hesaplama (%40 vize, %60 final)
    ortalama = (vize * 0.4) + (final * 0.6)

    sonuc_label.config(text=f"Ortalamanız: {ortalama:.2f}")

    if ortalama >= 50:
      durum_label.config(text="Durum: Geçti Harika! 🎉", fg="green")
    else:
      durum_label.config(text="Durum: Kaldı 😢", fg="red")

  except ValueError:
    messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")


# Ana pencere
pencere = tk.Tk()
pencere.title("Not Hesaplama Aracı")
pencere.geometry("300x300")

# Vize Girişi
tk.Label(pencere, text="Vize Notu:").pack(pady=5)
vize_entry = tk.Entry(pencere)
vize_entry.pack(pady=5)

# Final Girişi
tk.Label(pencere, text="Final Notu:").pack(pady=5)
final_entry = tk.Entry(pencere)
final_entry.pack(pady=5)

# Hesapla Butonu
hesapla_btn = tk.Button(
    pencere, text="Hesapla", command=hesapla, bg="lightblue"
)
hesapla_btn.pack(pady=10)

# Sonuç Ekranları
sonuc_label = tk.Label(pencere, text="Ortalamanız: ", font=("Arial", 10, "bold"))
sonuc_label.pack(pady=5)

durum_label = tk.Label(pencere, text="", font=("Arial", 10, "bold"))
durum_label.pack(pady=5)

pencere.mainloop()