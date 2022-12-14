# React-Flask URL Shortener
### Веб-сервис для создания коротких URL

Приложение, позволяющее для любой ссылки получить короткий аналог и затем пользоваться им любое количество времени для перенаправления на реальный источник.

- 💻 Frontend написан на React + TypeScript
- 🔨 Backend написан на Flask + Python
- 💾 База данных - MongoDB
### Features

- Учитывает необходимые параметры запроса: протокол, домен, путь, порт, параметры и якори.
- Валидирует URL на стороне frontend и backend.
### Prerequisites

- Для корректной работы необходимо иметь установленный сервер MongoDB, а так же зарегистрированного пользователя (по умолчанию: username='flask', password='flask') с readWrite правами в базе данных, куда планируется делать записи (по умолчанию база: 'flask-db', коллекция: 'url')
- Для корректной работы необходимо установить зависимости из backend/requirements.txt (pip install) и frontend/package.json (npm install)
