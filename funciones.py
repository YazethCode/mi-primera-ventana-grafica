import tkinter as pug

ventana = pug.Tk()

texto = pug.Label(ventana, text="hola")
texto.pack()

def cambiar():
    texto.config(text="bienvenido papanigga")
    
boton = pug.Button(ventana, text="presioname",command=cambiar)
boton.pack()

ventana.mainloop()