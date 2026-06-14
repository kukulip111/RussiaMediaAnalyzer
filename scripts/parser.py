
# Модуль сбора новостей из RSS-лент СМИ.

import feedparser
import pandas as pd


# Ключевые слова для поиска публикаций
KEYWORDS = [
    "россия",
    "россии",
    "российский",
    "российская",
    "российские",
    "россиянин",
    "россияне",
    "россия",
    "росси"
]


# RSS-ленты СМИ
RSS_FEEDS = {
    "РБК": "https://rssexport.rbc.ru/rbcnews/news/30/full.rss",
    "Коммерсантъ": "https://www.kommersant.ru/RSS/news.xml",
    "РИА Новости": "https://ria.ru/export/rss2/archive/index.xml"
}


def collect_news():

# Собирает новости из RSS-лент и сохраняет их в CSV-файл

    news_list = []

    for source, url in RSS_FEEDS.items():

        try:
            feed = feedparser.parse(url)
            print(f"\nИсточник: {source}")
            print(f"Найдено записей: {len(feed.entries)}")

            for entry in feed.entries:

                title = entry.get("title", "")
                summary = entry.get("summary", "")
                published = entry.get("published", "")

                text = (title + " " + summary).lower()

                if any(word in text for word in KEYWORDS):

                    news_list.append({
                        "source": source,
                        "date": published,
                        "title": title,
                        "summary": summary
                    })

        except Exception as error:
            print(f"Ошибка при обработке {source}: {error}")

    df = pd.DataFrame(news_list)

    df.to_csv(
        "data/news.csv",
        index=False,
        encoding="utf-8-sig"
    )

    return len(df)