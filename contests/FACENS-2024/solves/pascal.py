def combina(n, k):
    # Cálculo de combinação sem usar math.comb para compatibilidade
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    resultado = 1
    for i in range(1, k+1):
        resultado = resultado * (n - i + 1) // i
    return resultado

def gera_triangulo_pascal(n):
    triangulo = []
    for i in range(n):
        linha = [combina(i, k) for k in range(i+1)]
        triangulo.append(linha)
    return triangulo

def imprime_saida(triangulo):
    for i, linha in enumerate(triangulo):
        # Imprime os coeficientes
        coef_str = ' '.join(str(x) for x in linha)
        # Monta polinômio
        termos = []
        grau = i
        for k, coef in enumerate(linha):
            # coef * A^(grau-k) * B^(k)
            termos.append(f"{coef}*(A^{grau-k}*B^{k})")
        polinomio = ' + '.join(termos)
        print(f"{coef_str} => {polinomio}")

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        if not (1 <= n <= 15):
            continue

        triangulo = gera_triangulo_pascal(n)
        imprime_saida(triangulo)

if __name__ == "__main__":
    main()
