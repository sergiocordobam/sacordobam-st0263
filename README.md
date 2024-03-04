# Tópicos Especiales en Telemática
#
# Estudiante: Sergio Andrés Córdoba Muriel, sacordobam@eafit.edu.co
#
# Profesor: Edwin Montoya, emontoya@eafit.edu.co
#

# P2P - Comunicación entre Procesos
#
# 1. Breve descripción de la actividad
Creación de una red P2P que permite a los peers subir y descargar archivos. La comunicación se da por medio de API REST y RPC

<texto descriptivo>

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
  
Se desarrolló el pclient, sus respectivos pservers y el servidor. Además se implementaron los métodos de upload_file y download_file

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

El server se inicia correctamente, pero en el momento de que los peers hagan el respectivo log in, se produce un error para encontrar las credenciales del pserver. No fue desplegado en AWS

# 2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
![image](https://github.com/sergiocordobam/sacordobam-st0263/assets/89363748/29c9b080-fc3e-478b-ad8a-1ccb43bdf62b)

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Como se compila y ejecuta.
Para ejecutar el servidor es necesario el comando: **python server.py bootstrap/.env_server** </br>
Para correr el pserver se utiliza el siguiente comando: **python pserver.py bootstrap/.env_pserver1** </br>
Para correr el pclient se usa el siguiente comando: **python pclient.py bootstrap/.env_pclient1**
## Detalles del desarrollo.
La solución fue desarrollada con Python (version 3.10.8), haciendo uso de librerias como: flask (3.0.2), python-dotenv (1.0.1), grpcio (1.62.0), grpcio-tools (1.62.0) y requests (2.31.0)
## Detalles técnicos
El peer que se divide en pclient y pserver. El pclient permite iniciar sesión, subir y descargar archivos. El pserver es el encargado de se comunica tanto con otros peers como con el servidor. La comunicación entre pclient y pserver se da por medio de gRPC, mientras que la comunicación entre el pserver y el server se da por emdio de API REST
## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
- El puerto del servidor es el 5000
- El PServer1 tiene como puerto el 5001 y el PServer2 el puerto 5002
## Opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
El proyecto fue estructurado en 4 carpetas </br>
**Bootstrap:** contiene las credenciales del pclient, pserver y server </br>
**Peer:** contiene la lógica del pclient y el pserver </br>
**Server:** contiene la lógica del server </br>
**Protobuf:** la estructura del pserver.proto 
## Opcionalmente - si quiere mostrar resultados o pantallazos 
![image](https://github.com/sergiocordobam/sacordobam-st0263/assets/89363748/f8f2fbc6-2e30-4dbb-b48e-24c5096b5978)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## Descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## Como se lanza el servidor.

## Una mini guia de como un usuario utilizaría el software o la aplicación

## Opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. Otra información que considere relevante para esta actividad.

# Referencias:
- https://www.youtube.com/watch?v=WB37L7PjI5k&t=411s
- https://github.com/st0263eafit/st0263-241
