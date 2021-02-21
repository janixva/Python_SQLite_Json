import sqlite3
import json
from libary.ships import Ship


# --------------------------- END Call clases / import ------------------------------

# --------------------------- MENU ------------------------------

def show_menu():
    print()
    print('Buenas Tardes, aqui selecionaremos que gran grupo queremos entrar y luego nos dara las opciones de este')
    print()
    print(' 1. CREAR Tablas y columnas ')
    print(' 2. AÑADIR valores nuevos')
    print(' 3. ACTUALIZAR Valores de datos ya exitentes')
    print(' 4. BORRAR datos, columnas, tablas o la base de datos entera')
    print(' 5. Consultar datos')
    print(' 6. Json Menu (para importar data desde el json que tenemos)')
    print()
    print('0. Salir')

    user_response = int(input('Opcion? '))

    return user_response


def execute_option(opcion):
    if opcion == 1:
        creacion_menu()
    elif opcion == 2:
        add_menu()
    elif opcion == 3:
        update_menu()
    elif opcion == 4:
        delete_menu()
    elif opcion == 4:
        delete_menu()
    elif opcion == 5:
        search_menu()
    elif opcion == 6:
        json_menu()



    elif opcion == 0:
        salir()

    print()


def creacion_menu():
    print()
    print('--------------------------------------------')
    print()
    print("--MENU DE CREACION DE TABLAS--")
    print()
    print(' MODO "creation", escribe el num al que queires acceder:')
    print(' 1. Crea las 3 tablas predefinidas (LAS ELIMINA Y LAS VUELVE A CREAR SI YA ESTAN CREADAS) ')
    print(' 2. Crear una tabla defininedo los parametros')
    print()
    print()
    print(' 0. Volver al Menu principal')

    user_response_creation = int(input('Opcion? '))

    # return user_response_creation

    if user_response_creation == 1:
        crear_table1()
    elif user_response_creation == 2:
        crear_table1()
    elif user_response_creation == 0:
        execute_option()


def add_menu():
    print()
    print('--------------------------------------------')
    print()
    print("--MENU DE AÑADIR DATOS--")
    print()
    print(' 1. "insert_ships"---AÑADIR MANUALMENTE a la tabla SHIPS todos los parametros ')


    print(' ')

    print()
    print('0. Volver al Menu principal')

    user_response_creation = int(input('Opcion? '))

    # return user_response_creation

    if user_response_creation == 1:
        insert_ships()


    elif user_response_creation == 0:
        execute_option()


def update_menu():
    print()
    print('--------------------------------------------')
    print()
    print("--MENU DE Update DATOS--")
    print()
    print(' 1. Cambiar el origen del Barco usando el nombre y tier_number "update_ship_table" ')
    print(' 2. Cambiar el origen y tipo preguntandonos el id y nombre update_ship_table2 ')
    print(' 3. Cambiar nombre del barco id ""88888"" usando "clases!!!!" --''MIRAR EL CODIGO''-- ')
    print(' ')
    print(" ")
    print(' 0. Volver al Menu principal')

    user_response_creation = int(input('Opcion? '))

    if user_response_creation == 1:
        update_ship_table()
    elif user_response_creation == 2:
        update_ship_table2()
    elif update_ship_table_class == 3:
        update_ship_table_class()
    elif user_response_creation == 0:
        execute_option()


def delete_menu():
    print()
    print('--------------------------------------------')
    print()
    print("--MENU DE BORAR DATOS--")
    print()
    print(' 1. Borrar la fila o filas q contengan el nombre o el id establecido ')
    print(' 2. Borrar la tabla tiers ')
    print(' 3. Borrar todos los datos en la tabla ship pero no la tabla en si ')
    print(' 4. Borrar los barcos que tengan una velocidad igual o inferior a un numero establecido ')
    print(' ')

    print()
    print('0. Volver al Menu principal')

    user_response_creation = int(input('Opcion? '))

    if user_response_creation == 1:
        delete_menu1()
    elif user_response_creation == 2:
        delte_table1()
    elif user_response_creation == 3:
        delete_reset_data()
    elif user_response_creation == 4:
        delete_low_velocity()
    elif user_response_creation == 0:
        execute_option()


def search_menu():
    print()
    print('--------------------------------------------')
    print()
    print("--MENU DE BUSCAR/CONSULTAR DATOS--")
    print()
    print(' 1. buscar un barco con la id que quieras ')
    print(' 2. buscar en la tabla tiers con el coste ')
    print(' 3. Consultar todas los registros de ships ')

    print(' ')

    print()
    print('0. Volver al Menu principal')

    user_response_creation = int(input('Opcion? '))

    if user_response_creation == 1:
        buscar1()
    elif user_response_creation == 2:
        buscar2()
    elif user_response_creation == 3:
        buscar_all_ships()
    elif user_response_creation == 0:
        execute_option()


def json_menu():
    print()
    print('--------------------------------------------')
    print()
    print("--MENU DE JSON--")
    print('')
    print('!!Si ya hay datos ya introducidos en la tabla TYPESva a dar error por duplciacion de primarykey!!')
    print('!! En ese caso, usar la fuincion 1 de este menu para borrar y poder introducir todo de nuevo')
    print('')
    print(' 1. BORRAR toda la data de las 3 tablas ')
    print(' 2. IMPORTAR data para la tabla TIERS json ')
    print(' 3. IMPORTAR data para la tabla TYPE json----- !!Si ya hay datos ya introducidos va a dar error por duplciacion de primarykey!!')
    print(' 4. IMPORTAR data para la tabla SHIPS json ')
    print(' 3.  ')

    print(' ')

    print()
    print('0. Volver al Menu principal')

    user_response_creation = int(input('Opcion? '))

    json_doc = 'libary/battleships.json'

    if user_response_creation == 1:
        json_delete_all()
    elif user_response_creation == 2:
        json_import_tiers_data(json_doc)
    elif user_response_creation == 3:
        json_import_type_data(json_doc)

    elif user_response_creation == 4:
        json_import_ship_data(json_doc)



    elif user_response_creation == 0:
        execute_option()


# --------------------------- END MENUS ------------------------------


# ---------------------------- CRUD Comands -------------------------------

# --------------- CREACION de Tablas


def crear_table1():
    with conn:
        # c.execute("""DROP TABLE IF EXISTS ship, type, tiers""")

        c.execute("""DROP TABLE IF EXISTS tiers""", )
        c.execute("""DROP TABLE IF EXISTS type""", )
        c.execute("""DROP TABLE IF EXISTS ships""", )

        c.execute("""CREATE TABLE IF NOT EXISTS ships(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre text NOT NULL,                    
                    origin text NOT NULL,
                    type_class text NOT NULL,
                    tier_number integer NOT NULL,
                    max_velocity integer,                    
                    FOREIGN KEY (tier_number)
                        REFERENCES tiers (tier_number),
                    FOREIGN KEY (type_class)
                        REFERENCES type (type_class)
                    
                    
         )""")

        c.execute("""CREATE TABLE IF NOT EXISTS type(                             
                             type_class TEXT PRIMARY KEY NOT NULL,
                             full_name text NOT NULL,                    
                             origin text NOT NULL,
                             photo text,
                             video text,
                             countrys_owners text,
                             wars text,
                                                
                             FOREIGN KEY (type_class)
                                 REFERENCES ships (type_class)


                  )""")

        c.execute("""CREATE TABLE IF NOT EXISTS tiers(
                            id_tiers INTEGER PRIMARY KEY AUTOINCREMENT,
                            tier_number INTEGER NOT NULL,
                            cost_level text,
                            FOREIGN KEY (tier_number)
                                 REFERENCES ships (tier_number)
                            
                 )""")
    print("")
    print("")
    print("")

    print('-------Se han creado 3 tablas vacias!')
    print("")
    print("")


# -------------- END creacion de Tablas

# -------------- AÑADIR datos




def insert_ships():
    with conn:
        c.execute("INSERT INTO ships VALUES (:id,:nombre, :origin, :type_class, :tier_number, :max_velocity)",
                  {'id': input("introduce id:"), 'nombre': input("introduce nombre:"),
                   'origin': input("introduce origin añadir:"), 'type_class': input("introduce type_class:"),
                   'tier_number': input("introduce tier_number a añadir:"),
                   'max_velocity': input("introduce max_velocity a añadir:")})


# -------------- END AÑADIR datos


# -------------- ACTUALIZAR datos


def update_ship_table():  # Update especificando el id y nombre
    with conn:
        c.execute("""UPDATE ships SET origin = :origin
                    WHERE nombre = :nombre AND tier_number = :tier_number""",
                  {'origin': input('Change origin:'), 'nombre': input('Del ship llamado:'),
                   'tier_number': input('Con el tier number:')})
        c.execute("""SELECT * FROM ships WHERE nombre""")
        print(c.fetchall())


def update_ship_table2():  # Update origen y type preguntando el id y nombre
    with conn:
        c.execute("""UPDATE ships SET origin = :origin
                    WHERE nombre = :nombre AND id = :id""",
                  {'origin': input('Change origin:'),
                   'nombre': input('Del ship llamado:'),
                   'id': input('Con el id number:')})


def update_ship_table_class():

    # --- ESTE ES EL EJEMPO PARA MOSTRAR QUE FUNCIONA EL USO DE LAS CLASES y cambiar el nombre, NADA MAS-----
    with conn:
        ship_1 = Ship(88888, 'jan', 'jan', 'jan', 2, 22)
        c.execute("""UPDATE ships SET nombre = :nombre
                    WHERE type_class = :type_class AND tier_number = :tier_number""",
                  {'nombre': input('Change name:'), 'type_class': ship_1.type_class, 'tier_number': ship_1.tier_number})


# -------------- END ACTUALIZAR datos


# -------------- BORRAR datos

def delete_menu1():
    with conn:
        print("Eliminar la fila del ship:")
        c.execute("""DELETE FROM ships WHERE nombre = :nombre OR id = :id""",
                  {'nombre': input('Del ship llamado:'), 'id': input('o que tenga el ship id:')})


def delte_table1():
    with conn:
        c.execute("""DROP TABLE tiers""", )
        c.execute("""DROP TABLE type""", )
        c.execute("""DROP TABLE ships""", )
        print("")
        print("")
        print("Se ha eliminado las 3 tablas de Battleships! ")
        print("")
        print("")


def delete_reset_data():
    with conn:
        c.execute("""DELETE FROM Ships""")
        print("")
        print("")
        print("Se Han Borrado todos los datos de la tabla Ships")
        print("")
        print("")


def delete_low_velocity():
    with conn:
        c.execute("""DELETE FROM ships  WHERE "max_velocity" <= :max_velocity""",
                  {'max_velocity': input('Borrar el barco que tenga una velocidad igual o inferior a:')})
        print("")
        print("")
        print("Se han borrado los datos de las velocidades inferiores al num establecido")
        print("")
        print("")


# -------------- END BORRAR datos


# -------------- BUSCAR datos


def buscar1():
    with conn:
        c.execute("SELECT * FROM ships WHERE nombre=:name",
                  {'name': input("introduce un nombre del barco a consultar")})
        print(c.fetchall())


def buscar2():
    with conn:
        c.execute("SELECT * FROM tiers WHERE cost_level=:cost_level", {'cost_level': input(
            "introduce un cost_level para mostrar los tiers que quieras(low, medium, high, usa_level)")})
        print(c.fetchall())


def buscar_all_ships():
    with conn:
        c.execute("SELECT * FROM ships")
        print(c.fetchall())


# -------------- END BUSCAR datos

# ---- IMPORT JSON --------

def json_delete_all():
    with conn:
        c.execute("DELETE FROM ships")
        c.execute("DELETE FROM tiers")
        c.execute("DELETE FROM type")
        print("Se ha borrado la data de las tablas: ships, tiers and type")


def json_import_tiers_data(json_doc):
    with conn:
        data = json.load(open(json_doc, encoding='utf8'))  # si no pongo ''   encoding='utf8'  '' no funciona
        for batt in data['tiers']:

            c.execute('INSERT INTO tiers (tier_number,cost_level) VALUES (:tier_number,:cost_level)',
                      {'tier_number': batt['tier_number'], 'cost_level': batt['cost_level']})
        print('se han añadido todas los datos de tiers')


def json_import_type_data(json_doc):
    with conn:
        data = json.load(open(json_doc, encoding='utf8'))
        for batt in data['warship_types_introduction']['warships_types']:
            c.execute(
                'INSERT INTO type (type_class,full_name,origin,photo,video) VALUES (:type_class, :full_name, :origin, :photo, :video)',
                {'type_class': batt['english_name'], 'full_name': batt['info']['nombrecompleto'],
                 'origin': batt['info']['origen'], 'photo': batt['photo2'], 'video': batt['video']})
        print('se han añadido todas los datos de types')


def json_import_ship_data(json_doc):
    with conn:
        data = json.load(open(json_doc, encoding='utf8'))
        for batt in data['tiers']:
            for ships in batt['tier']:
                c.execute(
                    'INSERT INTO ships (nombre,origin,type_class,tier_number,max_velocity) VALUES (:nombre, :origin, :type_class, :tier_number, :max_velocity)',
                    {'nombre': ships['ship']['name'], 'origin': ships['ship']['origin'],
                     'type_class': ships['ship']['type_class'], 'tier_number': ships['ship']['tier_number'], 'max_velocity': ships['ship']['max_velocity']})
        print('se han añadido todas los datos de ships')

            # ---- END IMPORT JSON -----

            # ---------------------------- END CRUD Comands -------------------------------

            # --------------------------- Inicio Script --------------------------------------------


if __name__ == '__main__':
    conn = sqlite3.connect('libary/warship.db')
    c = conn.cursor()
    fin = False
    while not fin:
        opcion = show_menu()
        if opcion == 0:
            fin = True
            conn.close()
        else:
            execute_option(opcion)
