import interprete as scan
import asdis as a
import sys
import os


if len(sys.argv)>1 and len(sys.argv)<3:
	if os.path.exists(sys.argv[1]):
		archivo=open(sys.argv[1],'r')
		cont=archivo.read()
		print('')
		a.asdis(0,cont)
		print('\n')
	else:
		print('\nEl archivo '+sys.argv[1]+' no existe\n')
else:
	os.system('clear')
	while True:
		a.asdis(1,'')