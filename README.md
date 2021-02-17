  <h1>Programación Dinámica y Estocástica con Python</h1>
</div>

<div align="center"> 
  <img src="http://clipart-library.com/images_k/python-logo-transparent/python-logo-transparent-5.png" width="250">
</div>

<h1>objetivos:</h1>

- Aprender a usar la Programacion Dinamica para hacer mas eficientes los problemas de optimizacion.
- Sabar como funciona la Programcion Dinamica y cuando usarla
- enternder la diferencia entre la programcion determinista y la estocastica


<h1>Introduccion a la programacion dinamica:</h1>

El nombre de Programcion Dinamica no tiene nada que ver con dinamismo, es simplemente un termino inventado por Richard Bell con la intencion de hacer parecer que su investigacion era la hostia para de esta manera conseguir financiacion del gobierno.

Es una de las tecnicas mas poderosa para optimizar problemas que cumplen con dos caracteristicas:
-**Subestructura optima:** Caracteristica que consiste en que podemos solucionar un problema grande mediante la combinacio de soluciones pequeñas.

- **Problemas empalmados:** Es una caracteristica segun la cual resolvemos un mismo problema una y otra y otra vez.

Por otro lado, la optimizacion nos permite hacer que nuestro programa se ejecute en mucho menos timepo, esto lo conseguimos mediante la memorizacion, lo cual consiste en guardar el resultado de computos anteriores para asi evitar tener que hacer los computos varias veces. Normalmente usamos un diccionario o cualquier estructura de datos que nos permite acceder a estos datos de una manera muy rapida, estas consultas las hacemos en O(1). Sin embargo, esta velocidad tiene un coste, y es que utilizaremos mas espacio en memoria.

<h1>Optimizacion de Fibonacci:</h1>

La sucesion de Fibonacci es se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores, de manera que:
                       <div align="center">**0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…**</div>
                       
La suceson de fibonacci es infeciente porque repetimos el mismo calculo un muchas veces.

