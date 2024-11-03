# db_test

Project Name : db_test

Структура проекта
        .
        ├── docker-compose.yml
        ├── nginx.conf
        ├── Server/
        │   ├── Dockerfile
        │   └── service.py
        │   └── requirements.txt
        └── db-init/
            └── db.sql

Предварительные требования:
        - Установите Docker Compose

Установка: 
    1.Клонируйте репозиторий:
    HTTP:
        git clone https://github.com/al13666/db_test.git
    или SSH:
        git clone git@github.com:al13666/db_test.git
    перейдите в репозиторий:
        cd /путь/к/проекту/

    2.Запустите контейнер:
        docker-compose up --build
    3.Приложение доступно по адресу:
        http://localhost:PORT
        пример: 
        http://127.0.0.1:80


