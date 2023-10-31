# Задание 1
## Start

```bash
docker-compose up --build -d
```

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/api/v1/get_all

В swagger несколько эндпоинтов, по которым добавляются или считываются записи:

1 GET /api/v1/get_all - получение списка всех номеров

2 GET /api/v1/check_data - получение адреса по номеру

3 POST /api/v1/write_data - запись новой пары {'номер': 'адрес'}

4 PATCH /api/v1/write_data - изменение адреса по номеру телефона


# Задание 2
## Для запуска процедуры

SELECT update_full_names_status();

## Тело процедуры

CREATE FUNCTION update_full_names_status()

RETURNS VOID AS $$

DECLARE

    item TEXT;

BEGIN

    FOR item IN SELECT DISTINCT filename FROM full_names
    LOOP
        UPDATE full_names AS fn
        SET status = s.status
        FROM short_names AS s
        WHERE s.filename || item = fn.filename;
    END LOOP;

END;
