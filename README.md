# Taller 2 con gRPC

Este proyecto implementa un servidor gRPC que realiza el cálculo del número máximo en una lista de números enteros. El servidor puede delegar sublistas a otros servidores remotos, pero si estos fallan, puede realizar el cálculo de forma local.

## Características

- **Distribución de carga**: El servidor divide la lista de números y delega el cálculo a otros servidores.
- **Manejo de errores**: Si no puede conectar con los servidores remotos, realiza el cálculo localmente.
- **gRPC**: Utiliza gRPC para la comunicación entre los servidores.

## Requisitos

- **Python 3.x**
- **gRPC**

## Pasos para ejecutar el programa

### 1. Crear un entorno virtual

Para evitar conflictos con otras dependencias, es recomendable crear un entorno virtual. Ejecuta los siguientes comandos:

```bash
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate  # En Windows usa: venv\Scripts\activate
$ python -m pip install --upgrade pip
```
### 2. Instalar gRPC

```bash
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
```

### 3. Clona el repsotorio

```bash
$ git clone https://github.com/pescobarg/sistema_distribuido_grpc.git
$ cd sistema_distribuido_grpc
```

### 4. Ejecuta el cliente y distintos servidores