from packet import Packet


class Client(object):
	sessionID = 0
	connection = None

	def __init__(self, connection):
		self.connection = connection

	def sendPacket(self, pck):
		try:
			if(self.connection):
				pck.setSessionID(self.sessionID)
				self.connection.send(bytearray(pck.data))
		except:
			print("Ocorreu um erro ao enviar o pacote")


	def OnPacketData(self, id_packet, data, dict_packet):
		if id_packet in dict_packet:
			packet_class = dict_packet[id_packet]['class']()
			packet_class.data = data
			dict_packet[id_packet]['function'](self, packet_class)
		else:
			print(
				"Unknow package ID: "\
				+ str(id_packet) + " with data length: "\
				+ str(len(data))
			)