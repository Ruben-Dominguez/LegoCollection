from tkinter import *
import mysql.connector
from datetime import date
from PIL import ImageTk, Image

TABLAS = ["HISTORIAL", "OTRO", "PIEZA", "PRODUCTO", "SERIE", "SET_DE_LEGO"]

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

my_cursor = db.cursor(buffered=True)

my_cursor.execute("DROP TABLE IF EXISTS HISTORIAL;")
my_cursor.execute("DROP TABLE IF EXISTS OTRO;")
my_cursor.execute("DROP TABLE IF EXISTS PIEZA;")
my_cursor.execute("DROP TABLE IF EXISTS PRODUCTO;")
my_cursor.execute("DROP TABLE IF EXISTS SERIE;")
my_cursor.execute("DROP TABLE IF EXISTS SET_DE_LEGO;")

my_cursor.execute(
    "CREATE TABLE HISTORIAL (Producto_ID INTEGER NOT NULL, Fecha_ped CHAR(10) NULL, Fecha_ent CHAR(10) NULL);")
my_cursor.execute("ALTER TABLE HISTORIAL ADD CONSTRAINT XPKHISTORIAL PRIMARY KEY (Producto_ID);")

my_cursor.execute(
    "CREATE TABLE OTRO (Articulo_ID INTEGER NOT NULL, Serie_nombre CHAR(50) NOT NULL, Nombre CHAR(50) NULL, Tipo CHAR(50) NULL);")
my_cursor.execute("ALTER TABLE OTRO ADD CONSTRAINT XPKOTRO PRIMARY KEY (Articulo_ID);")

my_cursor.execute("CREATE TABLE PIEZA (Pieza_ID INTEGER NOT NULL, Color CHAR(50) NULL, Tipo_material CHAR(50) NULL);")
my_cursor.execute("ALTER TABLE PIEZA ADD CONSTRAINT XPKPIEZA PRIMARY KEY (Pieza_ID);")

my_cursor.execute("CREATE TABLE PRODUCTO (Producto_ID INTEGER NOT NULL, Costo INTEGER NULL);")
my_cursor.execute("ALTER TABLE PRODUCTO ADD CONSTRAINT XPKPRODUCTO PRIMARY KEY (Producto_ID);")

my_cursor.execute("CREATE TABLE SERIE (Serie_nombre CHAR(50) NOT NULL, Licencia  CHAR(50) NULL);")
my_cursor.execute("ALTER TABLE SERIE ADD CONSTRAINT XPKSERIE PRIMARY KEY (Serie_nombre);")

my_cursor.execute(
    "CREATE TABLE SET_DE_LEGO (Set_ID INTEGER NOT NULL, Nombre CHAR(80) NULL, Num_de_piezas INTEGER NULL, Edad CHAR(50) NULL, Serie_nombre CHAR(50) NOT NULL);")
my_cursor.execute("ALTER TABLE SET_DE_LEGO ADD CONSTRAINT XPKSET_DE_LEGO PRIMARY KEY (Set_ID);")

my_cursor.execute("ALTER TABLE OTRO ADD (CONSTRAINT R_2 FOREIGN KEY (Serie_nombre) REFERENCES SERIE (Serie_nombre));")
my_cursor.execute("ALTER TABLE OTRO ADD (CONSTRAINT R_20 FOREIGN KEY (Articulo_ID) REFERENCES PRODUCTO (Producto_ID));")
my_cursor.execute("ALTER TABLE PIEZA ADD (CONSTRAINT R_21 FOREIGN KEY (Pieza_ID) REFERENCES PRODUCTO (Producto_ID));")

db.commit()

# for t in TABLAS:
#     my_cursor.execute(f"DESCRIBE {t}")
#     print(t)
#     for x in my_cursor:
#         print(x)

my_cursor.execute("INSERT INTO SERIE (Serie_nombre, Licencia) VALUES('CREATOR', 'LEGO CR');")
my_cursor.execute("INSERT INTO SERIE (Serie_nombre, Licencia) VALUES('POWERED UP', 'DISNEY TM');")
my_cursor.execute("INSERT INTO SERIE (Serie_nombre, Licencia) VALUES('DISNEY', 'DISNEY TM');")
my_cursor.execute("INSERT INTO SERIE (Serie_nombre, Licencia) VALUES('HARRY POTTER', 'NBCU LLC');")
my_cursor.execute("INSERT INTO SERIE (Serie_nombre, Licencia) VALUES('LEGO', 'LEGO CR');")

my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10276, 12499);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10276, 'Coliseo', 9036, '18+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10278, 4999);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10278, 'Comisaría de Policía', 2923, '18+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(71044, 7999);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(71044, 'Tren y Estación Disney', 2925, '12+', 'POWERED UP');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(71040, 8499);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(71040, 'Castillo Disney', 4080, '16+', 'DISNEY');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(71043, 8499);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(71043, 'Castillo de Hogwarts TM', 6020, '16+', 'HARRY POTTER');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10261, 7999);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10261, 'Montaña rusa', 4124, '16+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10255, 5699);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10255, 'Gran plaza', 4002, '16+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10264, 2569);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10264, 'Taller de la Esquina', 2569, '16+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10272, 6299);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10272, 'Old Trafford', 3898, '16+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10273, 3231);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10273, 'Casa Encantada de la Feria', 3231, '16+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(10280, 1299);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(10280, 'Ramo de Flores', 756, '18+', 'CREATOR');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(40173, 271);")
my_cursor.execute(
    "INSERT INTO SET_DE_LEGO (Set_ID, Nombre, Num_de_piezas, Edad, Serie_nombre) VALUES(40173, 'Marco de fotos LEGO CR Iconic', 268, '7+', 'LEGO');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(850808, 119);")
my_cursor.execute(
    "INSERT INTO OTRO (Articulo_ID, Serie_nombre, Nombre, Tipo) VALUES(850808, 'LEGO', 'Llavero dorado LEGO', 'Llavero');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(853912, 219);")
my_cursor.execute(
    "INSERT INTO OTRO (Articulo_ID, Serie_nombre, Nombre, Tipo) VALUES(853912, 'LEGO', 'Bandeja para Polos', 'Bandeja para Polos');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(40172, 299);")
my_cursor.execute(
    "INSERT INTO OTRO (Articulo_ID, Serie_nombre, Nombre, Tipo) VALUES(40172, 'LEGO', 'Calendario de ladrillos 2017', 'Bandeja para Polos');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(4616581, 1);")
my_cursor.execute("INSERT INTO PIEZA (Pieza_ID, Color, Tipo_material) VALUES(4616581, 'Verde obscuro', 'Solido');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(6240219, 3);")
my_cursor.execute("INSERT INTO PIEZA (Pieza_ID, Color, Tipo_material) VALUES(6240219, 'Cafe', 'Transparente');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(6268823, 10);")
my_cursor.execute("INSERT INTO PIEZA (Pieza_ID, Color, Tipo_material) VALUES(6268823, 'Verde', 'Semi-Flex');")
my_cursor.execute("INSERT INTO PRODUCTO (Producto_ID,Costo) VALUES(370326, 17);")
my_cursor.execute("INSERT INTO PIEZA (Pieza_ID, Color, Tipo_material) VALUES(370326, 'Negro', 'Solido');")

# for t in TABLAS:
#     my_cursor.execute(f"SELECT * FROM {t}")
#     print(t)
#     for x in my_cursor:
#         print(x)

# GLOBALES GLOBALES
botones_agregar = []
disponibles_productos = []
ids = []

my_cursor.execute("SELECT * FROM SET_DE_LEGO")
for x in my_cursor:
    ids.append(x[0])
my_cursor.execute("SELECT * FROM PIEZA")
for x in my_cursor:
    ids.append(x[0])
my_cursor.execute("SELECT * FROM OTRO")
for x in my_cursor:
    ids.append(x[0])


def agregar(x, tipo):
    global disponibles_productos, botones_agregar, ids

    day = str(date.today())

    my_cursor.execute(f"INSERT INTO HISTORIAL (Producto_ID, Fecha_ped, Fecha_ent) VALUES({ids[x]}, '{day}' , '{day}');")

    if tipo == "set":
        my_cursor.execute(f"DELETE FROM SET_DE_LEGO WHERE Set_ID={ids[x]}")
    elif tipo == "pieza":
        my_cursor.execute(f"DELETE FROM PIEZA WHERE Pieza_ID={ids[x]}")
    else:
        my_cursor.execute(f"DELETE FROM OTRO WHERE Articulo_ID={ids[x]}")

    db.commit()
    print("Historial")
    my_cursor.execute(f"SELECT * FROM HISTORIAL")
    for i in my_cursor:
        print(i)

    print("Disponibles")
    my_cursor.execute(f"SELECT * FROM SET_DE_LEGO")
    for i in my_cursor:
        print(i)

    disponibles_productos[x].destroy()


# FUNCIONES
def verHistorial():
    global historial_frame, disponibles_frame

    historial_frame.destroy()
    disponibles_frame.destroy()

    historial_frame = Frame(main_frame, width=800, height=600, relief=FLAT, bg="#DFDFDF")  # el frame de los disponibles
    c = Canvas(historial_frame, height=600)  # el canvas donde va nuestro frame anterior
    scrollbar = Scrollbar(historial_frame, orient="vertical", command=c.yview)  # el widget de scrollbar
    sf = Frame(c)  # metemos el canvas, que contiene un frame
    sf.bind("<Configure>", lambda e: c.configure(scrollregion=c.bbox("all")))  # configuramos el evento con bind
    c.create_window((0, 0), window=sf, anchor="nw")  # finalmente configuramos el canvas
    c.configure(yscrollcommand=scrollbar.set)
    c.pack(side="left", fill="both", expand=1)
    scrollbar.pack(side="right", fill=Y)
    historial_frame.grid(column=0, row=1, columnspan=2, sticky=NSEW)

    my_cursor.execute("SELECT * FROM HISTORIAL")

    historial_productos = []
    for set in my_cursor:
        prod = f"Numero de producto: {set[0]}"
        fecha = f"Fecha: {set[1]}"

        historial_productos.append(Frame(sf, bg="black", relief=FLAT, bd=3, width=850))
        historial_productos[-1].pack(fill=X)
        image1 = Image.open(f"LegoImg/{set[0]}.png")
        resize = image1.resize((300, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize)
        label1 = Label(historial_productos[-1], image=test, width=300, height=300)
        label1.image = test
        label1.pack(fill=X)
        Label(historial_productos[-1], anchor=W, font="Fixedsys 18 bold", text=prod).pack(fill=X)
        Label(historial_productos[-1], anchor=W, font="Fixedsys 18 bold", text=fecha).pack(fill=X)



def verDisponibles():
    global historial_frame, disponibles_frame, botones_agregar, disponibles_productos, ids

    historial_frame.destroy()
    disponibles_frame.destroy()

    ids = []
    my_cursor.execute("SELECT * FROM SET_DE_LEGO")
    for x in my_cursor:
        ids.append(x[0])
    my_cursor.execute("SELECT * FROM PIEZA")
    for x in my_cursor:
        ids.append(x[0])
    my_cursor.execute("SELECT * FROM OTRO")
    for x in my_cursor:
        ids.append(x[0])

    disponibles_frame = Frame(main_frame, width=800, height=600, relief=FLAT,
                              bg="#DFDFDF")  # el frame de los disponibles
    c = Canvas(disponibles_frame, height=600)  # el canvas donde va nuestro frame anterior
    scrollbar = Scrollbar(disponibles_frame, orient="vertical", command=c.yview)  # el widget de scrollbar
    sf = Frame(c, width=800)  # metemos el canvas, que contiene un frame
    sf.bind("<Configure>", lambda e: c.configure(scrollregion=c.bbox("all")))  # configuramos el evento con bind
    c.create_window((0, 0), window=sf, anchor="nw")  # finalmente configuramos el canvas
    c.configure(yscrollcommand=scrollbar.set)
    c.pack(side="left", fill="both", expand=1)
    scrollbar.pack(side="right", fill=Y)
    disponibles_frame.grid(column=0, row=1, columnspan=2, sticky=NSEW)


    # SETS DE LEGO
    my_cursor.execute("SELECT * FROM SET_DE_LEGO")
    i = 0
    botones_agregar = []
    disponibles_productos = []
    for set in my_cursor:
        num_set = f"Numero de set: {set[0]}"
        name_set = f"Nombre: {set[1]}"
        num_piezas = f"Numero de piezas: {set[2]}"
        edad = f"Edad: {set[3]}"
        serie = f"Serie: {set[4]}"

        disponibles_productos.append(Frame(sf, bg="black", relief=FLAT, bd=3, width=850))
        botones_agregar.append(Button(disponibles_productos[-1], fg="white", bg="blue", text="Agregar",
                                      command=lambda num=i: agregar(num, "set")))

        disponibles_productos[-1].pack(fill=X)
        image1 = Image.open(f"LegoImg/{set[0]}.png")
        resize = image1.resize((300, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize)
        label1 = Label(disponibles_productos[-1], image=test, width=300, height=300)
        label1.image = test
        label1.pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=num_set).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=name_set).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=num_piezas).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=edad).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=serie).pack(fill=X)
        botones_agregar[-1].pack(fill=X)
        i += 1

    # PIEZAS
    my_cursor.execute("SELECT * FROM PIEZA")
    for set in my_cursor:
        pieza = f"Numero de pieza: {set[0]}"
        color = f"Color: {set[1]}"
        material = f"Material: {set[2]}"

        disponibles_productos.append(Frame(sf, bg="black", relief=FLAT, bd=3, width=850))
        botones_agregar.append(Button(disponibles_productos[-1], fg="white", bg="blue", text="Agregar",
                                      command=lambda num=i: agregar(num, "pieza")))

        disponibles_productos[-1].pack(fill=X)
        image1 = Image.open(f"LegoImg/{set[0]}.png")
        resize = image1.resize((300, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize)
        label1 = Label(disponibles_productos[-1], image=test, width=300, height=300)
        label1.image = test
        label1.pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=pieza).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=color).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=material).pack(fill=X)
        botones_agregar[-1].pack(fill=X)
        i += 1

    # OTRO
    my_cursor.execute("SELECT * FROM OTRO")
    for set in my_cursor:
        otro = f"Numero de Articulo: {set[0]}"
        serie = f"Serie: {set[1]}"
        nombre = f"Nombre: {set[2]}"
        tipo = f"Tipo: {set[3]}"

        disponibles_productos.append(Frame(sf, bg="black", relief=FLAT, bd=3, width=850))
        botones_agregar.append(Button(disponibles_productos[-1], fg="white", bg="blue", text="Agregar",
                                      command=lambda num=i: agregar(num, "otro")))

        disponibles_productos[-1].pack(fill=X)
        image1 = Image.open(f"LegoImg/{set[0]}.png")
        resize = image1.resize((300, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resize)
        label1 = Label(disponibles_productos[-1], image=test, width=300, height=300)
        label1.image = test
        label1.pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=otro).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=serie).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=nombre).pack(fill=X)
        Label(disponibles_productos[-1], anchor=W, font="Fixedsys 18 bold", text=tipo).pack(fill=X)
        botones_agregar[-1].pack(fill=X)
        i += 1


# DEFINICION DE ROOT
root = Tk()
root.title("Lego Shop History!")
root.minsize(600, 600)
root.resizable(0, 0)
main_frame = Frame(root, width=800, height=600)

# GLOBALES
historial_frame = Frame(main_frame, width=700, height=600, relief=FLAT, bg="#DFDFDF")
disponibles_frame = Frame(main_frame, width=700, height=600, relief=FLAT, bg="#DFDFDF")

btn_disponibles = Button(main_frame, text="Disponibles", command=verDisponibles, width=46)
btn_historial = Button(main_frame, text="Historial", command=verHistorial, width=46)

# COLOCACION DE ELEMENTOS EN PANTALLA
main_frame.grid(column=0, row=0, columnspan=2, rowspan=2)
btn_disponibles.grid(column=0, row=0)
btn_historial.grid(column=1, row=0)

# MAIN
verDisponibles()

root.mainloop()
