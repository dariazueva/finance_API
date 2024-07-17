# Finance_API

## Описание проекта

API для учета финансовых операций, разработанное с использованием фреймворка Django. API предоставляет следующие возможности:

- Создание счета
- Получение списка счетов
- Создание операции
- Удаление операции
- Получение списка операций с фильтрацией


### Основной стек технологий проекта:

python, django, docker, postgresql, django rest framework

### Как запустить проект с помощью Docker:

#### Создайте директорию foodgram .
```bash
mkdir finance_API
cd finance_API
```
#### Скачайте или скопируйте файл docker-compose.yml из этого репозитория.

#### Создайте файл .env и заполните его своими данными по образцу.
```bash
POSTGRES_USER=financeuser
POSTGRES_PASSWORD=financepass
POSTGRES_DB=finance
DB_HOST=db
DB_PORT=5432
SECRET_KEY = "ваш-секретный-ключ"

```
#### Запустите систему контейнеров.
```bash
docker-compose up --build
```
#### Выпоните миграции в контейнере backend.
```bash
docker-compose exec backend python manage.py migrate
```
#### Создайте суперпользователя.
```bash
docker-compose exec backend python manage.py createsuperuser
```
#### Остановить контейнер.
```bash
docker-compose down
```

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/