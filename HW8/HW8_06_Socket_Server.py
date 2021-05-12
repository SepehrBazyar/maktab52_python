# Written by: Sepehr Bazyar
import socket, logging, pickle, translators

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)-10s - %(message)s')

host, port = "", 9999 #"" or localhost is 127.0.0.1 IP(this PC) and 9999 desire port(upper 8000)
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPv4 SOCK_STREAM TCP protocol
server_address = (host, port)
tcpsocket.bind(server_address) #create server
logging.info("Server Created Successfully.")

logging.debug("Waiting for a Connection...")
tcpsocket.listen(1) #waiting for connection from 1 cleint request

client, addr = tcpsocket.accept() #addr is a tuple
logging.info(f"{addr[0]} IP at {addr[1]} Port Connected!")

while True: #infinity loop
    data = pickle.loads(client.recv(1024)) #get from the client(before convert from pickling)
    logging.info("Get a Text Message!")
    if data[0]: #data[0] is a user message can be a string to translate or empty to exit
        text = "#$%^&*~!@" #a symbol for when error at translate so send for client
        logging.debug("Translating...")
        try:
            text = getattr(translators, data[1])(data[0], #use getattr func because providers
            to_language = data[2], from_language = data[3])
        except: logging.error("Invalid Text! Untranslatable...")
        else: logging.info("Send Translation for Client!")
        finally: client.send(text.encode()) #at last must be send a text to client finally
    else:
        logging.warning("Client Disconnected!")
        tcpsocket.close() #close server and end program
        break

logging.warning("Closing Server.")
