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

    def buscar_producto(self, sku) -> Producto:
        pass

    def buscar_usuario(self, cedula) -> Usuario:
        pass

    def agregar_producto_a_carrito(self, sku, cantidad, cedula):
        producto = self.buscar_producto(sku)
        if producto is not None:
            if producto.hay_unidades_disponibles(cantidad):
                usuario = self.buscar_usuario(cedula)
                usuario.agregar_producto_a_carrito(producto, cantidad)

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
        pass




