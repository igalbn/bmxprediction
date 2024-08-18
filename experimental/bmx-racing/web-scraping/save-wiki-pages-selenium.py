from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
import re

read_interval = 30

json_path = 'properties/pages_links.json'
save_folder_path ='wiki-pages/'

# Read the links from the JSON file
with open(json_path, 'r') as file:
    wiki_links = json.load(file)


def save_pages():
    driver = webdriver.Chrome()
    
    for key in wiki_links.keys():
        pass
        for page_link in wiki_links[key]:
            pass
            print(page_link)
            driver.get(page_link)
            time.sleep(read_interval)
            
            # extract year from the link
            pattern = r'at_the_(\d+)'
            year = re.search(pattern, page_link)
            if year:
                year = year.group(1)
            else:
                year = '____'

            full_path = f'{save_folder_path}{key}-{year}-bmx-racing-olympics-wiki.html'
            html_content = driver.page_source
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
              
    print('completed')

save_pages()
