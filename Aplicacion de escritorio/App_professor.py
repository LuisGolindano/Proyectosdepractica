class Grado():
  def __init__(self, nombre):
    self.nombre = nombre

class Seccion():
  def __init__(self, nombre):
    self.nombre = nombre

class Profesor():
  def __init__(self, nombre, contraseña ):
    self.nombre = nombre
    self.contraseña = contraseña

class Materia():
  def __init__(self, nombre, profesor, grado):
    self.nombre = nombre
    self.profesor = profesor
    self.grado = grado

class Estudiante():
  def __init__(self, nombre, apellido, cedula, grado, seccion):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.grado = grado
    self.seccion = seccion

class Evaluacion():
  def __init__(self, objetivo, estrategia, ponderacion, escala, materia):
    self.objeivo = objetivo
    self.estrategia = estrategia
    self.ponderacion = ponderacion
    self.escala = escala
    self.materia = materia

class EstudianteMateria():
  def __init__(self, estudiante, materia):
    self.estdiante = estudiante
    self.materia = materia

class EstudianteEvaluacion():
  def __init__(self, estudiante, evaluacion, calificacion):
    self.estudiante = estudiante
    self.evaluacion = evaluacion
    self.calificacion = calificacion

def crear_cuenta(Profesor):
  pass

def login(user, contraseña):
  pass

def crear_materia(Materia):
  pass

def crear_estudiantes(Estudiante):
  pass

def crear_evaluacion(Evaluacion):
  pass

def listar_materias(nombre_profesor):
  pass

def listar_estudiantes(nombre_materia):
  pass

def editar_estudiante(Estudiante, Evaluacion):
  pass

def eliminar_estudiante(Estudiante, Evaluacion):
  pass

