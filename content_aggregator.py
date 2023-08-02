import requests
from bs4 import BeautifulSoup
import csv

def scrape_content(source_url):
    response = requests.get(source_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for article in soup.find_all('article'):
        title = article.find('h2').text.strip()
        url = article.find('a')['href']
        description = article.find('p').text.strip()

        articles.append({'title': title, 'url': url, 'description': description})

    return articles

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['title', 'url', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    sources = [
        'https://example.com/news',
        'https://exampleblog.com',
        # Add more sources here
    ]

    all_articles = []
    for source in sources:
        articles = scrape_content(source)
        all_articles.extend(articles)

    save_to_csv(all_articles, 'content_aggregator.csv')

if __name__ == "__main__":
    main()
