# СтудПортфолио

Веб-приложение для управления студенческим портфолио мероприятий.

## Возможности

- Регистрация студентов и преподавателей
- Каталог мероприятий (спортивные, культурные, научные, волонтёрские, личные)
- Загрузка подтверждающих документов (дипломы, грамоты, сертификаты)
- Добавление ссылок на соц. сети с упоминанием
- Проверка и одобрение/отклонение документов преподавателем

## Технологии

- **Backend**: Python, FastAPI, SQLAlchemy, SQLite
- **Frontend**: HTML, CSS, JavaScript (single-page)

## Локальный запуск

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

Откройте http://localhost:8000 в браузере.

**Демо-аккаунты:**
- Студент: `student@portal.ru` / `student123`
- Преподаватель: `teacher@portal.ru` / `teacher123`

## Деплой на Render.com (бесплатно)

1. Зарегистрируйтесь на [render.com](https://render.com)
2. Нажмите **New** → **Web Service**
3. Подключите этот GitHub-репозиторий
4. Render автоматически обнаружит `render.yaml` и настроит сервис
5. Нажмите **Deploy**

Или используйте Docker:

```bash
docker build -t studportfolio .
docker run -p 8000:8000 -v studdata:/data -e DATA_DIR=/data studportfolio
```
