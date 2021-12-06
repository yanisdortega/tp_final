from usuarios import usuarios
from carrito import Carrito
from validator import val
from factura import Factura
import stdiomask
from db import dba
from funciones import mostrarCiudades, recordarContraseña, agregarProductos
import base64
import datetime
user=0

def mostrar_productos():
    print("\n···· Lista de productos disponibles ····\n")
    dba.get_cursor().execute("select Nombre from productos where Nombre IS NOT NULL")
    primero=dba.get_cursor().fetchall()
    dba.get_cursor().execute("select Precio from productos")
    segundo=dba.get_cursor().fetchall()
    for count,i in enumerate(primero, 1):
        print(count,'-',*i, ' $',*segundo[count-1])

def crear_cuenta():
    i=False
    while not i==True:
        datos={}
        datos["Nombres"]=input("● Ingrese sus nombres:\n")
        datos["Apellidos"]=input("● Ingrese sus apellidos:\n")
        datos["Fecha_de_nacimiento"]=input("● Ingrese su fecha de nacimiento (YYYY-MM-DD):\n")
        datos["Mail"]=input("● Ingrese su email:\n")
        datos["Contrasena"]=input("● Ingrese su contraseña (DEBE TENER AL MENOS 6 CARACTERES, UNA MAYUSCULA, UNA MINUSCULA, UN CARACTER NUMERICO, Y AL MENOS UN CARACTER ESPECIAL: $,@,#,%,-,!,¡,?,¿,*,+):\n")
        datos["cContrasena"]=input("● Ingrese de nuevo la contraseña elegida:\n")
        datos["Telefono"]=input("● Ingrese su numero de telefono:\n")
        mostrarCiudades()
        datos["Ciudad_id"]=input("● Ingrese el ID de su ciudad:\n")
        errores=val.validar_usuarios(datos)
        if not errores:
            usuario=usuarios(datos["Nombres"],datos["Apellidos"],datos["Fecha_de_nacimiento"],datos["Mail"],datos["Contrasena"],datos["Telefono"],datos["Ciudad_id"])
            usuario.crear_usuarios()
            print("Usuario creado con éxito.")
            i=True
            return usuario
        else:
            for i in errores.values():
                print(f"\033[;31mTuvo el siguiente error: {i}.\033[0m")
            print(f"\033[;31mInténtelo de nuevo.\033[0m")

def ingresar_cuenta():
    global user
    datos={}
    datos['Mail']=input("\n● Ingrese su mail: ")
    datos['Contrasena']=stdiomask.getpass(prompt='● Ingrese su contraseña: ', mask='*')
    errores=val.validar_login(datos)
    if errores[4]==datos.get('Mail') and base64.decodebytes(errores[5].encode("UTF-8")).decode('utf-8')==datos.get('Contrasena'):
        sql="select UsuariosID from usuarios where Mail=%s"
        valor=(datos.get('Mail'),)
        dba.get_cursor().execute(sql,valor)
        for i in dba.get_cursor().fetchone():
            # Asigno el valor del ID del usuario a la variable global user
            user=i
    else:
        print("Mail o contraseña incorrectos. El e-commerce se cerrará por seguridad.")
        quit()

def nombre_usuario(user):
    sql="select Nombres from usuarios where UsuariosID=%s"
    val=(user,)
    dba.get_cursor().execute(sql,val)
    for i in dba.get_cursor().fetchone():
        return i

def eliminar_usuario(user):
    usuarios.eliminar_cuenta(user)
    print("Usuario dado de baja con éxito.")

def eliminarProductos(user):
    val=(user,)
    dba.get_cursor().execute("select Productos_id from carrito where Usuarios_id=%s", val)
    id=dba.get_cursor().fetchall()
    producto=int(input("\nIngrese el ID del producto que desea eliminar: "))
    if (producto,) in id:
        items=Carrito(user,producto)
        items.eliminar_producto()
        print("\nProducto eliminado con éxito.")
    else:
        print("\nNo tiene este producto en su carrito.")

def verCarrito():
    print("\nCarrito de compras\n")
    sql="select Nombre from itemscarrito where Usuarios_id=%s AND Nombre IS NOT NULL"
    val=(user,)
    dba.get_cursor().execute(sql, val)
    nombres=dba.get_cursor().fetchall()
    nombreproducto=[]
    for i in nombres:
        nombreproducto.append(i[0])
    sql="select Productos_id from itemscarrito where Usuarios_id=%s"
    val=(user,)
    dba.get_cursor().execute(sql,val)
    ids=dba.get_cursor().fetchall()
    idproducto=[]
    for j in ids:
        idproducto.append(j[0])
    dicc={}
    for i in range(len(nombreproducto)):
        dicc[nombreproducto[i]]=idproducto[i]
    if not dicc:
        print("<0 items>")
    else:
        for count,(k, v) in enumerate(dicc.items(), 1):
            print(f"Ítem nro {count}: {k} (ID:{v})")

def mostrar_factura():
    sql="select Productos_id from itemscarrito where Usuarios_id=%s"
    val=(user,)
    dba.get_cursor().execute(sql, val)
    cantidad=dba.get_cursor().fetchall()
    sql1="select Precio from itemscarrito where Usuarios_id=%s"
    dba.get_cursor().execute(sql1, val)
    ids=dba.get_cursor().fetchall()
    
    sql="select Nombre from itemscarrito where Usuarios_id=%s AND Nombre IS NOT NULL"
    val=(user,)
    dba.get_cursor().execute(sql, val)
    nombres=dba.get_cursor().fetchall()
    nombreproducto=[]
    for i in nombres:
        nombreproducto.append(i[0])
    sql2="select Precio from itemscarrito where Usuarios_id=%s AND Precio IS NOT NULL"
    val=(user,)
    dba.get_cursor().execute(sql2,val)
    ids=dba.get_cursor().fetchall()
    idproducto=[]
    for j in ids:
        idproducto.append(j[0])
    dicc={}
    for i in range(len(nombreproducto)):
        dicc[nombreproducto[i]]=idproducto[i]
    suma=0
    for i in ids:
        suma+=i[0]
    print(f'''
---------------------------------
TICKET DE COMPRA VIRTUAL
Fecha y hora: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
---------------------------------
CANTIDAD PRODUCTOS: {len(cantidad)}
Prooductos: ''')
    for count,(k, v) in enumerate(dicc.items(), 1):
        print(f"\n{count}- {k}: ${v}")
    print(f'''
---------------------------------
TOTAL sin descuentos: ${suma}
---------------------------------
:) ¡Gracias por la compra! :)
---------------------------------
''')

def cobro(user):
    sql="select medioPagoID, Nombre from mediopago"
    dba.get_cursor().execute(sql)
    resultado=[]
    resultado=dba.get_cursor().fetchall()
    for i in resultado:
        print(*i, sep=" - ")
    sql1="select CarritoID from carrito where Usuarios_id=%s"
    val=(user,)
    dba.get_cursor().execute(sql1, val)
    idcarrito=dba.get_cursor().fetchall()[0]
    metododepago=int(input("Seleccione el ID del método de pago que desea utilizar: "))
    facturas=Factura(datetime.datetime.now(),*idcarrito, metododepago)
    facturas.generar_factura()

def modificar_cuenta():
    print("\n···· Datos a modificar ····\n")
    for k,v in menuModif.items():
        print(f'> {k}: {v}')
    opcionmodif=int(input("\033[;36m"+"\nIngrese qué dato quiere modificar: "+"\033[0m"))
    if opcionmodif==1:
        nuevoNombre=input("● Ingrese su nuevo nombre: ")
        sql="UPDATE usuarios SET Nombres=%s WHERE UsuariosID=%s"
        val=(nuevoNombre,user)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    elif opcionmodif==2:
        nuevoApellido=input("● Ingrese su nuevo apellido: ")
        #usuarios.update_apellidos(nuevoApellido,user)
        sql="UPDATE usuarios SET Apellidos=%s WHERE UsuariosID=%s"
        val=(nuevoApellido,user)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        print("Apellido modificado con exito.")
    elif opcionmodif==3:
        nuevoMail=input("● Ingrese su nuevo mail: ")
        sql="UPDATE usuarios SET Mail=%s WHERE UsuariosID=%s"
        val=(nuevoMail,user)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    elif opcionmodif==4:
        nuevaContrasena=input("● Ingrese su nueva contraseña: ")
        sql="UPDATE usuarios SET Contrasena=%s WHERE UsuariosID=%s"
        val=(nuevaContrasena,user)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    elif opcionmodif==5:
        nuevoTelefono=int(input("● Ingrese su nuevo número telefónico: "))
        sql="UPDATE usuarios SET Telefono=%s WHERE UsuariosID=%s"
        val=(nuevoTelefono,user)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

menuInicial={1: 'Crear nueva cuenta', 2:'Ingresar a su cuenta', 3:'No recuerdo mi contraseña!', 4:'Salir'}
menuSecundario={1:'Modificar datos personales', 2: 'Ver productos', 3: 'Agregar productos al carrito', 4: 'Sacar productos del carrito', 5: 'Ver carrito de compras', 6: 'Ver promociones por método de pago', 7:'Comprar carrito de compras', 8: 'Eliminar mi cuenta de usuario',9: 'Cerrar sesión'}
menuModif={1: 'Modificar nombres', 2: 'Modificar apellidos', 3: 'Modificar e-mail', 4:'Modificar contraseña', 5:'Modificar teléfono de contacto', 6:'Volver al menú principal'}

def menu():
    print("\n"+"\033[1;36m"+" ***************¡Bienvenido al e-commerce virtual!***************"+"\033[0m"+"\n") 
    for k,v in menuInicial.items():
        print(f'> {k}: {v}')
    opcion=int(input("\033[;36m"+"\nIngrese qué acción desea realizar: "+"\033[0m"))
    if opcion==1:
        crear_cuenta()
        menu()
    elif opcion==2:
        ingresar_cuenta()
        menu_usuarios(user)
    elif opcion==3:
        recordarContraseña()
        menu()
    elif opcion==4:
        print(("\033[1;36m"+"***************¡Nos vemos pronto!***************"+"\033[0m"))
        quit()
def menu_usuarios(user):
    print(f"\n\033[1;36m ******************¡Bienvenida/o, {nombre_usuario(user)}!******************\033[0m\n")
    while True:
        print("\n···· Menú personal ····\n")
        for k,v in menuSecundario.items():
            print(f'> {k}: {v}')
        opcion=int(input("\033[;36m"+"\nIngrese qué acción desea realizar: "+"\033[0m"))
        if opcion==1:
            modificar_cuenta()
        elif opcion==2:
            mostrar_productos()
        elif opcion==3:
            mostrar_productos()
            agregarProductos(user)
        elif opcion==4:
            verCarrito()
            eliminarProductos(user)
        elif opcion==5:
            verCarrito()
        elif opcion==6:
            print('''\n···· Promociones por método de pago ····
15% de descuento en su compra para pagos en efectivo
10% de descuento en su compra para pagos mediante depósito bancario''')
        elif opcion==7:
            cobro(user)
            mostrar_factura()
            Carrito.setear_carrito(user)
        elif opcion==8:
            decision=input("\nPor favor, confirme si quiere eliminar su cuenta de usuario para siempre (SI/NO): ").lower()
            if decision[0] not in {"s","n"}:
                print("La respuesta debe ser SI/NO.")
            elif decision[0]=="s":
                eliminar_usuario(user)
                quit()
            elif decision[0]=="n":
                print("\nLo redigiremos al menú principal.")
                menu_usuarios(user)
        else:
            print(("\033[1;36m"+"***************¡Nos vemos pronto!***************"+"\033[0m"))
            quit()
menu()
