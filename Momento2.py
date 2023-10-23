class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = 0

    def asignar_precio_venta(self, margen_de_venta):
        self.precio_de_venta = self.costo / (1 - margen_de_venta)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, " \
               f"Costo: {self.costo}, Cantidad: {self.cantidad}, Precio de Venta: {self.precio_de_venta}"


class RegistroProductos:
    def __init__(self):
        self.productos = {}
    def registrar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
        else:
            print(f"El producto con ID {producto.id} ya está registrado.")

    def imprimir_lista_productos(self):
        for producto in self.productos.values():
            print(producto)


# Ejemplo de uso
registro = RegistroProductos()
producto1 = Producto(1, "Iphone", "Descripción1", 10000, 89)
producto2 = Producto(2, "Macbook", "Descripción2", 15000, 36)
producto3 = Producto(3, "Iwatch", "Descripción3", 12000, 14)
producto4 = Producto(4, "Imac", "Descripción4", 150000, 67)
producto5 = Producto(5, "MacStudio", "Descripción5", 30000, 78)
producto6 = Producto(6, "MacPro", "Descripción6", 915000, 98)

producto1.asignar_precio_venta(0.2)  # Margen de venta del 20%
producto2.asignar_precio_venta(0.3)  # Margen de venta del 30%
producto3.asignar_precio_venta(0.1)  # Margen de venta del 20%
producto4.asignar_precio_venta(0.4)
producto5.asignar_precio_venta(0.5)  # Margen de venta del 20%
producto6.asignar_precio_venta(0.3)

registro.registrar_producto(producto1)
registro.registrar_producto(producto2)
registro.registrar_producto(producto3)
registro.registrar_producto(producto4)
registro.registrar_producto(producto5)
registro.registrar_producto(producto6)

registro.imprimir_lista_productos()
