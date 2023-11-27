import interprete as scan
from Token import Token
from tipoToken import tipoToken

pila=['']
salida=''

def P(cad):
	global salida
	if cad[0]=='ASTERISCO':
		if cad[1]=='$':
			salida='Consulta correcta'
	elif cad[0]=='IDENTIFICADOR':
		#A(cad)
	else:
		salida='Error en P'

def D(cad):
	global salida
	if cad[0]=='DISTINCT':
		P(cad[1:])
	elif cad[0]=='ASTERISCO':
		P(cad)
	elif cad[0]=='IDENTIFICADOR':
		P(cad)
	elif cad[0]=='FROM':
		#Qaux(cad)
	else:
		salida='Error en D'

def Q(cad):
	if cad[0]=='SELECT':
		pila.append(cad[0])
		D(cad[1:])

def analisis(cad):
		sal=[cad[0]]
		for i in range(3,len(cad)-1,3):
			sal.append(cad[i])
		return sal

cad=scan.lineaComando()+['$','','']

#Q(analisis(cad))
print(analisis(cad))
print(salida)
