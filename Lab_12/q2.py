def somar_valores(a, b):
    try:
        return a + b
    except TypeError:
        return "nao tem como somar isso ai."

print(somar_valores(5, 3))
print(somar_valores(5, "TRES"))