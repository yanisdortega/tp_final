from db import dba
from validate_email import validate_email
import base64
class Validator():
    def __init__(self):
        pass
    def validar_usuarios(self,dicc):
        datosFinales={}
        errores={}
        caracteresEspeciales=['$', '@', '#', '%', '-', '!', '¡', '?', '¿','*','+']
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        #Verifico los datos ingresados en el campo Nombres
        if datosFinales["Nombres"]=="":
            errores["Nombres"]="campo nombre vacio"
        #Verifico los datos ingresados en el campo Apellidos
        if datosFinales["Apellidos"]=="":
            errores["Apellidos"]="campo apellidos vacio" 
        #Verifico los datos ingresados en el campo Mail
        if datosFinales["Mail"]=="":
            errores["Mail"]="campo mail vacio"
        elif validate_email(datosFinales['Mail'])==False:
            errores["Mail"]="su mail no tiene formato de mail. Debe terminar con '@mail.com'"
        #Verifico los datos ingresados en el campo Contraseña
        if datosFinales["Contrasena"]=="":
            errores["Contrasena"]="campo contraseña vacio"
        elif len(datosFinales["Contrasena"])<6:
            errores['Contrasena']="la contraseña debe contener mas de 6 caracteres"
        elif not any(i.isupper() for i in datosFinales['Contrasena']):
            errores["Contrasena"]="la contraseña debe contener al menos una mayuscula"
        elif not any(i.isdigit() for i in datosFinales['Contrasena']):
            errores["Contrasena"]="la contraseña debe contener al menos un numero"
        elif not any(i.islower() for i in datosFinales['Contrasena']):
            errores["Contrasena"]="la contraseña debe contener al menos una letra minuscula"
        elif not any(i in caracteresEspeciales for i in datosFinales['Contrasena']):
            errores["Contrasena"]="la contraseña debe contener al menos un caracter especial"
        elif datosFinales['Contrasena']!=datosFinales['cContrasena']:
            errores["Contrasena"]="la contraseña no coincide con la confirmacion de contraseña"
        #Verifico los datos ingresados en el campo teléfono
        if datosFinales["Telefono"]=="":
            errores["Telefono"]="campo telefono vacio"
        elif datosFinales["Telefono"].isdigit()==False:
            errores["Telefono"]="el telefono contiene al menos una letra"
        #Verifico los datos ingresados en el campo Ciudad
        if datosFinales["Ciudad_id"].isdigit()==False:
            errores["Ciudad_id"]="la ciudad debe indicarse con un número"
        if errores=={}:
            sql="select UsuariosID from usuarios where mail=%s"
            val=(datosFinales["Mail"],)
            dba.get_cursor().execute(sql, val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['Mail']="El mail ya esta registrado."
                return errores
        return errores
    def validar_login(self, dicc):
        errores={}
        datosFinales={}
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        sql="select * from usuarios where Mail=%s"
        val=(datosFinales['Mail'],)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        #Trae el mismo valor del mail ingresado que el que esta en la base
        if result is None:
            errores['Mail']="El mail ingresado no existe en la base."   
            print(errores['Mail'])
        else:
            if base64.decodebytes(result[5].encode("UTF-8")).decode('utf-8')==datosFinales['Contrasena']:
                return result
            else:
                errores['Contrasena']="La contraseña es incorrecta."
                print(errores['Contrasena'])
        return result
    def validar_login2(self, dicc):
        errores={}
        datosFinales={}
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        sql="select Mail,Contrasena from usuarios where Mail=%s"
        val=(datosFinales['Mail'],)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        if result is None:
            errores['Mail']="El mail ingresado no existe en la base."   
            return errores
        else:
            if base64.decodebytes(result[1].encode("UTF-8")).decode('utf-8')==datosFinales['Contrasena']:
                return result
            else:
                errores['Contrasena']="La contraseña es incorrecta."
                print(errores['Contrasena'])
        return errores

val=Validator()