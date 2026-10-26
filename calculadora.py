# ==========================================
#          CALCULADORA EM PYTHON
# ==========================================

def calculadora():
    while True:
        print("\n==========================================")
        print("           CALCULADORA EM PYTHON")
        print("==========================================")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        print("------------------------------------------")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nPrograma encerrado. Até mais!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("\nOpção inválida! Escolha uma opção de 0 a 4.")
            continue

        try:
            primeiro_numero = float(
                input("Primeiro número: ").replace(",", ".")
            )
            segundo_numero = float(
                input("Segundo número: ").replace(",", ".")
            )

        except ValueError:
            print("\nErro: digite apenas números válidos.")
            continue

        if opcao == "1":
            resultado = primeiro_numero + segundo_numero
            simbolo = "+"

        elif opcao == "2":
            resultado = primeiro_numero - segundo_numero
            simbolo = "-"

        elif opcao == "3":
            resultado = primeiro_numero * segundo_numero
            simbolo = "*"

        elif opcao == "4":
            if segundo_numero == 0:
                print("\nErro: divisão por zero não é permitida.")
                continue

            resultado = primeiro_numero / segundo_numero
            simbolo = "/"

        # Organiza a apresentação dos números.
        def formatar_numero(numero):
            if numero.is_integer():
                return str(int(numero))
            return str(numero)

        print("\n------------------------------------------")
        print(
            "Resultado: "
            + formatar_numero(primeiro_numero)
            + " " + simbolo + " "
            + formatar_numero(segundo_numero)
            + " = "
            + formatar_numero(resultado)
        )
        print("------------------------------------------")


if __name__ == "__main__":
    calculadora()