# ImageProcessing 

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado en tu sistema.

## ¿Cómo construir y correr la app?

1. **Clona este repositorio y entra a la carpeta del proyecto:**

   ```sh
   git clone <url-del-repo>
   cd Test_Backend_INbest
   ```

2. **Construye la imagen de Docker:**

   ```sh
   docker build -t imageprocessing-app .
   ```

3. **Corre el contenedor:**

   ```sh
   docker run -p 5000:5000 imageprocessing-app
   ```

4. **Abre tu navegador y entra a:**

   ```
   http://localhost:5000
   ```

## Notas

- Los archivos subidos y la base de datos SQLite se almacenan dentro del contenedor.  
  Si quieres persistencia, puedes montar un volumen:

  ```sh
  docker run -p 5000:5000 -v $(pwd)/uploads:/app/uploads -v $(pwd)/images.db:/app/images.db imageprocessing-app
  ```

- Si cambias el código, reconstruye la imagen con `docker build ...`.

---

¡Listo! Así puedes correr tu app Flask con OpenCV en Docker fácilmente.