n = int(input("Quantos números serão digitados: "))

soma = 0 
for i in range (0, n):
    x = int(input("Digite outro número: "))
    soma = soma + x
    
print(f"SOMA = {soma}")