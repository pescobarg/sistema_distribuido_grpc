import grpc
from concurrent import futures
import calculo_pb2
import calculo_pb2_grpc
import time
import sys

class ServidorOperacion(calculo_pb2_grpc.ServidorOperacionServicer):
    def ObtenerMaximo(self, request, context):
        subarray = request.numeros
        print(f"Servidor de Operación recibió el subarreglo: {subarray}")
        try:
            max_value = max(subarray)
            print(f"Servidor de Operación encontró el valor máximo: {max_value}")
            return calculo_pb2.NumeroMaximo(maximo=max_value)
        except Exception as e:
            print(f"Error en el Servidor de Operación: {e}")
            context.set_details('Error al procesar la solicitud.')
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculo_pb2.NumeroMaximo()

def serve(port):
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculo_pb2_grpc.add_ServidorOperacionServicer_to_server(ServidorOperacion(), servidor)
    servidor.add_insecure_port(f'[::]:{port}')
    servidor.start()
    print(f"Servidor de Operación iniciado en el puerto {port}. Esperando conexiones...")
    try:
        while True:
            time.sleep(86400)  # Mantiene el servidor en ejecución
    except KeyboardInterrupt:
        servidor.stop(0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python servidor_operacion.py <puerto>")
        sys.exit(1)

    puerto = int(sys.argv[1])
    serve(puerto)
