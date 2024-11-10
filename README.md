# RezkaScraper

RezkaScraper — это библиотека на Python для асинхронного поиска контента (аниме, фильмов, сериалов и мультфильмов) на сайте Rezka.ag.

## Возможности:
- Поиск по названию: Выполняет поиск по ключевому слову и возвращает первое совпадение.
- Поиск по категориям: Поддержка категорий аниме, фильмы, сериалы, мультфильмы с пагинацией.

## Установка:
```
pip install rezka_scraper
```

## Пример использование:
```
import asyncio
from rezka_scraper import RezkaScraper

async def main():
    scraper = RezkaScraper()

    # Поиск по названию
    title, link = await scraper.search_rezka("Наруто")
    if title:
        print(f"Найдено: {title} - {link}")
    else:
        print("Ничего не найдено по запросу.")

    # Поиск аниме
    anime_results = await scraper.search_anime(page=1)
    print("Аниме на первой странице:")
    for title, link in anime_results:
        print(f"{title} - {link}")

    # Поиск фильмов
    movies_results = await scraper.search_movies(page=1)
    print("Фильмы на первой странице:")
    for title, link in movies_results:
        print(f"{title} - {link}")

asyncio.run(main())
```

# Примечания:
Для работы необходим стабильный интернет для выполнения запросов к сайту Rezka.ag.

Библиотека использует aiohttp для асинхронных HTTP-запросов и BeautifulSoup для парсинга HTML-контента.

# Лицензия:
Данный проект распространяется под лицензией MIT.