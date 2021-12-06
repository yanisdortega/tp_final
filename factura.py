from db import dba
class Factura():
    def __init__(self, FechaEmision,Carrito_id, Mediodepago_id):
        self.__FacturaID=0 
        self.__FechaEmision=FechaEmision
        self.__Carrito_id=Carrito_id
        self.__Mediodepago_id=Mediodepago_id
    def get_FacturaID(self):
        return self.__FacturaID
    def get_FechaEmision(self):
        return self.__FechaEmision
    def get_Carrito_id(self):
        return self.__Carrito_id
    def get_Mediodepago_id(self):
        return self.__Mediodepago_id
    def set_FacturaID(self, FacturaID):
        self.__FacturaID=FacturaID
    def set_FechaEmision(self,FechaEmision):
        self.__FechaEmision=FechaEmision
    def set_Carrito_id(self,Carrito_id):
        self.__Carrito_id=Carrito_id
    def set_Mediodepago_id(self,Mediodepago_id):
        self.__Mediodepago_id=Mediodepago_id
    def generar_factura(self):
        sql='insert into factura(FechaEmision,Carrito_id,Mediodepago_id) values (%s,%s,%s)'
        val=(self.get_FechaEmision(),self.get_Carrito_id(),self.get_Mediodepago_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_FacturaID(dba.get_cursor().lastrowid)

