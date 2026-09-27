# Dispositivo de Briot-Ruffini em Python

Uma implementação simples, clara e interativa em Python do **Dispositivo de Briot-Ruffini**, um método prático da álgebra para dividir um polinômio $P(x)$ por um binômio do primeiro grau no formato $(x - a)$.

---

## 🚀 Funcionalidades

- **Interativo:** Solicita o grau do polinômio, seus coeficientes e o divisor diretamente no terminal.
- **Entrada amigável:** Exibe claramente qual termo de $x^n$ está sendo preenchido no momento.
- **Cálculo automático:** Aplica a regra de Briot-Ruffini para gerar os coeficientes do quociente $Q(x)$ e o resto $R$.

---

## 🛠️ Como Executar

1. **Certifique-se de ter o Python instalado** (versão 3.6 ou superior).
2. **Clone o repositório:**
   ```bash
   git clone [https://github.com/MeiaDois20/Dispositivo-de-Briot-Ruffini.git](https://github.com/MeiaDois20/Dispositivo-de-Briot-Ruffini.git)

   ## 💻 Exemplo de Uso

Ao executar o script com o exemplo **P(x) = 2x³ - 3x² + 4x - 5** e divisor **(x - 2)**:

```text
Digite o grau da equação polinomial: 3
Digite o coeficiente de x^3: 2
Digite o coeficiente de x^2: -3
Digite o coeficiente de x^1: 4
Digite o coeficiente de x^0: -5
Sua lista de coeficientes: [2.0, -3.0, 4.0, -5.0]

Digite o termo independente do divisor (ex: -2 para x - 2): -2
A raiz do divisor é: 2.0

Os coeficientes do quociente são: [2.0, 1.0, 6.0]
O resto da divisão é: 7.0
```

## 📝 Licença
**Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar!**
