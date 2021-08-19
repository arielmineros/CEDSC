from enum import unique
from re import T
import connection as con
db = con.client["Evaluacion01"]
mycol = db["CE"]

def switch_option(option):
    # Insertar un CE
    def insert_ce():
        print("Ha elegido insertar un centro escolar\n")
        _id = int(input("Ingrese el código del C.E: "))
        name = str(input("Ingrese el nombre del C.E: "))
        dep = str(input("Ingrese el departamento: "))
        mun = str(input("Ingrese el municipio: "))
        dictionary = {"_id":_id, "Nombre":name, "Departamento":dep, "Municipio":mun}
        mycol.insert_one(dictionary)
        if mycol.find_one({"_id":_id}):
            print("\nCE ingresado con éxito")
        input()
        
    # Ver todos los CE
    def show_ce():
        print("Ha elegido ver los centros escolares\n")
        for i in mycol.find({},{"_id":0, "Nombre":1,"Departamento":1}):
            print(i)
        input()

    # Actualizar un CE
    def update_ce():
        print("Ha elegido actualizar un centro escolar\n")
        _id = int(input("Ingrese el código del centro escolar: "))
        myquery = {"_id":_id}
        _nombre = str(input("Escriba el nombre del C.E: "))
        _dep = str(input("Escriba el departamento: "))
        _mun = str(input("Escriba el municipio: "))
        newvalue = {"$set":{"Nombre":_nombre, "Departamento":_dep, "Municipio":_mun}}
        mycol.update_one(myquery,newvalue)
        if mycol.find({"_id":_id}):
            print("CE actualizado con éxito")
        print(mycol.find_one(myquery))
        input()

    # Borrar un CE
    def delete_ce():
        print("Ha elegido eliminar un CE\n")
        _id = int(input("Ingrese el id del CE: "))
        myquery = {"_id":_id}
        x = mycol.delete_one(myquery)
        print(x.deleted_count, "CE se ha eliminado")
        input()
    # En caso que se ingrese dato erróneo
    def default():
        print("Elija un opción válida")
    dict = {
        1: insert_ce,
        2: show_ce,
        3: update_ce,
        4: delete_ce,
    }
    return dict.get(option,default)()
    