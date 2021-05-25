# Written by: Sepehr Bazyar
from requests import get
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')

URL = "https://www.pcmag.com/how-to/google-assistant-tips"
resp = get(URL)
if resp.ok:  # status code of response less than 400 successfully
    soup = BeautifulSoup(resp.text, 'html.parser')  # create instance
    print(soup.prettify(encoding='utf-8'))  # show good format text
    p_tags = [paragraph.get_text() for paragraph in soup.find_all('p')]
    with open("PCMAG.txt", 'w') as fl:
        print(*p_tags, sep='\n', file=fl)  # p_tags deleted <p> tags
    logging.info("Paragraphs Saved at PCMAG.txt File")
else:
    logging.error(f"HTTP Status Code: {resp.status_code}")
