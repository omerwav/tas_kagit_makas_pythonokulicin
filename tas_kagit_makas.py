#ÖNEMLİ BU KOD TAMAMEN EĞLENCE AMACLI YAZILMIŞTIR PRINT UZERINDEN YAZDIKLARIM CIDDIYE ALINMASIN TAMAMEN HEPSI IRONI ICINDIR.
import random


CHOICES = ["taş", "kağıt", "makas"]
WINS = {"taş": "makas", "kağıt": "taş", "makas": "kağıt"}

def play_game():
    score = [0, 0]  # [player, computer]
    
    print("ECURIN BABA PRO TAS KAGIT MAKAS")

    while True:
        player = input("\nSeçin (taş/kağıt/makas veya q=çıkış): ").lower().strip()
        
        if player == "q":
            print(f"\nSon skor → Sen: {score[0]}  Bilgisayar: {score[1]}")
            break
        
        if player not in CHOICES:
            print("taş, kağıt veya makas yazacan mal.")
            continue
        
        computer = random.choice(CHOICES)
        print(f"Bilgisayar: {computer}")
        
        if player == computer:
            print("Berabere!")
        elif WINS[player] == computer:
            print("Afferin lan salak ecurin. ")
            score[0] += 1
        else:
            print("HAHAHAHA kaybetti mal. ")
            score[1] += 1
        
        print(f"Skor: Sen {score[0]} - {score[1]} Bilgisayar")

if __name__ == "__main__":
    play_game()
