
# Модуль очистки и лемматизации текстов

import pandas as pd
import re
import pymorphy3

from nltk.corpus import stopwords


# Морфологический анализатор для получения начальной формы слов
morph = pymorphy3.MorphAnalyzer()

# Русские стоп-слова
russian_stopwords = set(stopwords.words("russian"))

# Загружаем собственный список стоп-слов
with open("data/stopwords.txt", encoding="utf-8") as file:

    custom_stopwords = {
        line.strip()
        for line in file
        if line.strip()
    }

russian_stopwords.update(custom_stopwords)



def clean_text(text):

# Очищает текст и приводит слова к начальной форме.

    # Если текст отсутствует, заменяем его пустой строкой
    if pd.isna(text):
        text = ""
    
    # Нижний регистр
    text = text.lower()

    # Удаляем всё кроме русских букв и пробелов
    text = re.sub(r"[^а-яё\s]", " ", text)

    words = text.split()

    cleaned_words = []

    for word in words:

        # Получаем начальную форму слова
        lemma = morph.parse(word)[0].normal_form

        # Проверяем уже лемму
        if lemma in russian_stopwords:
            continue

        cleaned_words.append(lemma)

    return " ".join(cleaned_words)


def process_news():

 # Обрабатывает все собранные новости.


    # Загружаем новости
    df = pd.read_csv("data/news.csv")

    # Заменяем пропуски пустыми строками
    df["title"] = df["title"].fillna("")
    df["summary"] = df["summary"].fillna("")

    # Объединяем заголовок и описание
    df["full_text"] = df["title"] + " " + df["summary"]

    # Создаем очищенный текст
    df["clean_text"] = df["full_text"].apply(clean_text)

    # Сохраняем результат
    df.to_csv(
        "output/tables/clean_news.csv",
        index=False,
        encoding="utf-8-sig"
    )

    return len(df)