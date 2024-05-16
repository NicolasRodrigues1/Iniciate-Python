soma = 0

x = int(input("Digite o primeiro numero: "))

while x != 0:
    soma = soma + x
    x = int(input("Digite outro número: "))

print(f"SOMA = {soma}")