# Ejercicio: Control Nutricional de Jugadores de Fútbol

def registrar_jugadores():
    jugadores = []
    print("Registro de 11 jugadores:")
    for i in range(11):
        print(f"\nJugador {i+1}:")
        rut = input("RUT: ")
        nombre = input("Nombre: ")
        try:
            peso = float(input("Peso (kg): "))
            estatura = float(input("Estatura (m): "))
        except ValueError:
            print("Error: Debe ingresar números válidos para peso y estatura.")
            continue
        print("Posición: 1) Delantero 2) Defensa 3) Medio Campo 4) Arquero")
        pos_op = input("Ingrese opción: ")
        posiciones = {"1": "Delantero", "2": "Defensa", "3": "Medio Campo", "4": "Arquero"}
        posicion = posiciones.get(pos_op, "Desconocido")
        jugador = {
            "rut": rut,
            "nombre": nombre,
            "peso": peso,
            "estatura": estatura,
            "posicion": posicion
        }
        jugadores.append(jugador)
    print("Jugadores registrados correctamente.\n")
    return jugadores

# Funciones para registrar jugadores, buscar por RUT y calcular estado nutricional
def buscar_jugador(rut, jugadores):
    for jugador in jugadores:
        if jugador["rut"] == rut:
            return jugador
    return None

def mostrar_nombres(jugadores):
    print("Nombres de los jugadores registrados:")
    for jugador in jugadores:
        print(jugador["nombre"])


def estado_nutricional(jugador):
    imc = jugador["peso"] / (jugador["estatura"] ** 2)
    if imc < 25:
        return f"IMC: {imc:.2f} (Normal)"
    else:
        return f"IMC: {imc:.2f} (Sobrepeso)"
    
# Función principal para el control nutricional de jugadores
# Permite registrar jugadores, buscar por RUT y mostrar estado nutricional

def main():
    jugadores = []
    while True:
        print("\n--- Dream Team: Control Nutricional ---")
        print("1. Registrar jugadores")
        print("2. Buscar jugador por RUT")
        print("3. Mostrar estado nutricional de un jugador")
        print("4. Mostrar nombres de jugadores")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            jugadores = registrar_jugadores()
        elif opcion == "2":
            rut = input("Ingrese RUT del jugador: ")
            jugador = buscar_jugador(rut, jugadores)
            if jugador:
                print(jugador)
            else:
                print("Jugador no encontrado.")
        elif opcion == "3":
            rut = input("Ingrese RUT del jugador: ")
            jugador = buscar_jugador(rut, jugadores)
            if jugador:
                print(estado_nutricional(jugador))
            else:
                print("Jugador no encontrado.")
        elif opcion == "4":
            mostrar_nombres(jugadores)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
    