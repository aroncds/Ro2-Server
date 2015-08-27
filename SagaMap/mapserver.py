import socket
import thread

import settings
import loginsession as LoginSession

from packet import Packet
from manager.mapclientmanager import MapClientManager

from client.map.mapclient import MapClient
from packets.map.List import dict_packets

print("Comecando a inicializar o servidor")
mapmanager = MapClientManager()

def startServer():
	print("Iniciando conexao com servidor de Login...")

	LoginSession.host = settings.LOGIN_HOST
	LoginSession.port = settings.LOGIN_PORT
	thread.start_new_thread(LoginSession.startConnectionLoginServer, ())

	print("Iniciando servidor de mapa")

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind((settings.HOST, settings.PORT))
	tcp.listen(1)

	while 1:
		con, cliente = tcp.accept()
		thread.start_new_thread(map_server, (con, cliente))

def map_server(connection, client):
	local_client = MapClient(connection)
	mapmanager.set_client(local_client)

	while 1:
		msg = connection.recv(1024)
		pck = Packet()
		pck.data = bytearray(msg)

		local_client.OnPacketData(pck.getPacketID(), pck.data, dict_packets)

	Thread.exit()


startServer()