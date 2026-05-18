import random

secenekler = ["taş", "kağıt", "makas"]
kazan = {"taş": "makas", "kağıt": "taş", "makas": "kağıt"}
skor = [0, 0]  # [oyuncu, bilgisayar]

print("=== Taş Kağıt Makas ===")

while True:
    oyuncu = input("\nSeçin (taş/kağıt/makas veya q=çıkış): ").lower()

    if oyuncu == "q":
        print(f"\nSon skor → Sen: {skor[0]}  Bilgisayar: {skor[1]}")
        break

    if oyuncu not in secenekler:
        print("Geçersiz seçim!")
        continue

    bilgisayar = random.choice(secenekler)
    print(f"Bilgisayar: {bilgisayar}")

    if oyuncu == bilgisayar:
        print("Berabere!")
    elif kazan[oyuncu] == bilgisayar:
        print("Kazandın! ")
        skor[0] += 1
    else:
        print("Kaybettin! ")
        skor[1] 
