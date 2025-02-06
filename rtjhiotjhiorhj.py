import requests
import json

url = "https://api.jikan.moe/v4/top/anime"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    popular_anime = []
    for anime in data["data"]:
        title = anime["title"]
        score = anime["score"]
        popular_anime.append({
            "title": title,
            "score": score
        })

    with open("popular_anime.json", "w", encoding="utf-8") as file:
        json.dump(popular_anime, file, ensure_ascii=False, indent=4)
    print("Данні про популярні аніме успішно збережені в popular_anime.json")

else:
    print("Помилка при підключенні до API")
