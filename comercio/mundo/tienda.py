from typing import Optional


class Producto:

    def __init__(self, sku, nombre, descripcion, unidades_disponibles, precio_unitario):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.unidades_disponibles = unidades_disponibles
        self.precio_unitario = precio_unitario

    def hay_unidades_disponibles(self, cantidad) -> bool:
        return self.unidades_disponibles >= cantidad

    def descontar_unidades(self, cantidad):
        self.unidades_disponibles -= cantidad

    def __str__(self) -> str:
        return f"{self.sku} - {self.nombre} - {self.precio_unitario}"


class Item:

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.total = 0

    def calcular_total(self) -> float:
        pass


class Carrito:

    def __init__(self):
        self.items = []
        self.total = 0

    def agregar_item(self, producto, cantidad):
        item = Item(producto, cantidad)
        self.items.append(item)

    def calcular_total(self) -> float:
        pass

    def eliminar_item(self, item):
        pass

    def tiene_items(self) -> bool:
        return len(self.items) > 0

    def comprar(self):
        for item in self.items:
            item.producto.descontar_unidades(item.cantidad)

    def limpiar(self):
        self.items.clear()


class Usuario:

    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.carrito = Carrito()

    def agregar_producto_a_carrito(self, producto, cantidad):
        self.carrito.agregar_item(producto, cantidad)


class Tienda:

    def __init__(self):
        self.archivo = "productos.json"
        self.total_acumulado = 0
        self.productos = {}
        self.usuarios = {}
        self.cargar_informacion_producto()

    def registrar_usuario(self, cedula, nombre) -> bool:
        """
        Este método registra un nuevo usuario en la tienda
        :param cedula: str con la cédula del usuario
        :param nombre: str con el nombre del usuario
        :return: True si se pudo registrar el usuario. False si ya existe un usuario
                 con la cédula dada
        """
        if self.buscar_usuario(cedula) is None:
            usuario = Usuario(cedula, nombre)
            self.usuarios[cedula] = usuario
            return True
        else:
            return False

    def buscar_producto(self, sku) -> Optional[Producto]:
        if sku in self.productos.keys():
            return self.productos[sku]
        else:
            return None

    def buscar_usuario(self, cedula) -> Optional[Usuario]:
        if cedula in self.usuarios.keys():
            return self.usuarios[cedula]
        else:
            return None

    def agregar_producto_a_carrito(self, sku, cantidad, cedula) -> int:
        """
        Agregar un producto al carrito de compras de un usuario
        :param sku: el código del producto
        :param cantidad: la cantidad de unidades que se van a agregar
        :param cedula: la cédula del usuario que está haciendo la compra
        :return: 0 si se  agregó el producto al carrito sin problema <br>
                 -1 No existe un producto con el sku dado <br>
                 -2 No existe el usuario con la cédula dada <br>
                 -3 No hay unidades disponibles para agregar la cantidad dada
        """
        producto = self.buscar_producto(sku)
        if producto is not None:
            if producto.hay_unidades_disponibles(cantidad):
                usuario = self.buscar_usuario(cedula)
                if usuario is not None:
                    usuario.agregar_producto_a_carrito(producto, cantidad)
                else:
                    return -2
            else:
                return -3
        else:
            return -1

        return 0

    def eliminar_item_de_carrito(self, item, cedula):
        usuario = self.buscar_usuario(cedula)
        usuario.carrito.eliminar_item(item)

    def comprar_carrito(self, cedula):
        usuario = self.buscar_usuario(cedula)
        if usuario.carrito.tiene_items():
            valor = usuario.carrito.calcular_total()
            self.total_acumulado += valor
            usuario.carrito.comprar()
            usuario.carrito.limpiar()

    def cargar_informacion_producto(self):
        # TODO: Cargar la información de un archivo
        self.productos["EA001"] = Producto("EA001",
                                           "Pantalla",
                                           "Pantalla de computador de 21 pulgadas",
                                           10,
                                           900000)
        self.productos["SP001"] = Producto("SP001",
                                           "Disco duro",
                                           "Disco SSD de 1Tb",
                                           20,
                                           750000)
        self.productos["WE001"] = Producto("WE001",
                                           "Arroz",
                                           "Arroz premium",
                                           20,
                                           5)
        self.productos["EA002"] = Producto("EA002",
                                           "Silla",
                                           "Silla reclinable",
                                           15,
                                           650000)





