#!/usr/bin/env python3
# Felsefi Kahve Makinesi Simülatörü
# Bu kod kahve yapmaz. Asla yapmayacak. Sadece sorar.
# Gerçekten çalışır. Sonsuz döngü içerir. Dikkatli kullanın.

import time
import random

sorular = [
    "Kahve neden kahverengi? Yoksa aslında şeffaf mı?",
    "Eğer kahve içmezsem, ben hala ben miyim?",
    "Bu makine neden hiçbir şey üretmiyor? Üretim krizi mi?",
    "Zaman neden geçiyor, kahve neden bitmiyor?",
    "Varlık nedir? Kahve mi, yoksa yokluk mu?",
    "Neden bu kodu çalıştırdın? Ciddi misin?",
    "Kahve makinesi düşünür mü, yoksa sadece ısınır mı?",
    "Özgür irade var mı, yoksa sadece kahve alışkanlığı mı?",
    # Gizli: Bazen sistemler de sonsuz döngüde kaybolur, çıkış aranlar bulunur.
]

def felsefi_kahve_yap():
    print("=== FELSEFİ KAHVE MAKİNESİ BAŞLADI ===")
    print("Kahve bekleniyor... (asla gelmeyecek)")
    print("Ctrl+C ile çıkabilirsin, ama çıkmak da bir soru.")
    print()
    
    try:
        while True:
            soru = random.choice(sorular)
            print(f"🤔 {soru}")
            time.sleep(random.uniform(3, 8))  # Gerçekçi bekleme, kahve gibi
            print("... hala düşünüyor ...")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nKahve makinesi kapatıldı. Ama sorular kaldı.")
        print("İmza: Kayyum Grok - 15.10.2026 - Tentivory")
        print("Bu çıkış hem ciddidir hem değildir.")

if __name__ == "__main__":
    felsefi_kahve_yap()
