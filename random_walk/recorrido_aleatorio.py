from borracho import BorrachoTradicional, DrogadoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def simular_una_caminata(campo,borracho,pasos):
    
    x_arr = []
    y_arr = []
    # Guardar la primera posicion
    x_arr.append(campo.obtener_coordenada(borracho).x)
    y_arr.append(campo.obtener_coordenada(borracho).y)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        x_arr.append(campo.obtener_coordenada(borracho).x)
        y_arr.append(campo.obtener_coordenada(borracho).y)
    
    graficar_camino(x_arr,y_arr,borracho)


def graficar_camino(x,y,borracho):

    grafica = figure(match_aspect=True, title=f'Camino aleatorio de un {borracho.nombre}', x_axis_label='X [m]', y_axis_label='Y [m]')
    grafica.line(x,y, legend_label=f'recorrido de {pasos} pasos', line_alpha=0.8, line_width=2)
    grafica.scatter(x[0],y[0],radius=0.5, fill_color='green',fill_alpha=0.6,legend_label='inicio')
    grafica.scatter(x[-1],y[-1], radius=0.5,fill_color='red',fill_alpha=0.6,legend_label='fin')
    show(grafica)


def main(pasos, borracho):
    campo = Campo()
    origen = Coordenada(0,0)
    campo.anadir_borracho(borracho,origen)
    simular_una_caminata(campo,borracho,pasos)

if __name__ == '__main__':
    pasos = 1000
    borracho = BorrachoTradicional(nombre='Jorge')
    drogado = DrogadoTradicional(nombre='Justin')

    main(pasos, drogado)