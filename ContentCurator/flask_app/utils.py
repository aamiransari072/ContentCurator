import os 
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from flask_app.constant import getConfig
load_dotenv()


def search_engine(query):


    endpoint = "https://www.googleapis.com/customsearch/v1"

    response = requests.get(endpoint,params=getConfig.get_config())

    if response.status_code == 200:
        results = response.json().get('items',[])
        extracted_result = [{
            "title": result.get('title'),
            "link": result.get('link'),
            "snippet": result.get('snippet')

        }
        for result in results
        
        ]
        return extracted_result
    else:
        print(f'Erro: {response.status_code} - {response.text}')
        return []




def get_para(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content,'html5lib')
    para = soup.find_all('p')

    cleand = []
    for p in para:
        for unwanted in p(['a', 'br', 'script', 'style']):
            unwanted.decompose()
        text = p.get_text(separator=" ", strip=True)
        cleand.append(text)
    return "\n\n".join(cleand)
        
        
def get_data(query):
    response = search_engine(query,getConfig.get_config())
    data = []
    for r in response:
        url = r['link']
        temp = get_para(url)
        data.append(temp)
    return data
    