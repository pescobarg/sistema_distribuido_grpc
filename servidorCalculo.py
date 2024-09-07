import grpc
from concurrent import futures
import calculo_pb2
import calculo_pb2_grpc


class ServidorCalculo(calculo_pb2_grpc.ServidorCalculoServicer):
    def CalcularMaximo(self, request, context):
        lista = list(request.numeros)
        maximo = self.procesarLista(lista)
        return calculo_pb2.NumeroMaximo(maximo=maximo)
        
    def calculo_falla(self, lista):
        print("Servidor Calculo procede a realizar la operación por su cuenta")
        print(f"El número mayor de la lista es {max(lista)}")
        return max(lista)

    def enviarServidor(self, ip, puerto, sublista):
        try:
            with grpc.insecure_channel(f'{ip}:{puerto}') as canal:
                stub = calculo_pb2_grpc.ServidorOperacionStub(canal)
                peticion = calculo_pb2.NumeroLista(numeros=sublista)
                respuesta = stub.ObtenerMaximo(peticion)
                print(f"El servidor de cálculo recibe del servidor de operaciones {ip}:{puerto} el número {respuesta.maximo}")
                return respuesta.maximo
        except Exception as e:
            print(f"Error al conectar con el servidor {ip}:{puerto} - {e}")
            return None

    def procesarLista(self, lista):
        print(f"Servidor Calculo recibió del cliente: {lista}")
        
        mitad = len(lista) // 2
        subLista1 = lista[:mitad]
        subLista2 = lista[mitad:]

        servidores = [
            {'ip': 'localhost', 'puerto': 5001, 'sublista': subLista1},
            {'ip': 'localhost', 'puerto': 5002, 'sublista': subLista2}
        ]

        maximos = []
        for servidor in servidores:
            maximo = self.enviarServidor(servidor['ip'], servidor['puerto'], servidor['sublista'])
            if maximo is None:
                print(f"Intentando con el otro servidor para el subarreglo {servidor['sublista']}")
                otro_servidor = [s for s in servidores if s != servidor][0]
                maximo = self.enviarServidor(otro_servidor['ip'], otro_servidor['puerto'], servidor['sublista'])
                if maximo is None:
                    print("Error: Ambos servidores fallaron")
                    return self.calculo_falla(lista)
            maximos.append(maximo)

        print("El servidor de cálculo encontró el máximo: ", max(maximos))
        return max(maximos)

def iniciarServidor():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculo_pb2_grpc.add_ServidorCalculoServicer_to_server(ServidorCalculo(), server)
    server.add_insecure_port('[::]:5000')
    print("Servidor Calculo iniciado en el puerto 5000.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    iniciarServidor()
