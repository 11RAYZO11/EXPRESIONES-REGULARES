# ENCONTRAR PATRON  "11011" EN CUALQUIER PARTE DE LA CADENA
importar  re

expresion  =  r '^ ([1] {1} [0] {1} [1] {1}) $'
resultado  =  re . compilar ( expresion )
prueba  =  raw_input ( "entrada:" )
busqueda = re . buscar ( resultado , prueba )

si  busqueda :
    imprimir  busqueda . grupo ()
más :
    imprimir "qr"
