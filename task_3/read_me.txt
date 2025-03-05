1. Запускаем контейнер ->
    -- Шаг 1: Открываем терминал в папке task_3 и выполняем:
            docker-compose up -d

    -- Шаг 2: Проверяем запущенные контейнеры. Должен появиться контейнер my_postgres_db:
            docker ps


2. Подключение к базе PostgreSQL ->
    -- Подключаемся к базе данных прямо внутри контейнера:
            docker exec -it my_postgres_db psql -U myuser -d mydatabase

    -- Проверяем даные:
            SELECT * FROM orders;

    -- SQL запросы находятся в файле:
            sql_queries.sql


3. Остановка и удаление контейнера ->
    -- Чтобы остановить контейнер:
            docker-compose down

    -- Чтобы удалить контейнер и данные. Удаляет volume postgres_data и все сохранённые данные:
            docker-compose down -v
