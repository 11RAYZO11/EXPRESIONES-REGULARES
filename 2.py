# ENCONTRAR PATRON  "1101" AL FIN DE LA CADENA
importar  re

expresion  =  r '^ ([0] {1} [1] {1} [0] {1}) $'
resultado  =  re . compilar ( expresion )
prueba  =  raw_input ( "entrada:" )
busqueda = re . buscar ( resultado , prueba )

si  busqueda :
    imprimir  busqueda . grupo ()
más :
    imprimir "qr"
