# Labelme_rebuild
Reconstrucción de los patches extraidos con Labelme (en https://cloud.iac.es/index.php/s/7RDFoHcd25L6n28)

## Entorno
El entorno de python es el mismo de https://github.com/cwestend/Patomat_Contrastive (aunque no hace falta pytorch).
Posiblemente haga falta OpenCV:

```
python3 -m pip install opencv-python==4.6.0.66

```

## Uso
El programa **rebuild_labelme.py** va leyendo los ficheros que tienen los datos de las posiciones en la imagen original. Reconstruye un array
en blanco (vacío) y lo  va rellenando con cada imagen en su sitio. Hay que tener en cuenta que al recortar se usan los
rectángulos marcados a mano que pueden hasta solaparse (no es lo ideal!)

En el path (dentro del código) está el directorio con todos los ficheros con cada uno de los patches de la imagen

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

Out[]: (5389, 1200, 3)

```

Además nos da las coordenadas iniciales del array en coordenadas de la **imagen original** y son **x_min** y **y_min**
(la otra esquina es **x_max**, **y_max**). 
Como tenemos la miniatura que es un factor cuatro más pequeña, ya tenemos todo.
Leemos la miniatura:

```
# image992 = np.asarray(Image.open("./992_22_ca_202203081937_pred_grid_web.jpg"))

```
Se reescala para tener el mismo tamaño que la original y asi encajar una en la otra:

```
# import cv2 os cv2
# im992 = image992.astype(np.uint8)
# original_height, original_width, channels = im992.shape
# new_height = original_height * 4
# new_width = original_width * 4
# new_dimensions = (new_width, new_height)
# nim992 = cv2.resize(im992, new_dimensions, interpolation=cv2.INTER_AREA)

```

Se visualiza:
```
# import matplotlib.pyplot as pl
# pl.imshow(nim992)
```
Para ver donde encajaría, se puede eliminar ese rectángulo en un canal:

```
# cnim992 = np.copy(nim992)
# cnim992[x_min:x_max, y_min:y_max, 1] = 0

```
Se visualiza

```
pl.imshow(cnim992)

```













