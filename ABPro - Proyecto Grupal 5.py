from excep import NoStockException

# Se define clase cliente.
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo
        
# Se agrega saldo al cliente. ########## AGREGUÉ TRY/EXCEPT POR SI SE AGREGA UN VALOR INCORRECTO AL MOMENTO DE INGRESAR SALDO.
    def agregar_saldo(self, monto):
        try:
            self.__saldo += monto
            print("Saldo actualizado.")
            return True
        except Exception as e:
            print("Error al agregar saldo:", str(e))
            return False

# Muestra el saldo al cliente.      
    def mostrar_saldo(self):
        try:
            print(f"El saldo actual es: {self.__saldo}")
            return True
        except Exception as e:
            print("Error al mostrar saldo:", str(e))
            return False

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

## Se define clase producto. 
class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria 
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto
        
        
#### EXCEPCIÓN PERSONALIZADA EN ARCHIVO EXTERNO excep.py, arriba importé el archivo. (no recordaba si era así tuve que buscar)      
    def descontar_stock(self):
        try:
            if self.stock > 0:
                self.stock -= 1
                return True
            else:
                raise NoStockException("No hay suficiente stock disponible para el producto.")
        except NoStockException as e:
            print(str(e))
            return False
        
    def calcular_valor_final(self):
        return self.valor_neto * self.__impuesto

# Se define clase Bodega.
class Bodega:
    def __init__(self):
        self.stock = 500

    def verificar_stock_suficiente(self):
        return self.stock >= 300

    def verificar_stock(self):
        if self.stock < 50:
            print("Se está solicitando y reponiendo productos.")
            bodega = Bodega()
            if bodega.verificar_stock_suficiente():
                bodega.descontar_stock(300)
                self.stock += 300
                print("Stock repuesto con éxito.")
            else:
                print("No hay suficiente stock en la bodega para reponer.")
                
    def descontar_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad

# Se define clase Vendedor.
class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision

    def vender(self, cliente, producto):
        orden_compra = OrdenCompra(1, producto, True)
        valor_final = orden_compra.calcular_valor_final()
        if producto.descontar_stock():
            self.__comision += producto.valor_neto * 0.005
            if cliente._Cliente__saldo >= valor_final:
                cliente._Cliente__saldo -= valor_final
                print("Venta realizada con éxito.")
                orden_compra.mostrar_detalle()
            else:
                print("Saldo insuficiente en el cliente.")
        else:
            print("No hay suficiente stock disponible para el producto.")

    def mostrar_comision(self):
        print(f"La comisión acumulada es: {self.__comision}")


##### CREO QUE SE LE DEBE AGREGAR LA FUNCIÓN AL VENDEDOR PARA QUE PUEDA VISUALIZAR ESTA INFORMACIÓN DE PROMEDIO
def calcular_valor_promedio(self):
    try:
        if len(self.compras) > 0:
            total = sum(self.compras)
            promedio = total / len(self.compras)
            return promedio
        else:
            raise ValueError("El cliente no tiene compras.")
    except ValueError as e:
        print(str(e))
        
# Se define clase OrdenCompra.
class OrdenCompra:
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho

    def calcular_valor_final(self):
        valor_final = self.producto.calcular_valor_final()
        if self.despacho:
            valor_final += 5000
        return valor_final

    def mostrar_detalle(self):
        print(f"Valor neto: {self.producto.valor_neto}")
        print(f"Impuesto: {self.producto.__impuesto}")
        print(f"Despacho: {'Sí' if self.despacho else 'No'}") ## Lo ví en tiktok, no sé si se estará bien así.
        print(f"Valor total: {self.calcular_valor_final()}")
        
class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.comuna = pais
        self.tipo_persona = tipo_persona

# Ejemplo de uso
cliente = Cliente(1, "Erick", "López", "erick@gmail.com", "13-05-2023", 1000)
producto = Producto("SKU123", "Cemento", "Materiales de construcción", "Sodimac", 10, 100, 1.19)
vendedor = Vendedor("987654321", "Emilio", "Eaton", "Patio constructor A", 0)

vendedor.vender(cliente, producto)
cliente.mostrar_saldo()
vendedor.mostrar_comision()


