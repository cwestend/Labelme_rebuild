# Labelme_rebuild
Reconstrucción de los patches extraidos con Labelme

## Entorno
El entorno de python es el mismo de https://github.com/cwestend/Patomat_Contrastive (aunque no hace falta pytorch).

## Uso
El programa va leyendo los ficheros que tienen los datos de las posiciones en la imagen original. Reconstruye un array
en blanco (vacío) y lo  va rellenando con cada imagen en su sitio. Hay que tener en cuenta que al recortar se usan los
rectángulos marcados a mano que pueden hasta solaparse (no es lo ideal!)








