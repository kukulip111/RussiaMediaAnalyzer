
# Семантический анализ образа России в СМИ

# Основной язык: Python
# Вспомогательный язык: R

# Библиотека для создания графического интерфейса
import tkinter as tk


# Модуль для всплывающих окон и другие
from tkinter import messagebox

from scripts.parser import collect_news
from scripts.cleaner import process_news
from scripts.frequency import calculate_frequency
from scripts.cloud import create_wordcloud
from scripts.r_runner import build_graphs
from scripts.manual import open_manual

# Сбор новостей из СМИ
def collect_news_button():

    try:
        count = collect_news()

        messagebox.showinfo(
            "Успешно",
            f"Найдено {count} публикаций"
        )

    except Exception as error:

        messagebox.showerror(
            "Ошибка",
            str(error)
        )


# Очистка и обработка текстов
def process_text():

    try:

        count = process_news()

        messagebox.showinfo(
            "Успешно",
            f"Обработано {count} публикаций"
        )

    except Exception as error:

        messagebox.showerror(
            "Ошибка",
            str(error)
        )


# Подсчет частоты слов
def frequency_analysis():

    try:

        count = calculate_frequency()

        messagebox.showinfo(
            "Успешно",
            f"Найдено {count} частотных позиций"
        )

    except Exception as error:

        messagebox.showerror(
            "Ошибка",
            str(error)
        )


# Построение облака слов
def build_wordcloud():

    try:

        create_wordcloud()

        messagebox.showinfo(
            "Успешно",
            "Облако слов сохранено"
        )

    except Exception as error:

        messagebox.showerror(
            "Ошибка",
            str(error)
        )


# Построение графиков и диаграмм
def build_plots():

    try:

        build_graphs()

        messagebox.showinfo(
            "Успешно",
            "Графики построены"
        )

    except Exception as error:

        messagebox.showerror(
            "Ошибка",
            str(error)
        )


# Открытие инструкции пользователя по кнопке прописано в отдельном файле

# Создаем окно приложения
window = tk.Tk()

window.title("Семантический анализ образа России в СМИ")

window.geometry("500x450")


title_label = tk.Label(
    window,
   text="Семантический анализ публикаций\nоб образе России в СМИ",
    font=("Arial", 14, "bold")
)

title_label.pack(pady=20)

# Кнопка запуска сбора новостей
btn_news = tk.Button(
    window,
    text="Собрать новости",
    width=30,
    height=2,
    command=collect_news_button
)
btn_news.pack(pady=5)


# Кнопка обработки текстов
btn_process = tk.Button(
    window,
    text="Обработать тексты",
    width=30,
    height=2,
    command=process_text
)
btn_process.pack(pady=5)


# Кнопка частотного анализа
btn_frequency = tk.Button(
    window,
    text="Частотный анализ",
    width=30,
    height=2,
    command=frequency_analysis
)
btn_frequency.pack(pady=5)


# Кнопка построения облака слов
btn_cloud = tk.Button(
    window,
    text="Облако слов",
    width=30,
    height=2,
    command=build_wordcloud
)
btn_cloud.pack(pady=5)


# Кнопка построения графиков
btn_plots = tk.Button(
    window,
    text="Построить графики",
    width=30,
    height=2,
    command=build_plots
)
btn_plots.pack(pady=5)


# Кнопка открытия инструкции
btn_manual = tk.Button(
    window,
    text="Инструкция",
    width=30,
    height=2,
    command=open_manual
)
btn_manual.pack(pady=5)


# Кнопка выхода из программы
btn_exit = tk.Button(
    window,
    text="Выход",
    width=30,
    height=2,
    command=window.destroy
)
btn_exit.pack(pady=15)

# Запускаем цикл обработки событий окна.
# После этой команды программа начинает ждать нажатия кнопок пользователем
window.mainloop()