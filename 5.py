# EXPRESION DE VALIDACION DE OPERACIONNES
import  re

while True:

    expresion = r'^([0-9]+|[\w]+)\s([-|+|*|/|^|#]|[\w]+)\s([0-9]+|[\w]+)$'
    expresion1  =  r '([\ w] +) \ s ([0-9] + | [\ w] +)'
    resultado  =  re . compilar ( expresion )
    resultado1  =  re . compilar ( expresion1 )
    prueba  =  raw_input ( "entrada:" )
    busqueda = re . buscar ( resultado , prueba )
    busqueda1 = re . búsqueda ( resultado1 , prueba )
    si  busqueda :
        imprimir  busqueda . grupo ( 1 )
        n1 = busqueda . grupo ( 1 )
        imprimir  busqueda . grupo ( 2 )
        op = busqueda . grupo ( 2 )
        imprimir  busqueda . grupo ( 3 )
        n2 = busqueda . grupo ( 3 )

        si  n1  ==  "cero" :
            n1  =  0
        si  n1  ==  "uno" :
            n1  =  1
        si  n1  ==  "dos" :
            n1  =  2
        si  n1  ==  "tres" :
            n1  =  3
        si  n1  ==  "cuatro" :
            n1  =  4
        si  n1  ==  "cinco" :
            n1  =  5
        si  n1  ==  "seis" :
            n1  =  6
        si  n1  ==  "siete" :
            n1  =  7
        si  n1  ==  "ocho" :
            n1  =  8
        si  n1  ==  "nueve" :
            n1  =  9
        si  op  ==  "mas" :
            op  =  "+"
        si  op  ==  "menos" :
            op  =  "-"
        si  op  ==  "por" :
            op  =  "*"
        si  op  ==  "entre" :
            op  =  "/"
        si  n2  ==  "cero" :
            n2  =  0
        si  n2  ==  "uno" :
            n2  =  1
        si  n2  ==  "dos" :
            n2  =  2
        si  n2  ==  "tres" :
            n2  =  3
        si  n2  ==  "cuatro" :
            n2  =  4
        si  n2  ==  "cinco" :
            n2  =  5
        si  n2  ==  "seis" :
            n2  =  6
        si  n2  ==  "siete" :
            n2  =  7
        si  n2  ==  "ocho" :
            n2  =  8
        si  n2  ==  "nueve" :
            n2  =  9
        prueba :
            n1 = int ( n1 )
            n2 = int ( n2 )

            si  op == "+"  o  "-"  o  "*"  o  "/" :
                si  op == "+" :
                    r = n1 + n2

                elif  op == "-" :
                    r = n1 - n2

                elif  op == "*" :
                    r = n1 * n2

                elif  op == "/" :
                    r = n1 / n2

                elif  op == "^" :
                    r = n1 ** n2

                elif  op == "#" :
                    r = n1 ** ( 1.0 / n2 )
                print ( "el resultado es:% s% s% s =% s"  % ( n1 , op , n2 , r ))

        excepto :
            imprimir "qr" ;


    elif  busqueda1 :
        imprimir  busqueda1 . grupo ( 1 )
        op = busqueda1 . grupo ( 1 )
        imprimir  busqueda1 . grupo ( 2 )
        n2 = busqueda1 . grupo ( 2 )


        prueba :
            n2 = int ( n2 )

            si  op == "sen"  o  "cos"  o  "tan" :
                si  op == "sen" :
                    r = matemáticas . sin ( n2 )

                elif  op == "cos" :
                    r = matemáticas . cos ( n2 )

                elif  op == "bronceado" :
                    r = matemáticas . bronceado ( n2 )



                print ( "el resultado es:% s% s =% s"  % ( op , n2 , r ))
        excepto :
            imprimir "qr" ;
