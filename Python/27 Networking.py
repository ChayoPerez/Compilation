import socket
import threading
import json
import time


def send(value, socket):
	msg_json = json.dumps(value)
	msg_bytes = msg_json.encode()
	msg_length = len(msg_bytes).to_bytes(4, byteorder="big")
	socket.send(msg_length + msg_bytes)

class Server:

	def __init__(self):
		print("Server: Initializing server...")
		self.host = "127.0.0.1"
		self.port = 1234
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.server_socket.bind((self.host, self.port))
		print("Server: Host and port binded...")

		self.server_socket.listen(10)
		print("Server: listening...")

		thread = threading.Thread(target=self.accept_connections_thread, daemon=True)
		thread.start()
		print("Server: Accepting clients")

	def accept_connections_thread(self):
		while True:
			client_socket, _ = self.server_socket.accept()
			print("Server: Connection to client started")
		 
			listening_client_thread = threading.Thread(
				target=self.listen_client_thread,
				args=(client_socket,),
				daemon=True
			)
			listening_client_thread.start()

	def listen_client_thread(self, client_socket):
		while True:
		
			# we get the number of bytes the message that arrived has	
			response_bytes_length = client_socket.recv(4)
			response_length = int.from_bytes(response_bytes_length, byteorder="big")

			# The respones we will decode:
			response = bytearray()

			# Since response is an array, it will get bigger
			# until it has the same length as the original
			while(len(response) < response_length):
				size = 256
				if response_length - len(response) < 256:
					size = response_length - len(response)

				# You add bytes to the response
				response += client_socket.recv(size)

			response = response.decode() #  response is an encoded  json
			decoded_json = json.loads(response) # decoded is a json
			self.handle_command(decoded_json, client_socket)

	def handle_command(self, received, client_socket):
		print("Server: Message received: {}".format(received))
		if received["status"] == "ready":
			print("Server: Connection is ready.")
			msg = {"status": "reply", "msg": "hello wordl!"}
			send(msg, client_socket)


# class ServerClient:

#    	def __init__(self, socket):
# 	  	self.socket = socket


class Client:

	def __init__(self):
		print("Client: Initializing client...")
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = "127.0.0.1"
		self.port = 1234
		try:
			self.client_socket.connect((self.host, self.port))
			print("Client: Client connected to server...")
		except:
			print("Client: Couldn't connect...")

		thread = threading.Thread(target=self.listen_thread, daemon=True)
		thread.start()
		print("Client: Listening to server")

		print("Client: Request to start connection sent.")
		msg = {"status": "ready"}
		send(msg, self.client_socket)

	def listen_thread(self):
		while True:
			response_bytes_length = self.client_socket.recv(4)
			response_length = int.from_bytes(response_bytes_length,
											 byteorder="big")
			response = bytearray()
			while(len(response) < response_length):
				size = 256
				if response_length - len(response) < 256:
					size = response_length - len(response)
				response += self.client_socket.recv(size)
			response = response.decode()
			decoded = json.loads(response)
			self.handle_command(decoded)

	def handle_command(self, decoded):
		print("Client: Message received: {}".format(decoded))



s = Server()
c1 = Client()
time.sleep(5)