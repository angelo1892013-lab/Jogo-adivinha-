
import random

numero = random.randint(1, 10)

tentativa = int(input("Adivinha o número (1 a 10): "))

if tentativa == numero:
    print("Acertaste!")
elif tentativa < numero:
    print("Muito baixo!")
else:
    print("Muito alto!")

print("O número era:", numero)
