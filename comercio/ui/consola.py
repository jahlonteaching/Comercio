import sys
from comercio.mundo.tienda import Tienda


class Consola:

    def __init__(self):
        self.tienda = Tienda()
        self.opciones = {
            "1": self.registrar_usuario,
            "2": self.listar_productos,
            "3": self.agregar_producto_al_carrito,
            "4": self.ver_carrito,
            "5": self.eliminar_item_carrito,
            "6": self.comprar_carrito,
            "7": self.salir
        }

    def mostar_menu(self):
        print("""
        \n
        BIENVENIDO A LA TIENDA DE PRODUCTOS
        ===================================
        Menú de opciones:\n
        1. Registrar usuario
        2. Listar productos
        3. Agregar producto a carrito
        4. Ver carrito
        5. Eliminar item de carrito
        6. Comprar carrito
        7. Salir
        ===================================
        """)

    def ejecutar(self):
        while True:
            self.mostar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"ERROR: {opcion} no es una opción válida")

    def registrar_usuario(self):
        print("\n>>> REGISTRAR USUARIO")
        cedula = input("Ingrese la cédula: ")
        nombre = input("Ingrese el nombre: ")
        if self.tienda.registrar_usuario(cedula, nombre):
            print("INFO: El usuario se registró exitosamente")
        else:
            print(f"ERROR: Ya existe un usuario con la cédula {cedula}")

    def listar_productos(self):
        print("\n>>> LISTADO DE PRODUCTOS")
        for producto in self.tienda.productos.values():
            print(producto)

    def agregar_producto_al_carrito(self):
        print("\n>>> AGREGAR PRODUCTO A CARRITO")
        self.listar_productos()
        cedula = input("Ingrese la cédula del usuario: ")
        sku = input("Ingrese el SKU del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        resp = self.tienda.agregar_producto_a_carrito(cedula=cedula, sku=sku, cantidad=cantidad)
        if resp == 0:
            print("INFO: Se agregó el producto al carrito")
        elif resp == -1:
            print(f"ERROR: No existe un producto con el sku {sku}")
        elif resp == -2:
            print(f"ERROR: No existe un usuario con la cédula {cedula}")
        elif resp == -3:
            print(f"ERROR: No hay unidades disponibles para agregar la cantidad {cantidad}")

    def ver_carrito(self):
        print("INFO: AUN NO ESTÁ IMPLEMENTADO")

    def eliminar_item_carrito(self):
        pass

    def comprar_carrito(self):
        pass

    def salir(self):
        print("\nMUCHAS GRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)
