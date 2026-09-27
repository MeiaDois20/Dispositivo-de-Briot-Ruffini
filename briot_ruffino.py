grauDoPolinomio = int(input("Digite o grau da equação polinomial: "))
print()

coeficientes = []

for i in range(0, grauDoPolinomio + 1):
    numero = float(input(f"Digite o coeficiente de x^{grauDoPolinomio - i}: "))
    coeficientes.append(numero)
print()

print("Sua lista de coeficientes:", coeficientes)
print()

termo_binomio = float(input("Digite o termo independente do divisor (ex: -2 para x - 2): "))
raiz = -termo_binomio
print("A raiz do divisor é:", raiz)

resultado = [coeficientes[0]]

for i in range(0, grauDoPolinomio):
    resultado.append(coeficientes[i+ 1] + resultado[i] * raiz)
print()

print("Os coeficientes do quociente são:", resultado[:-1])
print("O resto da divisão é:", resultado[-1])