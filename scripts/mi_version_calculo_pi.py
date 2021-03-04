import random
from varianza import desviacion_estandar, media
from bokeh.plotting import figure, output_file, show


def aventar_agujas(numero_agujas):

    in_circle_x = [ ]
    in_circle_y = [ ]
    out_circle_x = [ ]
    out_circle_y = [ ]
    dentro_del_circulo = 0
    

    for _ in range(numero_agujas):
        x = random.uniform(1,-1)
        y = random.uniform(1,-1)

        if (x**2 + y**2) ** 0.5 < 1:
            in_circle_x.append(x)
            in_circle_y.append(y)
            dentro_del_circulo += 1
        else:
            out_circle_x.append(x)
            out_circle_y.append(y)

    pi = (4 * dentro_del_circulo) / numero_agujas
    return pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y

def graficar(in_circle_x, in_circle_y, out_circle_x, out_circle_y):
    output_file("line.html")
    plot = figure(plot_width=600, plot_height= 600)
    plot.circle(in_circle_x, in_circle_y, size=5, color='blue', alpha=0.5)
    plot.circle(out_circle_x,out_circle_y,size=5, color='red',alpha=0.5)
    show(plot)

def main(numero_simulaciones, numero_agujas):
    resultados = [ ]
    inside_circle_x = [ ]
    inside_circle_y = [ ]
    outside_circle_x = [ ]
    outside_circle_y = [ ]
    for _ in range(numero_simulaciones):
        pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y = aventar_agujas(numero_agujas)
        resultados.append(pi)
        inside_circle_x.append(in_circle_x)
        inside_circle_y.append(in_circle_y)
        outside_circle_x.append(out_circle_x)
        outside_circle_y.append(out_circle_y)
    mean = media(resultados)
    stdev = desviacion_estandar(resultados)
    return inside_circle_x, inside_circle_y, outside_circle_x, outside_circle_y
    

if __name__ == '__main__':
    main(10, 10000)






































































# import random
# from varianza import desviacion_estandar, media
# from bokeh.plotting import figure, output_file, show


# def aventar_agujas(numero_agujas):

#     in_circle_x = [ ]
#     in_circle_y = [ ]
#     out_circle_x = [ ]
#     out_circle_y = [ ]
#     dentro_del_circulo = 0
    

#     for _ in range(numero_agujas):
#         x = random.uniform(1,-1)
#         y = random.uniform(1,-1)

#         if (x**2 + y**2) ** 0.5 < 1:
#             in_circle_x.append(x)
#             in_circle_y.append(y)
#             dentro_del_circulo += 1
#         else:
#             out_circle_x.append(x)
#             out_circle_y.append(y)
#     resultado_pi = (4 * dentro_del_circulo) / numero_agujas
#     return resultado_pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y

# def graficar(in_circle_x, in_circle_y, out_circle_x, out_circle_y):
#     output_file("vertical.html")
#     plot = figure(plot_width=600, plot_height= 600)
#     plot.circle(in_circle_x, in_circle_y, size=5, color='blue', alpha=0.5)
#     plot.circle(out_circle_x,out_circle_y,size=5, color='red',alpha=0.5)
#     show(plot)


# def estimaciones(numero_agujas, numero_intentos):
#     resultados = [ ]
#     inside_circle_x = [ ]
#     inside_circle_y = [ ]
#     outside_circle_x = [ ]
#     outside_circle_y = [ ]
#     for _ in range(numero_intentos):
#         resultado_pi, in_circle_x, in_circle_y, out_circle_x, out_circle_y = aventar_agujas(numero_agujas)
#         resultados.append(resultado_pi)
#         inside_circle_x.append(in_circle_x)
#         inside_circle_y.append(in_circle_y)
#         outside_circle_x.append(out_circle_x)
#         outside_circle_y.append(out_circle_y)
#     mean = media(resultados)
#     stdev = desviacion_estandar(resultados)
#     return (mean, stdev, inside_circle_x, inside_circle_y, outside_circle_x, outside_circle_y)

# def estimar_pi(precision, numero_intentos):
#     numero_agujas = 1000
#     sigma = precision
#     while sigma >= precision / 1.96:
#         mean, stdev,inside_circle_x, inside_circle_y, outside_circle_x, outside_circle_y = estimaciones(numero_agujas, numero_intentos)
#         numero_agujas *= 2
#         sigma -= 0.001
        
#     graficar(inside_circle_x, inside_circle_y, outside_circle_x, outside_circle_y)    
#     return mean


# if __name__ == '__main__':
#     print(estimar_pi(0.1,100))




