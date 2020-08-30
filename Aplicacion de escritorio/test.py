from tkinter import Tk, Label, Button


def clear():
  list = window.grid_slaves()
  for l in list:
    l.destroy() 

def go_to(window, name):
  def wrapped():
    if name == 'home':
      clear()
      primera_view(window)
    if name == 'segunda':
      clear() 
      segunda_view(window)
  return wrapped

def primera_view(window):
  Label(window, text = 'HOLA MUNDO').grid(row = 0, column = 0, columnspan = 2, sticky = 'n', pady = 100)
  button_next = Button(window, text = 'next', command = go_to(window, 'segunda')).grid(row = 0, sticky = 'n', columnspan = 2, pady = 0)
  return window

def segunda_view(window):
  Label(window, text='Segundo hola').grid(row = 0, column = 0, columnspan = 2, sticky = 'n', pady = 50)
  button_back = Button(window, text = 'back', command = go_to(window, 'home')).grid(row = 1,columnspan = 2, pady = 15)
  return window

if __name__ == "__main__":
    window = Tk()
    primera_view(window)
    window.mainloop()