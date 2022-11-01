#Importacion de librerias



import tkinter 
import os     
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import *
import webbrowser




#Creacion de funciones Archivo

def archivo_nuevo():
    
    editor.delete(1.0,END)


def archivo_abrir():

    documento = askopenfile(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 

    if documento != None:

        editor.insert(1.0, documento.read())
        

def archivo_guardar():
   # documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])
    #print(documento.write(editor.get(1.0, END)))
    f = asksaveasfile(mode='w',defaultextension=".txt")
    if (f):
        f.write("Archivo guardado con exito")
        f.close()
    

    
    
def archivo_guardarcomo():
    documento = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")])
    
    
#Creacion de funciones Editar

def editar_deshacer():

    editor.edit_undo()

def editar_rehacer():

    editor.edit_redo()
    
def editar_copiar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())
    

def editar_pegar():

    editor.insert(INSERT, editor.clipboard_get())

def editar_cortar():

    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

    editor.delete("sel.first", "sel.last")




#Creacion de funciones Ayuda

def ayuda_informacion():

    messagebox.showinfo("Informacion bloc de notas plus","Dicha aplicacion es generada para el uso de un bloc de notas"
                        "En el cual se pueda realizar la lectura y escritura de datos de texto"
                        "\n\n" 
                        "Bloc de notas de  VERSION 1.1 2022. Todos los derechos reservados. ")
                        

def ayuda_manual():
    messagebox.showinfo("Bloc de notas de  VERSION 1.1 2022. Todos los derechos reservados.")
    
def ayuda_integrantes():
    messagebox.showinfo("Desarrollado por:","El siguiente proyeto fue desarrollado por:"
                        "\n\n" 
                        "Billy Alberto Morales Santos          No. Carné: 7690-20-712"
                        "\n\n" 
                        "Jose Leonel Salazar Tejeda              No. Carné7690-22-8974"
                        "\n\n" 
                        "Remy Briyan Castillo Hernandez      No. Carné 7690-15-15298")

def link_video():
    webbrowser.open("https://youtu.be/epu5ue33U58")
def link():
    webbrowser.open("https://github.com/josetejeda97/bloc-de-notas")
def link_manual():
    webbrowser.open("https://umgt-my.sharepoint.com/:b:/g/personal/jsalazart3_miumg_edu_gt/ERvW9pRNakZEinE5LJ4zUxEBDuayGgBEeVPxipyJNIm8dQ?e=14XNSw")



if __name__ == "__main__":



    ventana = Tk()



    menubar = Menu(ventana)

    archivo = Menu(menubar, tearoff=0)

    archivo.add_command(label="Nuevo     ", command=archivo_nuevo)

    archivo.add_command(label="Abrir     ", command=archivo_abrir)

    archivo.add_command(label="Guardar     ", command=archivo_guardar)
    archivo.add_command(label="Guardar Como     ", command=archivo_guardarcomo)
    archivo.add_separator()
    archivo.add_command(label="Salir (Alt + F4)    ", command=ventana.quit)
    

    menubar.add_cascade(label="Archivo", menu=archivo)



    editar = Menu(menubar, tearoff=0)

    editar.add_command(label="Deshacer (Ctrl + Z)     ", command=editar_deshacer)

    editar.add_command(label="Rehacer (Ctrl + Y)    ", command=editar_rehacer)

    editar.add_separator()

    editar.add_command(label="Copiar (Ctrl + C)    ", command=editar_copiar)

    editar.add_command(label="Pegar (Ctrl + V)     ", command=editar_pegar)

    editar.add_command(label="Cortar (Ctrl + X)    ", command=editar_cortar)

    menubar.add_cascade(label="Edición", menu=editar)



    ayuda = Menu(menubar, tearoff=0)

    ayuda.add_command(label="Informacion", command=ayuda_informacion)
    menubar.add_cascade(label="Ayuda", menu=ayuda)
    
    ayuda.add_command(label="Manual de usuario", command=link_manual)
    ayuda.add_command(label="Integrantes", command=ayuda_integrantes)
    ayuda.add_separator()
    ayuda.add_command(label="Video Tutorial",command=link_video)
    ayuda.add_command(label="Repositorio", command=link)
    
    
        
    editor = Text(ventana, undo="true")

    editor.pack(side=TOP, fill=BOTH, expand=1)



    ventana.title("Bloc de notas")

    ventana.geometry("1000x700+100+10")

    ventana.config(menu=menubar)

    ventana.mainloop()