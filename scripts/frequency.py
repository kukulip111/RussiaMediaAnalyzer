
# Модуль частотного анализа текста

import pandas as pd
from collections import Counter


def calculate_frequency():
# Подсчитывает частоту слов в обработанных текстах

    # Загружаем очищенные новости
    df = pd.read_csv("output/tables/clean_news.csv")

    all_words = []

    # Собираем все слова из столбца clean_text
    for text in df["clean_text"]:

        if pd.isna(text):
            continue

        words = text.split()

        all_words.extend(words)

    # Подсчет частот
    word_counts = Counter(all_words)

    top_words = word_counts.most_common()

    result_df = pd.DataFrame(
        top_words,
        columns=["word", "count"]
    )

    # Сохраняем таблицу
    result_df.to_csv(
        "output/tables/frequencies.csv",
        index=False,
        encoding="utf-8-sig"
    )

    return len(result_df)