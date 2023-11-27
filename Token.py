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
        return '<'+str(self.tipo)+' '+str(self.lexema)+' '+str(self.posicion)+'>'

    def almacenar(self,tipo,lexema,posicion):
        entrada=['','','']
        entrada[0]=tipo
        entrada[1]=lexema
        entrada[2]=posicion
        self.salida+=entrada

    def imprimirEstruct(self):
        print(self.salida)

    def obtener()
        return self.salida
      
