import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def mostrar_menu():
    print("\n--- REDIS INTERACTIVO ---")
    print("1. Guardar valor")
    print("2. Leer valor")
    print("3. Incrementar contador")
    print("4. Ver contador")
    print("5. Listar todas las claves")
    print("6. Eliminar clave")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige opción: ")

    if opcion == "1":
        clave = input("Clave: ")
        valor = input("Valor: ")
        r.set(clave, valor)
        print(f"✅ Guardado: {clave} = {valor}")

    elif opcion == "2":
        clave = input("Clave: ")
        valor = r.get(clave)
        print(f"📦 {clave} = {valor}" if valor else "❌ Clave no existe")

    elif opcion == "3":
        clave = input("Nombre del contador: ")
        nuevo = r.incr(clave)
        print(f"🔢 {clave} = {nuevo}")

    elif opcion == "4":
        clave = input("Nombre del contador: ")
        valor = r.get(clave)
        print(f"🔢 {clave} = {valor}" if valor else "❌ No existe")

    elif opcion == "5":
        claves = r.keys("*")
        if claves:
            for c in claves:
                print(f"  • {c} → {r.get(c)}")
        else:
            print("📭 No hay claves guardadas")

    elif opcion == "6":
        clave = input("Clave a eliminar: ")
        eliminado = r.delete(clave)
        print("🗑️ Eliminado" if eliminado else "❌ Clave no existe")

    elif opcion == "0":
        print("👋 Saliendo...")
        break

    else:
        print("❌ Opción inválida")