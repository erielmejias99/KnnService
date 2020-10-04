from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


def home( request ):
    return render( request, 'Home.html' )

@csrf_exempt
def knn_service( request ):

    # el metodo tiene q ser POST xq nos estan enviando informacion
    if request.method == 'POST':
        # El parametro data va a estar dentro del json
        # en realidad lo q envian es un lista de bytes lo cual se decodifica a string
        data = request.body.decode('utf-8')

        if data:
            try:

                # En realidad lo que me envian por parametro es un JSON en
                # forma de texto y hay q parsearlo a diccionario y listas de python
                # json es una libreria de python nativo para hacerlo
                print( data )
                data = json.loads( data ).get( "data" )


                # dentro de data va a estar la variable matrix q es la q contiene toda la info
                matrix = data.get('matrix')

                # tiene q existir el parametro y ser de tipo list y no estar vacio

                print( matrix )

                if matrix and type( matrix ) == list and len( matrix ) >= 2:

                    # recorro cada fila y q cada una tenga el mismo tamano
                    row_size = len( matrix[ 0 ] )
                    for row in matrix:
                        if row_size != len( row ):
                            # return an error
                            return JsonResponse( { 'message': "All the row of the matrix parameter most have the save size" })

                    # en este punto la matrix esta validada
                    # ahora validar el objeto q se quiera clasificar el cual tiene q ser una list
                    # de tamano row_size - 1 xq no tendria la clasificacion
                    obj = data.get( 'object' )
                    if obj and type( obj ) == list:
                        if len( obj ) != row_size - 1:
                            return JsonResponse(
                                {
                                    'message': "Error in the object parameter, "
                                               "the amount of features has to be equal"
                                               " to the amount of feature of the matrix"
                                })

                        # en este punto ya esta validado la matrix y el objeto ahora obtego la k
                        # la cual tiene q ser de tipo int vamos a poner q este campo no es requerido
                        # o sea q si el usuario no lo envia le ponemos nosotros una constante
                        k = data.get( 'k' )
                        # si no la envio o sea k = None o no es un entero ponerle constante 10
                        if not k or type( k ) != int:
                            k = 10

                        # En este punto ya es posible llamar a tu metodo despues q se validaron los datos
                        # classif = knn_algorithm( matrix, obj, k )

                        # return JsonResponse( {'classification': classif } )

                    else:
                        return JsonResponse( { 'message': "The parameter object is required and has to be a list with lenght > 2" } )

                else:
                    # Si el usuario no envia la variable matrix entonces responderle con un error
                    return JsonResponse( { 'message': "The matrix parameter most be sent and has to be a list" })

                # tengo q validar q todas las filas de la matrix tengan el mismo length y que
                # y q todas excepto la ultima tenga timpo de datos int o float para evitar errores
                # en to algorithm al no xq sino da error tu algorithmo al calcular la dist o al hacer
                # cualquier operacion. ejemplor ( "carlos" * 3 )

            except Exception as e:
                print( e )
                return JsonResponse( {'message': "Error in data parameter"})
        else:
            return JsonResponse( {'message': "data parameter most be sent" } )
    else:
        return JsonResponse( { 'message': "Most be a post request" } )