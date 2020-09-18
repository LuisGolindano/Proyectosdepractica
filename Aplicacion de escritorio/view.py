import App_professor
import sqlite3
import tkinter as tk


def crear_login_view(window):
  window.title("Aplicacion de escritorio")
  window.columnconfigure(0, weight = 1, minsize = 100)
  window.rowconfigure(0, weight = 1, minsize = 50)

  tk.Label(window, text = 'NOMBRE').grid(row = 0, column = 0, columnspan = 3, sticky = 'n', pady = 50)

  frame = tk.LabelFrame(window, text = 'Ingresar')
  frame.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 100)
    
  tk.Label(frame, text = 'Usuario: ').grid(row = 1, column = 0)
  name = tk.Entry(frame)
  name.focus()
  name.grid(row = 1, column = 1)

  tk.Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
  contra = tk.Entry(frame)
  contra.grid(row = 2, column = 1)
  
  def ent():
    if len(name.get()) != 0 and len(contra.get()) != 0 :
      clear()
      materias(window)
    else:
      msj_err = tk.Label(frame, text = 'Usuario Incorrecto', fg = 'red').grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')

  btn_ent = tk.Button(frame, text = "Entrar", command = ent).grid(row = 3, columnspan = 2, pady=6)

  btn_reg = tk.Button(frame, text = "Registrarse", command = go_to(window, 'register')).grid(row = 5, columnspan = 2, pady = 6)
  return window


def reg(window):
      frame = tk.LabelFrame(window, text = 'Registrarse')
      frame.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 50)

      tk.Label(frame, text = 'Ingrese el usuario: ').grid(row = 1, column = 0)
      ing_usu = tk.Entry(frame)
      ing_usu.focus()
      ing_usu.grid(row = 1, column = 1)

      tk.Label(frame, text = 'Ingrese la contraseña: ').grid(row = 2, column = 0)
      ing_contra = tk.Entry(frame)
      ing_contra.grid(row = 2, column = 1)

      def regt():
        if len(ing_usu.get()) != 0 and len(ing_contra.get()) != 0 :
          mjs_reg = tk.Label(frame, text = 'El usuario a sido registrado', fg = 'blue').grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')
        elif len(ing_usu.get()) == 0 :
          mjs_urr = tk.Label(frame, text = 'No se a ingresado el usuario', fg = 'red').grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')
        elif len(ing_contra.get()) == 0 :
          mjs_crr = tk.Label(frame, text = 'No se a ingresado la contraseña', fg = 'red').grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')

      btn_regt = tk.Button(frame, text = 'Registrarse', command = regt).grid(row = 3, columnspan = 2)

      btn_black = tk.Button(window, text = 'Volver', command = go_to(window, 'login')).grid(row = 0, column = 0,pady = 0, sticky = 'wn')
      return window


def crear_bottones(frame, materias=[]):
  def wrapped():
    for index, materia in enumerate(materias):
      tk.Button(frame, text=materia).grid(row=index, column=0, sticky='s', pady = 50)
  return wrapped


def materias(window):
  pass


def clear():
  list = WINDOW.grid_slaves()
  for l in list:
    l.destroy()


def go_to(window, ventana):
  def button():
    if ventana == 'login':
      clear()
      crear_login_view(window)
    if ventana == 'register':
      clear()
      reg(window)
  return button


if __name__ == "__main__":
  WINDOW = tk.Tk()
  crear_login_view(WINDOW)
  WINDOW.geometry('960x540')
  WINDOW.mainloop()