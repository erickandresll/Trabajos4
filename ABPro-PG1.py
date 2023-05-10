# Se define clase cliente.

class Cliente:
    def __ini__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = 0
        
    def agregar_saldo(self, monto):
        self.__saldo += monto
        print("Saldo actualizado.")
        
    def mostrar_saldo(self):
        print(f"El saldo actual es: {self.__saldo}")
        
 # Se define clase producto. 
     
class Producto: 
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria 
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 1.19
        
# Se define clases vendedor. 
        
class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = 0
        
cliente1 = Cliente("C001", "Erick", "Lopez", "erick@lopez.cl", "13-10-2023", 100)
cliente2 = Cliente("C002", "Andres", "Lopez", "andres@lopez.cl", "25/12/2023", 200)
producto1 = Producto("P001", "Notebook", "Electronica", "HP", 10, 300000)
producto2 = Producto("P002", "Cocina", "Linea blanca", "Sindelen", 5, 150000)
vendedor1 = Vendedor("11222333-4", "Carlos", "Soto", "Electronica")