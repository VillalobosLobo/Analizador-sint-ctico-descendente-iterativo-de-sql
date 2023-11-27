import interprete as scan
from Token import Token
from tipoToken import tipoToken

pila=['']
salida=''

def analisis(cad):
		sal=[cad[0]]
		for i in range(3,len(cad)-1,3):
			sal.append(cad[i])
		return sal

cad=scan.lineaComando()+['$','','']

#Q(analisis(cad))
print(analisis(cad))
print(salida)
