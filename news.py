import requests
from bs4 import BeautifulSoup

def fetch_news():
    file=open("news.txt","w",encoding='utf-8')
    url = "https://www.news18.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h3')
    for headline in headlines:
        a=headline.get_text(strip=True)
        file.write(a+"\n")


if __name__ == '__main__':
    fetch_news()