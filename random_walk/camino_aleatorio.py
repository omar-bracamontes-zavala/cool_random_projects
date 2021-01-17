from borracho import BorrachoTradicional, DrogadoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo,borracho,pasos):
    
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return inicio.distacia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos,numero_de_intentos,tipo_de_borracho):

    borracho = tipo_de_borracho(nombre='Jorge')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho,origen)
        simulacion_caminata = caminata(campo,borracho,pasos)
        distancias.append(round(simulacion_caminata,1))

    return distancias

def graficar(x,y):
    
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x,y, legend='distancia media')
    show(grafica)


def main(distancias_de_caminata,numero_de_intentos,tipo_de_borracho):

    print(f'\nExperimentos: {numero_de_intentos}\n')
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__}, caminata aleatoria de {pasos} pasos')
        print('Distancia: ')
        print(f'   * Media = {distancia_media} m')
        print(f'   * Max = {distancia_maxima} m')
        print(f'   * Min = {distancia_minima} m\n')

    grafica(distancias_de_caminata, distancias_media_por_caminata)


if __name__=='__main__':
    distancias_de_caminata = [10,100,1000,10000,100000]
    numero_de_intentos = 500

    #main(distancias_de_caminata,numero_de_intentos,BorrachoTradicional)
    main(distancias_de_caminata,numero_de_intentos,DrogadoTradicional)