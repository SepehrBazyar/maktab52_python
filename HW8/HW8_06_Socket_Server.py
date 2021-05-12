# Written by: Sepehr Bazyar
import socket, logging, pickle, translators

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)-10s - %(message)s')

host, port = "", 9999 #localhost is 127.0.0.1 IP(this PC) and 9999 desire port(upper 8000)
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPv4 SOCK_STREAM TCP protocol
server_address = (host, port)
tcpsocket.bind(server_address)
logging.info("Server Created Successfully.")

logging.debug("Waiting for a Connection...")
tcpsocket.listen(1) #waiting for connection from 1 cleint request

client, addr = tcpsocket.accept()
logging.info(f"{addr[0]} IP at {addr[1]} Port Connected!")

while True:
    data = pickle.loads(client.recv(1024))
    logging.info("Get a Text Message!")
    if data[0]:
        text = "#$%^&*~!@"
        logging.debug("Translating...")
        try:
            text = getattr(translators, data[1])(data[0],
            to_language = data[2], from_language = data[3])
        except: logging.error("Invalid Text! Untranslatable...")
        else: logging.info("Send Translation for Client!")
        finally: client.send(text.encode())
    else:
        logging.warning("Client Disconnected!")
        tcpsocket.close()
        break

logging.warning("Closing Server.")
