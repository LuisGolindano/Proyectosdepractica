from tkinter import Tk, Label, LabelFrame, Entry, Button

def back_button(window, view_name):
  return Button(window, text = '<', command = go_to(window, view_name)).grid(row = 0, sticky = 'wn')

def is_not_empty(string):
  return len(string) != 0

def login_event(window, frame, user_name_controller, password_controller):
  def wrapped():
    if is_not_empty(user_name_controller.get()) and is_not_empty(password_controller.get()):
      # TODO: Login process
      return go_to(window, 'signatures', {'signatures':['Fisica', 'Quimica']})()
    else:
      return Label(frame, text = 'Usuario Incorrecto', fg = 'red').grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')
  return wrapped

def register_event_from_login(window, params=None):
  def wrapped():
    return go_to(window, 'register', params)()
  return wrapped

def register_event(window, frame, user_name_controller, password_controller):
  def wrapped():
    if is_not_empty(user_name_controller.get()) and is_not_empty(password_controller.get()):
      # TODO: Register process
      return go_to(window, 'signatures', {'signatures':[]})()
    else:
      return Label(frame, text = 'Usuario Incorrecto', fg = 'red').grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')
  return wrapped
    

def new_signature_event(window, frame, new_class_controller, params):
  def wrapped():
    if is_not_empty(new_class_controller.get()):
      # TODO: create new signature
      return go_to(window, 'signatures', {'signatures': params['signatures'] + [new_class_controller.get()]})()
    else:
      return Label(frame, text = 'Materia incorrecta', fg = 'red').grid(row = 3, column = 0, columnspan = 2, sticky = 'ew')
  return wrapped

def login_view(window, params):
  Label(window, text='LOGIN').grid(row=0, column = 0, columnspan = 2, sticky = 'n', pady = 50)

  frame = LabelFrame(window, text='Ingresar')
  frame.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 100)
  
  Label(frame, text = 'Usuario: ').grid(row = 1, column = 0)
  user_name = Entry(frame)
  user_name.focus()
  user_name.grid(row = 1, column = 1)

  Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
  password = Entry(frame)
  password.grid(row = 2, column = 1)

  Button(frame, text = 'Ingresar', command=login_event(window, frame, user_name, password)).grid(row = 3, columnspan = 2)
  
  Button(frame, text='Registrarse', command=register_event_from_login(window)).grid(row = 5, columnspan = 2, pady = 10)
  return window

def signatures_view(window, params):
  back_button(window, 'home')
  frame = LabelFrame(window, text = 'Materias')
  frame.grid(row = 0, column = 0, columnspan = 5, padx = 50, pady = 50)
  Label(frame, text = 'Ingrese las materias: ').grid(row = 1, column = 0)

  new_class = Entry(frame)
  new_class.focus()
  new_class.grid(row = 1, column = 1)
        
  Button(frame, text = 'Agregar materia', command=new_signature_event(window, frame, new_class, params)).grid(row = 2, columnspan = 2, pady = 10)
  Label(frame, text = 'MATERIAS').grid(row = 4,column = 0, sticky = 'w', pady = 10)

  buttons = [Button(frame, text=signature).grid(row = index + 5, columnspan = 4, padx = 5, pady = 5, sticky='s') for index, signature in enumerate(params['signatures'])]
  return window

def register_view(window, params):
  back_button(window, 'home')
  Label(window, text='Nuevo Usuario').grid(row=0, column = 0, columnspan = 2, sticky = 'n', pady = 50)

  frame = LabelFrame(window, text='Ingresar')
  frame.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 100)

  Label(frame, text = 'Usuario: ').grid(row = 1, column = 0)
  user_name = Entry(frame)
  user_name.focus()
  user_name.grid(row = 1, column = 1)

  Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
  password = Entry(frame)
  password.grid(row = 2, column = 1)

  Button(frame, text='Registrarse', command=register_event(window, frame,user_name, password)).grid(row = 5, columnspan = 2, pady = 10)
  return window

def go_to(window,name, params=None):
  print(name, params)
  def wrapped():
    [slave.destroy() for slave in window.grid_slaves()]
    if name == 'home':
      return login_view(window, params)
    if name == 'signatures':
      return signatures_view(window, params)
    if name == 'estudents':
      pass
    if name == 'register':
      return register_view(window, params)
  return wrapped

if __name__ == "__main__":
    WINDOW = Tk()
    WINDOW.title('Professor Assistant')
    go_to(WINDOW, 'home')()
    WINDOW.mainloop()