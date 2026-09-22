def converter_e_dividir(valor, divisor):
    try:
        resultado = float(valor) / divisor
        print(f"Resultado: {resultado}")
    except ValueError:
        print("O valor informado não é um número válido.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")

converter_e_dividir("10", 2)
converter_e_dividir("abc", 2)
converter_e_dividir("10", 0)