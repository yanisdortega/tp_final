import stdiomask
from db import dba
import base64
from carrito import Carrito
from factura import Factura

# ······· Funcion para agregar productos al carrito ·······
def agregarProductos(user):
    dba.get_cursor().execute("select ProductosID from productos")
    ids=dba.get_cursor().fetchall()
    producto=int(input("\nIngrese el ID del producto que desea agregar a su carrito: "))
    if (producto,) in ids:
        items=Carrito(user,producto)
        items.llenar_carrito()
        print("\nProducto agregado con éxito.")
    else:
        print("\nNúmero ingresado fuera de rango.")

# ······· Funcion para agregar productos al carrito ·······
def nombresProductos():
    dba.get_cursor().execute("select * from productosid")
    for i in dba.get_cursor().fetchall():
        print(*i)
    #agregar a esta vista el precio de los productos para hacer la suma ahi
# ······· Traigo la vista de las ciudades ·······
def mostrarCiudades():
    dba.get_cursor().execute("select CiudadID, nombreCiudad, nombreProvincia, nombrePais from mostrarCiudad")
    print("ID  | CIUDAD | PROVINCIA | PAIS")
    for i in dba.get_cursor().fetchall():
        print(*i,sep=" --> ")

# ······· Metodo para traer colores con ANSCI ·······
#https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html

# ······· Esta funcion compara el numero ingresado en la terminal, los compara con los numeros de la base y si esta el numero imprime que voy por buen camino ·······
def recordarContraseña():
    nrocelular=int(input("Ingrese su número de celular: "))
    valor=[]
    sql="select Telefono from usuarios"
    dba.get_cursor().execute(sql)
    for i in dba.get_cursor().fetchall():
        valor.append(i)
    nuevalista=[]
    for i in valor:
        nuevalista.append(i[0])
    if nrocelular in nuevalista:
        consulta="select Contrasena from usuarios where Telefono=%s"
        numero=(nrocelular,)
        dba.get_cursor().execute(consulta,numero)
        password=""
        for j in dba.get_cursor().fetchone():
            password=j
        print(f'Tu contraseña es: {base64.decodebytes(password.encode("UTF-8")).decode("utf-8")}')
    else:
        print("Tu numero de celular no se encuentra en la base.")    

