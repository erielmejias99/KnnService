import operator
from math import pow, sqrt

def knn_eriel( matrix , object, k ):
    """
    :param matrix: The info of the training data, the last row is the class of the data 
    :param object: Object to predict the class
    :param k: The nearest objects to count
    :return: The prediction
    """

    distances = []

    # Calculate the distance from object to every objects of the matrix
    for row in matrix:
        distances.append( ( distance( row[ 0 : -1 ], object ), row[ -1 ] ) )

    # Sort ascending order the distances
    distances.sort( key=operator.itemgetter( 0 ) )

    # count the class occurrences in the first k elements
    first_k_elemets = {}
    for i in range( 0, k ):
        # If the class is already in the dict
        if first_k_elemets.get( distances[ 1 ] ):
            first_k_elemets[ distances[ 1 ] ] += 1
        else:
            first_k_elemets[ distances[ 1 ] ] = 1

    return sorted( first_k_elemets.items(), key = operator.itemgetter( 1 ), reverse = True )[ 0 ][ 0 ][ 1 ]


def distance( object1, object2 ):
    """
    :param object1: numeric list to calculate the euclidean distance
    :param object2: numeric list to calculate the euclidean distance
    :return: the euclidean distance
    """

    # sumatoria de las potencias
    sum_of_pow = 0

    for i in range( 0, len( object1 )):
        sum_of_pow += pow( object1[ i ] - object2[ i ], 2)

    return sqrt( sum_of_pow )