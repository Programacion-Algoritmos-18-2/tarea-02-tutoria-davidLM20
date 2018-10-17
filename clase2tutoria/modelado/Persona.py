class Persona:  

  def __init__(self):
    self.nombre = ""
    self.edad = 0

  def agregar_nombre(self,n):
    self.nombre = n
  
  def obtener_nombre(self):
    return self.nombre
  
  def agregar_edad(self,n):
    self.edad = n 

  def obtener_edad(self):
    return self.edad

  def presentar_datos(self):
    cadena = "%s - %s" % (self.obtener_nombre(),self.obtener_edad())
    return cadena