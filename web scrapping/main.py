import requests
import bs4
from fake_headers import Headers


HEADER = Headers(headers=False)
KEYWORDS = ['трекинг', 'бенчмарки', 'Бизнес', 'телефон']

url = 'https://habr.com/ru/all'

response = requests.get(url, headers=HEADER.generate())
text = response.text
soap = bs4.BeautifulSoup(text, features='html.parser')
articles = soap.find_all('article')

if __name__ == '__main__':
    for article in articles:
        all_preview = article.find_all(class_="tm-article-body tm-article-snippet__lead")
        all_preview = [one_preview.text.strip() for one_preview in all_preview]
        for one_preview in all_preview:
            for elem in one_preview.split():
                if elem in KEYWORDS:
                    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                    full_href = f'https://habr.com{href}'
                    title = article.find('h2').find('span').text
                    date_of_publication = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                    print(f'<{date_of_publication}> - <{title}> - <{full_href}>')


