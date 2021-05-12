# Written by: Sepehr Bazyar
import socket, logging, pickle

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)-10s - %(message)s')

host, port = socket.gethostname(), 9999
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
tcpsocket.connect(server_address)
logging.info("Connected to the Server.")

provider = input("Choose Your Provider[Google or Bing]? ").strip().lower()
while provider not in ('google', 'bing'):
    print("Invalid Provider for Translating! Please Try Again...")
    provider = input("Choose Your Provider[Google or Bing]? ").strip().lower()
target_lang = input("Please Select Target Language -> ").strip().lower()[: 2]
start_lang = input("Enter Your Language Text(Enter for Auto): ").strip().lower()[: 2] or "auto"

while True:
    message = input("Text(Just Enter Exit Program)<<< ").strip()
    tcpsocket.send(pickle.dumps([message, provider, target_lang, start_lang]))
    logging.debug("Successfully Send Text Message to Server for Translating.")
    if message:
        trans = tcpsocket.recv(1024).decode()
        logging.debug("Successfully Get Translated Text Message from Server.")
        if trans != "#$%^&*~!@": print("Result Translated >>>", trans)
        else: logging.error("Invalid Text! Please Try Again...")
    else:
        logging.warning("Quit at Translator Program Server!")
        tcpsocket.close()
        break
