from tkinter import *
from tkinter import filedialog, messagebox
import tkinter

from src.PatronSingleton.Singleton import Singleton
from src.Symbol.Error import Error
from src.Symbol.EntornoTabla import EntornoTabla
from gramatica import gramatica

ventana=Tk()
textE=Text()
textS=Text()

def generarVentana():
    global ventana,textE,textS
    ventana.configure(background="#008080")
    ancho=1400
    alto=700
    x=ventana.winfo_screenwidth()
    #calculamos la coordenada X donde se posicionara la ventana
    x=(x-ancho)/2
    y=ventana.winfo_screenheight()
    #calculamos la coordenada Y donde se posicionara la ventana
    y=(y-alto)/2
    ventana.geometry('%dx%d+%d+%d' % (ancho, alto, x, y))
    ventana.title("OLC2 DB_Rust")

    #para el text area de entrada
    frameEntrada=Frame(ventana)
    frameEntrada.place(x=200,y=80)
    scrollbar1=Scrollbar(frameEntrada, orient='horizontal')
    scrollbar1.pack(side=BOTTOM, fill='x')
    textE=Text(frameEntrada, font=("Calibri, 14"), wrap="none", xscrollcommand=scrollbar1.set,width=58,height=25)
    textE.pack()
    scrollbar1.config(command=textE.xview)

    #para el text area de salida
    frameSalida=Frame(ventana)
    frameSalida.place(x=900,y=80)
    scrollbar2=Scrollbar(frameSalida, orient='horizontal')
    scrollbar2.pack(side=BOTTOM, fill='x')
    textS=Text(frameSalida, font=("Calibri, 14"),background="#696969", wrap="none", xscrollcommand=scrollbar2.set,width=43,height=25,state=DISABLED)
    textS.pack()
    scrollbar2.config(command=textS.xview)


    #botones
    b1=Button(ventana,text="Cargar",command=cargarArchivo,font=("Verdana",10),borderwidth=3,background="beige").place(x=300,y=35,height=40,width=100)
    b2=Button(ventana,text="Analizar",command=Ejecutar,font=("Verdana",10),borderwidth=3,background="beige").place(x=980,y=35,height=40,width=100)
    b3=Button(ventana,text="Reporte de Errores",font=("Verdana",10),borderwidth=3,background="beige").place(x=20,y=300,height=40,width=150)
    b4=Button(ventana,text="Reporte de Tokens",font=("Verdana",10),borderwidth=3,background="beige").place(x=20,y=360,height=40,width=150)
    
    
    #Labels
    Label(ventana,bg="#008080",fg="white",relief="flat" ,text="Entrada:", font=("arial italic", 18) ).place(x=200,y=40)
    Label(ventana,bg="#008080",fg="white",relief="flat" ,text="Salida:", font=("arial italic", 18) ).place(x=900,y=40)


    ventana.mainloop()

def cargarArchivo():
    global texto,textE
    archivo=filedialog.askopenfilename(
        title="Por favor seleccine un archivo txt con el codigo fuente",
        initialdir="./",
        filetypes=(
            ("Archivo TXT","*.txt"),("Todos los archivos","*.*")
        )
    )
    print(archivo)
    if archivo=="":
        messagebox.showerror(message="No selecciono ningun archivo, por favor vuelva a intentarlo",title="Error")
    else:
        contenido=open(archivo,"r",encoding='UTF-8')
        temp=contenido.read()
        textE.delete('1.0', END)
        textE.insert(END,temp)
        contenido.close()

def Ejecutar():
    global texto,analizado,textE, textS
    s=Singleton.getInstance()
    s.reset()
    texto=textE.get("1.0", "end-1c")
    if texto=="":
        messagebox.showerror(message="No hay texto en consola por ejecutar",title="Error")
    else:
        textS.config(state=NORMAL)
        textS.delete('1.0', END)
        textS.config(state=DISABLED)
        EntornoPadre=EntornoTabla(None)
        AST = gramatica.parse(texto)
        #print(AST)
        for i in AST:
            try:
                i.Ejecutar(EntornoPadre)
            except:
                print("error.........................")
        textS.config(state=NORMAL)
        textS.delete('1.0', END)
        textS.insert(END,s.getConsola())
        textS.config(state=DISABLED)

        errores:Error=s.getErrores()
        for e in errores:
            print(e.descripcion,e.tiempo," linea: ",e.linea," columna: ",e.columna)
        
     
if __name__=='__main__':
    generarVentana()
