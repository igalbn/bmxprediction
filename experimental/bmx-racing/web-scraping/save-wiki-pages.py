from bs4 import BeautifulSoup
import requests
import time
import re

read_interval = 30
save_folder_path ='wiki-pages/'

wiki_links = {
    'men':[
        'https://en.wikipedia.org/wiki/Cycling_at_the_2008_Summer_Olympics_%E2%80%93_Men%27s_BMX',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2012_Summer_Olympics_%E2%80%93_Men%27s_BMX',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2016_Summer_Olympics_%E2%80%93_Men%27s_BMX',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2020_Summer_Olympics_%E2%80%93_Men%27s_BMX_racing',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2024_Summer_Olympics_%E2%80%93_Men%27s_BMX_racing'
    ],
    'women':[
        'https://en.wikipedia.org/wiki/Cycling_at_the_2008_Summer_Olympics_%E2%80%93_Women%27s_BMX',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2012_Summer_Olympics_%E2%80%93_Women%27s_BMX',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2016_Summer_Olympics_%E2%80%93_Women%27s_BMX',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2020_Summer_Olympics_%E2%80%93_Women%27s_BMX_racing',
        'https://en.wikipedia.org/wiki/Cycling_at_the_2024_Summer_Olympics_%E2%80%93_Women%27s_BMX_racing'
    ]
}

def save_pages():
    pass
    for key in wiki_links.keys():
        for page_link in wiki_links[key]:
            page = requests.get(page_link)
            soup = BeautifulSoup(page.text,'html.parser')
            print('***')
            print(soup.title.text)
            pattern = r'at_the_(\d+)'
            year = re.search(pattern, page_link)
            if year:
                year = year.group(1)
            else:
                year = '____'
            
            full_path = f'{save_folder_path}{key}-{year}-bmx-racing-olympics-wiki.html'
            # print(soup.prettify())
            # Save the content to a file
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(soup.prettify())
            time.sleep(read_interval) # Delay between reading the pages

save_pages()
