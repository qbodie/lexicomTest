### Start (Задание 1)

```bash
docker-compose up --build -d
```

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/api/v1/get_all


## Для выполнения процедуры (Задание 2)

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
