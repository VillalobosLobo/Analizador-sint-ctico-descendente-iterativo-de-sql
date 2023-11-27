from Token import Token
from tipoToken import tipoToken
import os

t=Token('','',0)

def identificador(cad,pos):
    j=1
    if cad[0].isalpha() or cad[0].isdigit():
	for i in cad:
	    if i.isdigit() or i.isalpha() or i=='_' or i=='-':
		j+=1
	    else:
		break
	#print(Token(tipoToken.IDENTIFICADOR,cad[:j-1],pos).toString())
	t.almacenar(tipoToken.IDENTIFICADOR,cad[:j-1],pos)
	return j-1
    else:
        return 0

def identificar(cad,pos):
	
	#Caracteres
	if cad[0]==',':
		#print(Token(tipoToken.COMA,cad[0],pos).toString())
		t.almacenar(tipoToken.COMA,cad[0],pos)
		return 0
	elif cad[0]=='.':
		#print(Token(tipoToken.PUNTO,cad[0],pos).toString())
		t.almacenar(tipoToken.PUNTO,cad[0],pos)
		return 0
	elif cad[0]=='*':
		#print(Token(tipoToken.ASTERISCO,cad[0],pos).toString())
		t.almacenar(tipoToken.ASTERISCO,cad[0],pos)
		return 0
	elif cad[:6]=='select':
		if len(cad)>6:
		    if cad[:7]=='select ':
			#print(Token(tipoToken.SELECT,cad[:6],pos).toString())
			t.almacenar(tipoToken.SELECT,cad[:6],pos)
			return 6
		    else:
			return identificador(cad,pos)
		 else:
		    #print(Token(tipoToken.SELECT,cad[:6],pos).toString())
		    t.almacenar(tipoToken.SELECT,cad[:6],pos)
		    return 6
	elif cad[:4]=='from':
	    if len(cad)>4:
		    if cad[:5]=='from ':
		    #print(Token(tipoToken.FROM,cad[:4],pos).toString())
		    t.almacenar(tipoToken.FROM,cad[:4],pos)
		    return 4
	        else:
		    return identificador(cad,pos)
	    else:
		
