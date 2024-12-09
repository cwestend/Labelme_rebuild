# Labelme_rebuild
Reconstrucción de los patches extraidos con Labelme

## Entorno
El entorno de python es el mismo de https://github.com/cwestend/Patomat_Contrastive (aunque no hace falta pytorch).

## Uso
El programa va leyendo los ficheros que tienen los datos de las posiciones en la imagen original. Reconstruye un array
en blanco (vacío) y lo  va rellenando con cada imagen en su sitio. Hay que tener en cuenta que al recortar se usan los
rectángulos marcados a mano que pueden hasta solaparse (no es lo ideal!)

En path es el directorio con todos los ficheros con cada uno de los patches de la imagen

```
% path = "./992_22_ca_202203081937_labelme/"

```

Al ejecutar el programa en una consola interactiva:

```
# run rebuild_labelme.py
```
El programa lee cada uno de los ficheros y los encaja en un array. El array es:

```
# rebuild_ima.shape
```

Además nos da las coordenadas iniciales del array en coordenadas de la **imagen original** y son x_min y y_min). 
Como tenemos la miniatura que es un factor cuatro más pequeña, ya tenemos todo.

prueba













