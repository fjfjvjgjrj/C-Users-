from bs4 import BeautifulSoup
import requests


url = "http://books.toscrape.com/catalogue/page-1.html"
top_books = []

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("h3")
    for book in books:
        title = book.a["title"]
        print(title)
        top_books.append(title)
    with open("top_books.txt", "w", encoding="utf-8") as file:
        for book in top_books:
            file.write(book + "\n")
    print("Назви книг додано успішно")

else:
    print("Ошибка при подключении к сайту")
