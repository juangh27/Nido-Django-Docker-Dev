# Nido-Django-Docker-Dev

## Usar ambiente virtual *(requiere tener python instalado)*

1.  Creacion de la carpeta 

    ```py -3 -m venv venv```


2.  Activando venv
    
    ```venv\Scripts\activate```
    
3.  Instalar django y otras dependecias 

    ``` pip install -r requirements.txt ```

4.  Correr el servidor

    ```cd server```

    ```manage.py runserver```

5.  Para revisar la pagina es ir a la url http://localhost:8000/nido/
## Usar contenedor mostrando el proyecto lo mas cercano a produccion *(requiere tener Docker instalado)*

[![Alt text](https://img.youtube.com/vi/_et7H0EQ8fY/0.jpg)](https://www.youtube.com/watch?v=_et7H0EQ8fY)


### Crear y correr contenedor

``` docker-compose up --build ```

### Solo correr contendor 

``` docker-compose up ```

### Correr contenedor en background 

``` docker-compose up -d```
### Detener contenedor
``` docker-compose stop```
### Borrar contenedor
``` docker-compose down```
### Depurar docker borrando imagenes, contenedores y volumenes sin usar 
``` docker system prune```




### Carpetas y archivos a revisar

* _/server/nido/templates/nido/_
    
    Aqui se encuentran los archivos html

* _/server/nido/urls.py_

    Aqui estan las direciones de las paginas

* _/server/nido/views.py_

    Aqui tenemos las vistas de cada pagina

* _/server/static_

    Aqui estan los archivos estaticos 

    * css
    * img
    * js









