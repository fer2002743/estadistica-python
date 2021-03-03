import random
from varianza import desviacion_estandar
from bokeh.plotting import figure, output_file, show



numero_agujas = int(input('con cuantas agujas quieres correr la simulacion?? '))  
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

    #pi = (4 * dentro_del_circulo) / numero_agujas
output_file("line.html")
plot = figure(plot_width=600, plot_height= 600)
plot.circle(in_circle_x, in_circle_y, size=5, color='blue', alpha=0.5)
plot.circle(out_circle_x,out_circle_y,size=5, color='red',alpha=0.5)
show(plot)


