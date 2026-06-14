
# Модуль построения облака слов

import pandas as pd

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_wordcloud():
    
# Создает облако слов на основе частотного анализа

    # Загружаем таблицу частот
    df = pd.read_csv(
        "output/tables/frequencies.csv"
    )

    # Преобразуем таблицу в словарь
    frequencies = dict(
        zip(df["word"], df["count"])
    )

    # Создаем облако слов
    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color="white"
    ).generate_from_frequencies(
        frequencies
    )

    # Сохраняем изображение
    wordcloud.to_file(
        "output/plots/wordcloud.png"
    )

    return True