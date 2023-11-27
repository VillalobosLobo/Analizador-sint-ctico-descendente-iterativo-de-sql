from tipoToken import tipoToken

class Token():
  def __init__(self,tipo,lexema,posicion):
    self.tipo=tipo
    self.lexema=lexema
    self.posicion=posicion
    self.salida=[]

  '''def __init__(self,tipo,lexema):
      self.tipo=tipo
      self.lexema=lexema
      self.posicion=0
      self.salida=[]'''

  def toString(self):
