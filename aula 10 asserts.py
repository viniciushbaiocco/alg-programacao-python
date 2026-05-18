def calcular_progressao(a1, r, n):
    if a1 is None or r is None or n is None:
        return None
    if a1 == 0 or n == 0:
        return 0
    if r == 1:
        return a1 * n
    return a1 * (r**n - 1) / (r - 1)


def test__pg():
    assert calcular_progressao(a1=1, r=2, n=1) == 1
    assert calcular_progressao(a1=2, r=0, n=1) == 2
    assert calcular_progressao(a1=0, r=1, n=1) == 0
    assert calcular_progressao(a1=0, r=0, n=1) == 0
    assert calcular_progressao(a1=1, r=2, n=0) == 0
    assert calcular_progressao(a1=None, r=None, n=None) is None


test__pg()
print("Todos os testes passaram!")

a1 = float(input("Digite a1 (primeiro termo): "))
r = float(input("Digite r (razão): "))
n = int(input("Digite n (número de termos): "))

resultado = calcular_progressao(a1, r, n)
print(f"Soma da PG: {resultado}")
