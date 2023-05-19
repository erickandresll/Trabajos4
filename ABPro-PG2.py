# Se define clase cliente.
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo

# Se agrega saldo al cliente.
    def agregar_saldo(self, monto):
        self.__saldo += monto
        print("Saldo actualizado.")

# Muestra el saldo al cliente.       
    def mostrar_saldo(self):
        print(f"El saldo actual es: {self.__saldo}")

# Función para comprar los productos.       
    def comprar_producto(self, producto):
        if self.__saldo >= producto.calcular_valor_final():
            if producto.descontar_stock():
                self.__saldo -= producto.calcular_valor_final()
                self.__actualizar_comision(producto.valor_neto)
                print("Compra realizada con éxito.")
            else:
                print("No hay suficiente stock disponible para el producto.")
        else:
            print("Saldo insuficiente para comprar el producto.")

# La función actualiza la comisión con el valor neto más el 5% de comisión.
    def __actualizar_comision(self, valor_neto):
        self.__comision += valor_neto * 0.005

# Opción para que el vendedor revise su comisión acumulada.        
    def mostrar_comision(self):
        print(f"La comisión acumulada es: {self.__comision}")

# Se define clase producto.
class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria 
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto
        
    def descontar_stock(self):
        if self.stock > 0:
            self.stock -= 1
            return True
        else:
            return False
        
    def calcular_valor_final(self):
        return self.valor_neto * self.__impuesto

# Se define clase proveedor.
class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.comuna = pais
        self.tipo_persona = tipo_persona

# Se define clase vendedor.
class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision
        
    def vender(self, cliente, producto):
        if producto.descontar_stock():
            comision_producto = producto.valor_neto * 0.005
            self.__comision += comision_producto
            valor_final = producto.calcular_valor_final()
            if cliente._Cliente__saldo >= valor_final:
                cliente._Cliente__saldo -= valor_final
                print("Venta realizada con éxito.")
            else:
                print("Saldo insuficiente en el cliente.")
        else:
            print("No hay suficiente stock disponible para el producto.")
        
    def mostrar_comision(self):
        print(f"La comisión acumulada es: {self.__comision}")

# Ejemplo de uso
cliente = Cliente(1, "Erick", "López", "erick@gmail.com", "13-05-2023", 1000)
proveedor = Proveedor("123456789", "Antonio González", "Constructora Antornio", "Villa Alemana", "Persona Jurídica")
producto = Producto("SKU123", "Cemento", "Materiales de contrucción", "Sodimac", 10, 100, 1.19)
vendedor = Vendedor("987654321", "Emilio", "Eaton", "Patio contructor A", 0)

vendedor.vender(cliente, producto)
cliente.mostrar_saldo()
vendedor.mostrar_comision()
