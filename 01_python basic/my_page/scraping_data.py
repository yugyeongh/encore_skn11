from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def scraping():
    url = 'https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024&type=pitcher&playerOrder=era'
    response = requests.get(url)
    response.raise_for_status()
    
    return response

def baseball_data():
    html = scraping().text
    soup = bs(html, 'html.parser')
    table = soup.find_all("table")[0]

    header = soup.find_all("thead")[0]
    headers = [th.get_text(strip=True) for th in header.find_all("span", class_="blind")]

    body = soup.find_all("tbody")[0]
    rows = body.find_all('tr')

    data = []
    for row in rows:
        cells = row.find_all(['th', 'td'])
        row_data = []
        for cell in cells:
            row_data.append(cell.text.strip())
        data.append(row_data)
    
    df = pd.DataFrame(data, columns=headers)
    df.set_index('순위', inplace=True)

    return df
    