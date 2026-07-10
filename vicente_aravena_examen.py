##Paso 1 ( se realiza el bucle infinito que pide el número)
def leer_entero(mensaje: str, mensaje_error: str = "Debe ingresar valores enteros") -> int:
    while True:
        try:

##Paso 2 (Atrapar el error si el usuario escribe letras)
            return int(input(mensaje))
        except ValueError:
            print(mensaje_error)

def leer_flotante(mensaje: str, mensaje_error: str = "Debe ingresar un valor numérico") -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(mensaje_error)

##Paso 3 (Evitar códigos vacíos o repetidos)
def validar_codigo_nuevo(codigo: str, productos: dict) -> bool:
    if not codigo.strip():
        return False
    return codigo.strip().upper() not in productos

##Paso 4 (Asegurar que los textos no sean puros espacios)
def validar_texto(texto: str) -> bool:
    return bool(texto.strip())

##Paso 5 (Limitar respuestas a 's' o 'n')
def validar_opcion_binaria(opcion: str) -> bool:
    return opcion.strip().lower() in ['s', 'n']

## Paso 6 (Contar Stock por Categoría)
def unidades_categoria(categoria: str, productos: dict, stock: dict) -> None:
    total_unidades = 0
    categoria_buscada = categoria.strip().lower()

    for codigo, datos_producto in productos.items():
        if datos_producto[1].strip().lower() == categoria_buscada:
            if codigo in stock:
                total_unidades += stock[codigo][1]
                
    print(f"El total de unidades disponibles es: {total_unidades}")

## Paso 7 (Vitrina por Rango de Precio)
def busqueda_precio(p_min: int, p_max: int, productos: dict, stock: dict) -> None:
    resultados = []
    
    for codigo, datos_stock in stock.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]
        
        if p_min <= precio <= p_max and unidades > 0:
            if codigo in productos:
                nombre = productos[codigo][0]
                resultados.append(f"{nombre}--{codigo}")
    if resultados:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")

## Paso 8 (Cambiar Precios)
def actualizar_precio(codigo: str, nuevo_precio: int, stock: dict) -> bool:
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio in stock:
        stock[codigo_limpio][0] = nuevo_precio
        return True
    return False

## Paso 9 (Abastecer la Tienda / Agregar)
def agregar_producto(codigo: str, nombre: str, categoria: str, marca: str, peso_kg: float, 
                     es_importado: bool, es_para_cachorro: bool, precio: int, unidades: int, 
                     productos: dict, stock: dict) -> None:
    codigo_limpio = codigo.strip().upper()
    
    productos[codigo_limpio] = [
        nombre.strip(), 
        categoria.strip().lower(), 
        marca.strip(), 
        peso_kg, 
        es_importado, 
        es_para_cachorro
    ]
    stock[codigo_limpio] = [precio, unidades]

## Paso 10 (Sacar del Catálogo / Eliminar)
def eliminar_producto(codigo: str, productos: dict, stock: dict) -> bool:
    codigo_limpio = codigo.strip().upper()
    if codigo_limpio in productos and codigo_limpio in stock:
        del productos[codigo_limpio]
        del stock[codigo_limpio]
        return True
    return False

## Paso 11 (listas de productos y stock)
def main():
    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
    }
    
    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3]
    }
## Paso 12 (Menú Principal)
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")

        opcion = leer_entero("Ingrese opción: ")
        
        if opcion == 1:
            cat = input("Ingrese categoría a consultar: ")
            unidades_categoria(cat, productos, stock)
        elif opcion == 2:
            p_min = leer_entero("Ingrese precio mínimo: ")
            p_max = leer_entero("Ingrese precio máximo: ")
            busqueda_precio(p_min, p_max, productos, stock)
        elif opcion == 3:
            while True:
                cod = input("Ingrese código del producto: ")
                nuevo_precio = leer_entero("Ingrese nuevo precio: ")
                if actualizar_precio(cod, nuevo_precio, stock):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                repetir = input("¿Desea actualizar otro precio (s/n)?: ")
                if repetir.strip().lower() != 's':
                    break

        elif opcion == 4:
            cod = input("Ingrese código del producto: ")
            nom = input("Ingrese nombre: ")
            cat = input("Ingrese categoría: ")
            mar = input("Ingrese marca: ")
            pes = leer_flotante("Ingrese peso (kg): ")
            imp = input("¿Es importado? (s/n): ")
            cac = input("¿Es para cachorro? (s/n): ")
            pre = leer_entero("Ingrese precio: ")
            uni = leer_entero("Ingrese unidades: ")

            if not validar_codigo_nuevo(cod, productos):
                print("Error: El código está vacío o ya existe.")
            elif not validar_texto(nom) or not validar_texto(cat) or not validar_texto(mar):
                print("Error: El nombre, categoría o marca no pueden estar vacíos.")
            elif pes <= 0:
                print("Error: El peso debe ser mayor a cero.")
            elif not validar_opcion_binaria(imp) or not validar_opcion_binaria(cac):
                print("Error: Las respuestas de importado y cachorro deben ser 's' o 'n'.")
            elif pre <= 0:
                print("Error: El precio debe ser un número entero mayor a cero.")
            elif uni < 0:
                print("Error: Las unidades deben ser un número entero positivo o cero.")
            else:
                es_imp = imp.strip().lower() == 's'
                es_cac = cac.strip().lower() == 's'
                
                agregar_producto(cod, nom, cat, mar, pes, es_imp, es_cac, pre, uni, productos, stock)
                print("Producto agregado")
        elif opcion == 5:
            cod = input("Ingrese código del producto: ")
            if eliminar_producto(cod, productos, stock):
                print("Producto eliminado")
            else:
                print("El código no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida (1-6).")

if __name__ == "__main__":
    main()