# Playwright Setup Guide

## Установка проекта

### 1. Активируйте виртуальное окружение

#### Windows:
```bash
venv\Scripts\activate
```

#### macOS и Linux:
```bash
source venv/bin/activate
```

### 2. Установите зависимости:
```bash
pip install -r requirements.txt
```
#### Убедитесь, что у вас установлен Python и необходимые зависимости из файла `requirements.txt`.
#### Для корректной работы Playwright требуется актуальная версия браузеров, которые могут быть установлены с помощью команды:
```bash
playwright install
```

### 3. Запустите тесты:

#### Запуск всех тестов на PRE с логами:
```bash
pytest --log-cli-level=DEBUG
```
#### Запуск смок тестов
```bash
pytest -m "smoke"
```
#### Запуск регресс тестов
```bash
pytest -m "regression"
```
#### Запуск smoke and not xfail на стенде devtest5
###### с пропуском ожидаемо упавших тестов (т.е. не запускаем xfail)
```bash
pytest --env=devtest5 --log-cli-level=DEBUG -m "smoke and not xfail"
```
#### Запуск теста по названию 
######  поиск названия и запуск по подстроке
```bash
pytest -k "cart or order"
```

