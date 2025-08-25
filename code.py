def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Por favor escribe un número.")

def main():
    operaciones = {
        '+': sumar,
        '-': restar,
        '*': multiplicar,
        '/': dividir
    }

    print("=== Calculadora en Python ===")
    print('Escribe "salir" para terminar.')

    while True:
        op = input("Operación (+, -, *, /): ").strip()
        if op.lower() == "salir":
            print("¡Hasta pronto!")
            break

        if op not in operaciones:
            print("❌ Operación no válida")
            continue

        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        resultado = operaciones[op](a, b)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    if cmd == "add": add(" ".join(args))
    elif cmd == "ls": ls()
    elif cmd == "done": done(int(args[0])) # pyright: ignore[reportShadowedImports]