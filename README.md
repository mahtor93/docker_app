# Docker App

Este proyecto es una aplicación Docker que proporciona una configuración básica para desplegar una aplicación.

## Requisitos

- Docker
- Docker Compose

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/docker_app.git
    cd docker_app
    ```

2. Construye y levanta los contenedores:
    ```sh
    docker-compose up --build
    ```
3. Ejecuta las migraciones de la base de datos desde django:
    ```sh
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    ```

## Uso

La aplicación estará disponible en `http://localhost:puerto` (reemplaza `puerto` con el puerto configurado en tu `docker-compose.yml`).

Para conseguir la ip que está sirviendo la base de datos y poder conectar a PgAdmin:
sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nombre_del_contenedor


## Estructura del Proyecto

- `Dockerfile`: Define la imagen de Docker para la aplicación.
- `docker-compose.yml`: Configuración de Docker Compose para levantar los servicios.
- `src/`: Código fuente de la aplicación.

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
