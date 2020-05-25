# EXPRESION REGULAR DE UN CORREO ELECTRONICO
importar  re

expresion  =  r '^ ([A-Za-z0-9] +) ([@]) ([az] +) ([.]) ([az] +) $'
resultado  =  re . compilar ( expresion )
prueba  =  raw_input ( "entrada:" )
busqueda = re . buscar ( resultado , prueba )

si  busqueda :
    imprimir  busqueda . grupo ()
más :
    imprimir "qr"
