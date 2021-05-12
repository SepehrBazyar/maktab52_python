# Written by: Sepehr Bazyar
import socket, logging, pickle #translators module in server code

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)-10s - %(message)s')

host, port = socket.gethostname(), 9999 #gethostname refrence to pc name or localhost
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
tcpsocket.connect(server_address) #connecting to server
logging.info("Connected to the Server.")

print("Welcome to My Translator Program ^_^\t{© Seper Bazyar}\n")
provider = input("Choose Your Provider[Google or Bing]? ").strip().lower() #choose translator
while provider not in ('google', 'bing'): #while provider != 'google' and provider != 'bing': ...
    print("Invalid Provider for Translating! Please Try Again...")
    provider = input("Choose Your Provider[Google or Bing]? ").strip().lower()
target_lang = input("Please Select Target Language -> ").strip().lower()[: 2] #just 2 first char
start_lang = input("Enter Your Language Text(Enter for Auto): ").strip().lower()[: 2] or "auto"

while True: #infinity loop
    message = input("Text(0 for Change Setting Just Enter Exit Program):\n<<< ").strip()
    if message == '0': #setup config setting of system change languages or translator provider
        print("\nPlease Just Enter for Unchanging Setting:\n") #just enter unchage value
        provider = input("Choose Your Provider[Google or Bing]? ").strip().lower() or provider
        while provider not in ('google', 'bing'):
            print("Invalid Provider for Translating! Please Try Again...")
            provider = input("Choose Your Provider[Google or Bing]? ").strip().lower() or provider
        target_lang = input("Please Select Target Language -> ").strip().lower()[: 2] or target_lang
        start_lang = input("Enter Your Language Text(Enter for Auto): ").strip().lower()[: 2] or start_lang
    else: #if message not 0 is a text or emtpy string mean enter for the exit
        tcpsocket.send(pickle.dumps([message, provider, target_lang, start_lang])) #send pickeling
        logging.debug("Successfully Send Text Message to Server for Translating.")
        if message:
            trans = tcpsocket.recv(1024).decode() #get a binary string from the server for result
            logging.debug("Successfully Get Translated Text Message from Server.")
            if trans != "#$%^&*~!@": print("Result Translated:\n>>>", trans)
            else: logging.error("Invalid Text! Please Try Again...") #error at translating
        else: #message is '' that boolean value is false
            logging.warning("Quit at Translator Program Server!")
            tcpsocket.close() #disconnect to server and close program
            break
