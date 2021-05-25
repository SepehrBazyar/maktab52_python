# Written by: Sepehr Bazyar
from requests import get
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')

URL = "https://virgool.io/@mmt/%D9%85%DB%8C%D9%86%DB%8C%D9%BE%D8%B3%D8%AA-carbon-%D8%B2%DB%8C%D8%A8%D8%A7%DB%8C%DB%8C-%DA%A9%D8%AF%D9%87%D8%A7%DB%8C%D8%AA%D8%A7%D9%86-%D8%A8%D8%A7-%D9%85%D8%A7-i21qbl6d2omb"
resp = get(URL)
soup = BeautifulSoup(resp.text, 'html.parser')

if resp.ok:
    print(soup.prettify(encoding='utf-8'))
    p_tags = soup.find_all('p')
    with open("Virgool.txt", 'w') as fl:
        print(*p_tags, sep='\n', file=fl)
    logging.info("Paragraphs Saved at Virgool.txt File")
