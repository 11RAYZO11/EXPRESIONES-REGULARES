
# ENCONTRAR PATRON  "1101" AL INICIO DE LA CADENA
importar  re

expresion  =  r '^ ([az] {3,5}) $'
resultado  =  re . compilar ( expresion )
prueba  =  raw_input ( "entrada:" )
busqueda = re . buscar ( resultado , prueba )

si  busqueda :
    imprimir  busqueda . grupo ()
más :
    imprimir "qr"
