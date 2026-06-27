#Calculadora de FIIs — Dividend Yield (DY) e Preço sobre Valor Patrimonial (P/VP)

import sys


def calcular_dy(dividendo_anual: float, preco_cota: float):
    return (dividendo_anual / preco_cota) * 100


def calcular_pvp(preco_cota: float, valor_patrimonial: float):
    return preco_cota / valor_patrimonial


def formatar_numero(valor: float):
    return str(int(valor)) if valor.is_integer() else str(valor)
#Exibe inteiro se não tiver casas decimais.


def exibir_resultado_dy(dy: float):
    dy_fmt = formatar_numero(dy)

    print(f"O Dividend Yield (DY) é de {dy_fmt}%\n")

    if 8 <= dy <= 12:
        print("Está dentro do esperado (8% a 12%)")
    else:
        print("Está fora do esperado (8% a 12%)")


def exibir_resultado_pvp(pvp: float):

    print(f"\nO P/VP é de {pvp:.2f}")

    if pvp < 1:
        print("A cota está 'barata' em relação ao patrimônio")
    elif pvp > 1:
        print("A cota está 'cara'")
    else:
        print("O preço está justo")




#Exibição principal

def main():
    print("\n--- Cálculo do Dividend Yield (DY) ---")

    da = float(input("Digite o valor do dividendo anual (DA): "))
    pc = float(input("Digite o preço atual da cota (PC): "))

    dy = calcular_dy(da, pc)
    exibir_resultado_dy(dy)

    continuar = input("\nDeseja calcular o P/VP também? (s/n): ").lower()

    if continuar == "s":
        print("\n--- Cálculo do Preço sobre Valor Patrimonial (P/VP) ---")
        vp = float(input("Digite o valor patrimonial (VP): "))
        pvp = calcular_pvp(pc, vp)
        exibir_resultado_pvp(pvp)
    else:
        sys.exit()


main()
