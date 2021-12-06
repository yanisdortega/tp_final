import base64
from db import dba
from validator import val
class usuarios():
    def __init__(self, Nombres, Apellidos, Fecha_de_nacimiento, Mail, Contrasena, Telefono, Ciudad_id):
        self.__Nombres=Nombres
        self.__Apellidos=Apellidos
        self.__Fecha_de_nacimiento=Fecha_de_nacimiento
        self.__Mail=Mail
        self.__Contrasena=self.encriptarPass(Contrasena)
        self.__Telefono=Telefono
        self.__Ciudad_id=Ciudad_id
        self.__UsuariosID=0
        self.__Carrito=[]
    def get_Nombres(self):
        return self.__Nombres
    def get_Apellidos(self):
        return self.__Apellidos
    def get_Fecha_de_nacimiento(self):
        return self.__Fecha_de_nacimiento
    def get_Mail(self):
        return self.__Mail
    def get_Contrasena(self):
        return self.__Contrasena
    def get_Telefono(self):
        return self.__Telefono
    def get_Ciudad_id(self):
        return self.__Ciudad_id
    def get_UsuariosID(self):
        return self.__UsuariosID
    def get_Carrito(self):
        return self.__Carrito
    def set_Nombres(self, Nombres):
        self.__Nombres=Nombres
    def set_Apellidos(self, Apellidos):
        self.__Apellidos=Apellidos
    def set_Fecha_de_nacimiento(self, Fecha_de_nacimiento):
        self.__Fecha_de_nacimiento=Fecha_de_nacimiento
    def set_Mail(self, Mail):
        self.__Mail=Mail
    def set_Contrasena(self, Contrasena):
        self.__Contrasena=self.encriptarPass(Contrasena)
    def set_Telefono(self, Telefono):
        self.__Telefono=Telefono
    def set_Ciudad_id(self, Ciudad_id):
        self.__Ciudad_id=Ciudad_id
    def set_UsuariosID(self, ids):
        self.__UsuariosID=ids
    def encriptarPass(self, Contrasena):
        b=Contrasena.encode("UTF-8")
        e=base64.b64encode(b)
        return e.decode("UTF-8")
    def desencriptarPass(self,Contrasena):
        base64.decodebytes(Contrasena.encode("UTF-8")).decode('utf-8')
    def crear_usuarios(self):
        sql="insert into usuarios(Nombres, Apellidos, Fecha_de_nacimiento, Mail, Contrasena, Telefono, Ciudad_id) values(%s, %s, %s, %s, %s, %s, %s)"
        val=(self.get_Nombres(), self.get_Apellidos(), self.get_Fecha_de_nacimiento(), self.get_Mail(), self.get_Contrasena(), self.get_Telefono(), self.get_Ciudad_id())
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit() 
        self.set_UsuariosID(dba.get_cursor().lastrowid) 
    def eliminar_cuenta(variable):
        sql='delete from usuarios where UsuariosID=%s'
        val=(variable,)
        dba.get_cursor().execute(sql, val)
        dba.get_conexion().commit()
    def update_nombres(self,Nombres):
        sql="update set Nombres=%s from usuarios where UsuariosID=%s"
        val=(Nombres,self.get_UsuariosID())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    def update_apellidos(self,Apellidos, user):
        sql="UPDATE usuarios SET Apellidos=%s WHERE UsuariosID=%s"
        val=(Apellidos,user)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    def update_numero(self,Telefono):
        sql="update set Telefono=%s from usuarios where UsuariosID=%s"
        val=(Telefono,self.get_UsuariosID())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    def update_mail(self,Mail):
        sql="update set Mail=%s from usuarios where UsuariosID=%s"
        val=(Mail,self.get_UsuariosID())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    def update_contrasena(self,Contrasena):
        sql="update set Contrasena=%s from usuarios where UsuariosID=%s"
        val=(Contrasena,self.get_UsuariosID())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
