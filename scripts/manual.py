
# Модуль открытия инструкции пользователя
import os

def open_manual():

    # Путь к PDF-файлу инструкции
    pdf_path = os.path.join(
        "notes",
        "user_manual.pdf"
    )
    print("Открываю:", os.path.abspath(pdf_path))
    
    # Открываем PDF через программу по умолчанию
    os.startfile(pdf_path)