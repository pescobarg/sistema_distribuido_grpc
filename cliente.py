import grpc
import calculo_pb2
import calculo_pb2_grpc

def leer_archivo(nombre_archivo):
    try:
        with open(f'{nombre_archivo}.txt', 'r') as fichero:
            print(f"El archivo '{nombre_archivo}' ha sido abierto correctamente")
            return [int(line.strip()) for line in fichero.readlines()]
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se ha podido abrir")
        return None

def enviar_datos_al_servidor(lista_datos):
    try:
        with grpc.insecure_channel('localhost:5000') as canal:
            cliente = calculo_pb2_grpc.ServidorCalculoStub(canal)
            respuesta = cliente.CalcularMaximo(calculo_pb2.NumeroLista(numeros=lista_datos))
            return respuesta.maximo
    except grpc.RpcError as e:
        print(f"Ocurrió un error al conectar con el servidor de cálculo: {e}")
        return None

def main():
    print("¡BIENVENIDO!\nEncuentra el número mayor de tu lista")
    nomArchivo = input("Escribe el nombre de tu archivo: ")

    lista = leer_archivo(nomArchivo)
    if lista is not None:
        respuesta = enviar_datos_al_servidor(lista)
        if respuesta is not None:
            print(f"El número mayor es: {respuesta}")
        else:
            print("No se pudo obtener el número mayor.")

if __name__ == '__main__':
    main()
