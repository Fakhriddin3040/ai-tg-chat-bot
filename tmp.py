import os

# Определяем структуру папок и файлов
structure = {
    "src": {
        "bot.py": "",
        "config.py": "",
        "handlers": {
            "__init__.py": "",
            "start_handler.py": "",
            "help_handler.py": "",
            "menu_handler.py": "",
        },
        "keyboards": {
            "__init__.py": "",
            "main_menu.py": "",
            "sub_menu.py": "",
            "builder.py": "",
        },
        "services": {
            "__init__.py": "",
        },
        "utils": {},
    },
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # Если это папка
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Рекурсивно создаём вложенные элементы
        else:  # Если это файл
            with open(path, 'w') as file:
                file.write(content)

# Указываем начальный путь и создаём структуру
base_path = os.getcwd()  # Текущая директория
create_structure(base_path, structure)

print(f"Структура успешно создана в {base_path}")