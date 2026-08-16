import tkinter

ventana = tkinter.Tk()

ventana.title("mi primera ventana")

tkinter.Label(ventana , text="nombre").pack()

entrada = tkinter.Entry(ventana)
entrada.pack()

tkinter.Label(ventana , text="edad").pack()

entrada_edad = tkinter.Entry(ventana)
entrada_edad.pack()

tkinter.Label(ventana , text="calificacion").pack()

entrada_calificacion = tkinter.Entry(ventana)
entrada_calificacion.pack()

resultado = tkinter.Label(ventana , text="")
resultado.pack()

imagen = tkinter.PhotoImage(file="capibara2.png")
capibara = tkinter.Label(ventana , image=imagen)
capibara.pack()



def obtener_nombre():
   nombre =  entrada.get()
   edad = int(entrada_edad.get())
   calificacion = float(entrada_calificacion.get())
   
   if calificacion >= 8:
      resultado.config(text="felicidades " + nombre + " tuviste muy buena calificacion")
      
   elif calificacion >= 6:
      resultado.config(text="has aprobado" + nombre )
   
   else:
      resultado.config(text="has reprobado")

boton = tkinter.Button(ventana , text="aceptar" , command=obtener_nombre)

boton.pack()

ventana.mainloop()     