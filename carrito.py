from db import dba

class Carrito():
    def __init__(self, usuario_id, producto_id):
        self.__CarritoID=0
        self.__usuario_id=usuario_id
        self.__producto_id=producto_id
    def get_carritoid(self):
        return self.__CarritoID
    def get_usuario_id(self):
        return self.__usuario_id
    def get_producto_id(self):
        return self.__producto_id
    def set_carritoid(self,CarritoID):
        self.__CarritoID=CarritoID
    def set_usuario_id(self, usuario_id):
        self.__usuario_id=usuario_id
    def set_producto_id(self, producto_id):
        self.__producto_id=producto_id
    def llenar_carrito(self):
        sql="insert into carrito(Usuarios_id, Productos_id) values (%s,%s)"
        val=(self.get_usuario_id(),self.get_producto_id())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit() 
        self.set_carritoid(dba.get_cursor().lastrowid)  
    def eliminar_producto(self):
        sql='delete from carrito where Productos_id=%s LIMIT 1'
        val=(self.get_producto_id(),)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
    def ver_carrito(self):
        sql="select Productos_id from carrito where Usuarios_id=%s"
        val=(self.get_usuario_id())
        dba.get_cursor().execute(sql,val)
        for i in dba.get_cursor().fetchall():
            print(*i)
    def setear_carrito(self):
        sql="update carrito set Productos_id=19 where Usuarios_id=%s"
        val=(self,)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    def eliminar_carrito(self):
        sql="delete from carrito where Usuarios_id=%s"
        val=(self,)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()