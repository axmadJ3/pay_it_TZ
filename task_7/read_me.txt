1. Подключение к контейнеру PostgreSQL
   - Сначала проверьте запущенные контейнеры:  
      docker ps

   - Найдите ID контейнера с PostgreSQL (например, `postgres_db` в нашем `docker-compose.yml`).  

   - Затем подключитесь к контейнеру:  
      docker exec -it postgres_db psql -U user -d task_7_db


2. Все SQL запросы в файле -> sql_queries.sql
