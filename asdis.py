import interprete as scan
from Token import Token
from tipoToken import tipoToken

pila=['']
salida=''

def asdis(op,cont):
	def A3(cad):
		global salida
		if cad[0]=='PUNTO':
			if cad[1]=='IDENTIFICADOR':
				if cad[2]=='$' and len(cad)==3:
					salida='Consulta correcta'
					return 0#Todo nice
				else:
					Qaux(cad[2:])
					return 2
			else:
				salida='Error en A3'
				return 2
		elif cad[0]=='IDENTIFICADOR':
			salida='Error en A3'
			return 2
		elif cad[0]=='FROM':
			Qaux(cad)
			return 0
		elif cad[0]=='$':
			salida='Consulta correcta'
			return 0
		elif cad[0]=='COMMA' and cad[1]!='$':
			return 0
		else:
			salida='Error en A3'
			return 1#Para ver errores

	def A2(cad):
		global salida
		if cad[0]=='IDENTIFICADOR':
			pila.append(cad[0])
			return A3(cad[1:])
		else:
			salida='Error en A2'
			return 0

	def A1(cad):
		if cad[0]=='COMA':
			pila.append('COMA')
			A(cad[1:])

	def A(cad):
		pos=A2(cad)
		if pos==1:
			A1(cad[1:])

	def P(cad):
		global salida
		if cad[0]=='ASTERISCO':
			if cad[1]=='$':
				salida='Consulta correcta'
			#else:
				#print('Error en P - *')	
		elif cad[0]=='IDENTIFICADOR':
			A(cad)
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
			Qaux(cad)
		else:
			salida='Error en D'

	def T3(cad):
		global salida
		if cad[0]=='IDENTIFICADOR':
			pila.append(cad[0])
			if cad[1]=='$' and len(cad)==2:
				salida='Consulta correcta'
			else:
				salida='Error en T3'
		elif cad[0]=='$':
			pila.append('$')
			salida='Consulta correcta'

	def T2(cad):
		if cad[0]=='IDENTIFICADOR':
			pila.append(cad[0])
			T3(cad[1:])

	def T1(cad):
		if cad[0]=='COMA':
			pila.append(cad[0])
			T(cad[1:])
		elif cad[0]=='$':
			global salida
			salida='Consulta correcta'

	def T(cad):
		if cad[0]=='IDENTIFICADOR':
			T2(cad)
			T1(cad[1:])
		else:
			global salida
			salida='Error en T'

	def Qaux(cad):
		if cad[0]=='FROM':
			T(cad[1:])
		else:
			global salida
			salida='Error en From'

	def Q(cad):
		if cad[0]=='SELECT':
			pila.append(cad[0])
			D(cad[1:])	

	def analisis(cad):
		sal=[cad[0]]
		for i in range(3,len(cad)-1,3):
			sal.append(cad[i])
		return sal

	if op==1:
		cad=scan.lineaComando()+['$','','']
	else:
		cad=scan.scanerArchivo(cont)+['$','','']
		#print(cad)
	Q(analisis(cad))
	print(salida)
