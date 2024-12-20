#!/bin/bash

# Проверка наличия папки venv
if [ ! -d "venv" ]; then
    echo "Папка 'venv' не найдена. Создаем виртуальное окружение..."

    brew install python-tk

    # Создание виртуального окружения
    which python3
    python3 -m venv venv
    
    # Активируем виртуальное окружение
    source venv/bin/activate

    # Установка зависимостей из файла req.txt
    if [ -f "req.txt" ]; then
        echo "Устанавливаем зависимости из req.txt..."
        pip3 install -r req.txt
    else
        echo "Файл 'req.txt' не найден. Убедитесь, что он существует."
        exit 1
    fi

    echo "Виртуальное окружение и зависимости созданы."
else
    echo "Папка 'venv' уже существует. Активируем виртуальное окружение..."
fi

# Активируем виртуальное окружение
source venv/bin/activate

# Запуск проекта (здесь замените main.py на ваш основной файл)
echo "Запускаем проект..."
python3 src/main.py

# Деактивация (по желанию)
deactivate