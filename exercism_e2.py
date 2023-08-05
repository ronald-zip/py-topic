EXPECTED_BAKE_TIME = 40 #Define constant time expected to finish cook
PREPARATION_TIME = 80 #Define constant 
TIME_LAYERS = 2 #Define constant time per layer

def bake_time_remaining(current_time):
    """Calcula el tiempo restante que queda para hacer una lasaña
    :param elapsed_bake_time : int - tiempo total que toma hacer la lasaña
    :param current_time : int - tiempo actual de cocinada la lasaña
    :return: int - tiempo restante para terminar la lasaña"""
    elapsed_bake_time = EXPECTED_BAKE_TIME-current_time
    return elapsed_bake_time

def preparation_time_in_minutes(layer):
    """Funcion de preparacion en minutos
    :param layer : int - cantidad de capas
    :param TIME_LAYERS : int - constante, segun el ejercicio toma 2 minutos preparar una capa
    :return: int - tiempo total para cocinar una lasaña con "n" capas"""
    total_time = layer*TIME_LAYERS
    return total_time

def elapsed_time_in_minutes(layers,time):
    """Calcula el total del tiempo para hacer una lasaña
    :param layers : int - numero de capas.
    :param time : int - tiempo por capas.
    :return: int - tiempo total para hacer la lasaña de "x" capas"""
    total_time = layers*2+time
    return total_time